<#
.SYNOPSIS
  Erkundet eine VFM-Installation und sucht Replays. Liest nur, verändert nichts.

.DESCRIPTION
  1. Findet VFM in allen Steam-Bibliotheken (appmanifest), Unity-Version, Mono oder IL2CPP,
     mitgelieferte Bibliotheken (verraten das Serialisierungsformat), lesbare Konfigdateien.
  2. Sucht Datenordner (AppData\LocalLow, Roaming, Local, Dokumente, Gespeicherte Spiele,
     Steam-Cloud) und beschreibt jede Datei: Größe, Datum, Magic Bytes, Entropie,
     Probe-Entpacken (gzip, zlib, zip).
  3. Optional (-Bezeichner): sucht in Assembly-CSharp.dll bzw. global-metadata.dat nach
     Bezeichnern mit Replay/Record/Playback/Snapshot. Das ist ein reiner Text-Scan, keine
     Dekompilierung. Vorher die EULA prüfen.
  4. Optional (-Proben n): kopiert die n neuesten Replay-Kandidaten in den Ausgabeordner.

  Pfade im Bericht sind anonymisiert (%USERPROFILE%). Vor dem Teilen trotzdem lesen.

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File tools\replays\erkunden.ps1
  powershell -ExecutionPolicy Bypass -File tools\replays\erkunden.ps1 -Bezeichner -Proben 3
#>
param(
    [string]$Ausgabe = (Join-Path $PSScriptRoot "erkundung"),
    [switch]$Bezeichner,
    [int]$Proben = 0,
    [int]$MaxDateien = 400
)

$ErrorActionPreference = "Continue"
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

New-Item -ItemType Directory -Force -Path $Ausgabe | Out-Null
$bericht = New-Object System.Collections.Generic.List[string]
$json = [ordered]@{ erstellt = (Get-Date).ToString("s"); installation = $null; datenordner = @(); dateien = @(); bezeichner = $null }

function Anon([string]$s) {
    if (-not $s) { return $s }
    $s = $s -replace [regex]::Escape($env:USERPROFILE), '%USERPROFILE%'
    return $s -replace [regex]::Escape($env:USERNAME), '<USER>'
}
function Z([string]$s = "") { $bericht.Add($s); Write-Host $s }
function Groesse([long]$b) {
    if ($b -ge 1GB) { return "{0:N1} GB" -f ($b / 1GB) }
    if ($b -ge 1MB) { return "{0:N1} MB" -f ($b / 1MB) }
    if ($b -ge 1KB) { return "{0:N1} KB" -f ($b / 1KB) }
    return "$b B"
}

function Lies-Kopf([string]$pfad, [int]$n) {
    $fs = [System.IO.File]::Open($pfad, 'Open', 'Read', 'ReadWrite')
    try {
        $buf = New-Object byte[] ([Math]::Min($n, [Math]::Max(0, $fs.Length)))
        $gelesen = $fs.Read($buf, 0, $buf.Length)
        if ($gelesen -eq 0) { return ,(New-Object byte[] 0) }
        if ($gelesen -lt $buf.Length) { $buf = $buf[0..($gelesen - 1)] }
        return ,$buf
    } finally { $fs.Dispose() }
}

function Hex([byte[]]$b, [int]$n = 32) {
    if (-not $b -or $b.Length -eq 0) { return "" }
    $m = [Math]::Min($n, $b.Length)
    return (($b[0..($m - 1)] | ForEach-Object { $_.ToString("X2") }) -join " ")
}

function Ascii([byte[]]$b, [int]$n = 32) {
    if (-not $b -or $b.Length -eq 0) { return "" }
    $m = [Math]::Min($n, $b.Length)
    return -join ($b[0..($m - 1)] | ForEach-Object { if ($_ -ge 32 -and $_ -lt 127) { [char]$_ } else { "." } })
}

function Entropie([byte[]]$b) {
    if (-not $b -or $b.Length -eq 0) { return 0 }
    $z = New-Object int[] 256
    foreach ($x in $b) { $z[$x]++ }
    $h = 0.0; $n = $b.Length
    foreach ($c in $z) { if ($c -gt 0) { $p = $c / $n; $h -= $p * [Math]::Log($p, 2) } }
    return [Math]::Round($h, 2)
}

function Druckbar([byte[]]$b) {
    if (-not $b -or $b.Length -eq 0) { return 0 }
    $d = 0
    foreach ($x in $b) { if (($x -ge 32 -and $x -lt 127) -or $x -eq 9 -or $x -eq 10 -or $x -eq 13) { $d++ } }
    return [Math]::Round($d / $b.Length, 2)
}

function Magic([byte[]]$b) {
    if (-not $b -or $b.Length -lt 2) { return "leer" }
    $h = Hex $b 8
    $a = Ascii $b 16
    if ($b[0] -eq 0x1F -and $b[1] -eq 0x8B) { return "gzip" }
    if ($b[0] -eq 0x78 -and @(0x01, 0x5E, 0x9C, 0xDA) -contains $b[1]) { return "zlib" }
    if ($h.StartsWith("50 4B 03 04")) { return "zip" }
    if ($h.StartsWith("28 B5 2F FD")) { return "zstd" }
    if ($h.StartsWith("04 22 4D 18")) { return "lz4-frame" }
    if ($h.StartsWith("FD 37 7A 58 5A")) { return "xz" }
    if ($a.StartsWith("BZh")) { return "bzip2" }
    if ($a.StartsWith("UnityFS")) { return "Unity-AssetBundle" }
    if ($a.StartsWith("SQLite format 3")) { return "SQLite" }
    if ($h.StartsWith("89 50 4E 47")) { return "png" }
    if ($h.StartsWith("FF D8 FF")) { return "jpeg" }
    if ($a.StartsWith("RIFF")) { return "riff" }
    if ($h.StartsWith("EF BB BF")) { return "Text (UTF-8 BOM)" }
    if ($h.StartsWith("FF FE") -or $h.StartsWith("FE FF")) { return "Text (UTF-16 BOM)" }
    $t = $a.TrimStart()
    if ($t.StartsWith("{") -or $t.StartsWith("[")) { return "JSON?" }
    if ($t.StartsWith("<")) { return "XML?" }
    if ($b[0] -ge 0x80 -and $b[0] -le 0x8F) { return "MessagePack-Map?" }
    return "unbekannt"
}

function Probe-Entpacken([string]$pfad, [string]$art) {
    try {
        if ($art -eq "zip") {
            $z = [System.IO.Compression.ZipFile]::OpenRead($pfad)
            try { return "zip-Inhalt: " + (($z.Entries | Select-Object -First 20 | ForEach-Object { "$($_.FullName) ($($_.Length) B)" }) -join "; ") }
            finally { $z.Dispose() }
        }
        if ($art -ne "gzip" -and $art -ne "zlib") { return $null }
        $fs = [System.IO.File]::Open($pfad, 'Open', 'Read', 'ReadWrite')
        try {
            if ($art -eq "zlib") { $fs.Seek(2, 'Begin') | Out-Null; $s = New-Object System.IO.Compression.DeflateStream($fs, [System.IO.Compression.CompressionMode]::Decompress) }
            else { $s = New-Object System.IO.Compression.GZipStream($fs, [System.IO.Compression.CompressionMode]::Decompress) }
            $ms = New-Object System.IO.MemoryStream
            $buf = New-Object byte[] 65536
            $gesamt = 0L
            while (($n = $s.Read($buf, 0, $buf.Length)) -gt 0) {
                if ($ms.Length -lt 16384) { $ms.Write($buf, 0, [Math]::Min($n, 16384 - [int]$ms.Length)) }
                $gesamt += $n
            }
            $kopf = $ms.ToArray()
            return "entpackt $(Groesse $gesamt) (Faktor {0:N1}), Kopf: {1} | {2} | Entropie {3}, druckbar {4}" -f ($gesamt / (Get-Item $pfad).Length), (Hex $kopf 32), (Ascii $kopf 32), (Entropie $kopf), (Druckbar $kopf)
        } finally { $fs.Dispose() }
    } catch { return "Entpacken fehlgeschlagen: $($_.Exception.Message)" }
}

# ---------------------------------------------------------------- 1. Installation
Z "# VFM-Erkundung $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
Z ""
Z "## 1. Installation"
Z ""

$steam = $null
foreach ($k in @('HKCU:\Software\Valve\Steam', 'HKLM:\SOFTWARE\WOW6432Node\Valve\Steam')) {
    try {
        $p = Get-ItemProperty -Path $k -ErrorAction Stop
        if ($p.SteamPath) { $steam = $p.SteamPath; break }
        if ($p.InstallPath) { $steam = $p.InstallPath; break }
    } catch {}
}
if (-not $steam -and (Test-Path "C:\Program Files (x86)\Steam")) { $steam = "C:\Program Files (x86)\Steam" }
$steam = if ($steam) { $steam -replace '/', '\' } else { $null }
Z "- Steam: $steam"

$bibliotheken = New-Object System.Collections.Generic.List[string]
if ($steam) {
    $bibliotheken.Add($steam)
    $vdf = Join-Path $steam "steamapps\libraryfolders.vdf"
    if (Test-Path $vdf) {
        foreach ($m in [regex]::Matches((Get-Content $vdf -Raw), '"path"\s+"([^"]+)"')) {
            $p = $m.Groups[1].Value -replace '\\\\', '\'
            if (-not ($bibliotheken -contains $p)) { $bibliotheken.Add($p) }
        }
    }
}
Z "- Steam-Bibliotheken: $($bibliotheken -join ', ')"

$inst = $null; $appid = $null
foreach ($lib in $bibliotheken) {
    foreach ($acf in Get-ChildItem -Path (Join-Path $lib "steamapps") -Filter "appmanifest_*.acf" -ErrorAction SilentlyContinue) {
        $t = Get-Content $acf.FullName -Raw
        $name = [regex]::Match($t, '"name"\s+"([^"]+)"').Groups[1].Value
        if ($name -match 'Fighter Maneuvers|^VFM') {
            $appid = [regex]::Match($t, '"appid"\s+"(\d+)"').Groups[1].Value
            $dir = [regex]::Match($t, '"installdir"\s+"([^"]+)"').Groups[1].Value
            $inst = Join-Path $lib "steamapps\common\$dir"
            Z "- Gefunden: **$name**, AppID $appid, Build $([regex]::Match($t, '"buildid"\s+"(\d+)"').Groups[1].Value), Ordner ``$inst``"
        }
    }
}
if (-not $inst) {
    foreach ($lib in $bibliotheken) {
        $k = Get-ChildItem -Path (Join-Path $lib "steamapps\common") -Directory -ErrorAction SilentlyContinue | Where-Object { $_.Name -match 'Fighter|VFM' } | Select-Object -First 1
        if ($k) { $inst = $k.FullName; Z "- Gefunden über Ordnername: ``$inst``" }
    }
}

$datenOrdner = $null; $metaQuelle = $null
if ($inst -and (Test-Path $inst)) {
    $exe = Get-ChildItem $inst -Filter *.exe | Where-Object { $_.Name -notmatch 'UnityCrashHandler|Uninstall' } | Select-Object -First 1
    $datenOrdner = Get-ChildItem $inst -Directory | Where-Object { $_.Name -like '*_Data' } | Select-Object -First 1
    $player = Join-Path $inst "UnityPlayer.dll"
    $unity = if (Test-Path $player) { (Get-Item $player).VersionInfo.FileVersion } else { "?" }
    $managed = if ($datenOrdner) { Join-Path $datenOrdner.FullName "Managed" } else { $null }
    $mono = $managed -and (Test-Path (Join-Path $managed "Assembly-CSharp.dll"))
    $il2cpp = Test-Path (Join-Path $inst "GameAssembly.dll")
    $backend = if ($mono) { "Mono (Assembly-CSharp.dll vorhanden)" } elseif ($il2cpp) { "IL2CPP (GameAssembly.dll)" } else { "unklar" }
    $groesse = (Get-ChildItem $inst -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum

    Z "- Exe: $($exe.Name), Unity $unity, Backend: **$backend**, Installation $(Groesse $groesse)"
    Z ""
    Z "Oberste Ebene:"
    Z ""
    foreach ($e in Get-ChildItem $inst) { Z "    $($e.Name)$(if ($e.PSIsContainer) { '\' } else { '  ' + (Groesse $e.Length) })" }

    if ($mono) {
        $metaQuelle = Join-Path $managed "Assembly-CSharp.dll"
        Z ""
        Z "Managed-Bibliotheken (Serialisierung, Netzwerk, Mods erkennbar an den Namen):"
        Z ""
        Z ("    " + ((Get-ChildItem $managed -Filter *.dll | Where-Object { $_.Name -notmatch '^(System|Unity\.|UnityEngine|mscorlib|netstandard|Mono\.)' } | ForEach-Object { $_.Name }) -join ", "))
        $hinweis = Get-ChildItem $managed -Filter *.dll | Where-Object { $_.Name -match 'Newtonsoft|Json|MessagePack|protobuf|Proto|FlatBuffers|Bson|LZ4|Zstd|SharpZip|Photon|Mirror|Fusion|Netcode|Steamworks|Facepunch|Harmony|BepInEx|ModLoader' }
        if ($hinweis) { Z ""; Z "Auffällig: $(($hinweis | ForEach-Object { $_.Name }) -join ', ')" }
    }
    if ($il2cpp -and $datenOrdner) {
        $gm = Join-Path $datenOrdner.FullName "il2cpp_data\Metadata\global-metadata.dat"
        if (Test-Path $gm) { $metaQuelle = $gm }
    }

    if ($datenOrdner) {
        $sa = Join-Path $datenOrdner.FullName "StreamingAssets"
        Z ""
        if (Test-Path $sa) {
            Z "StreamingAssets (erste 60 Dateien):"
            Z ""
            foreach ($f in Get-ChildItem $sa -Recurse -File | Select-Object -First 60) { Z "    $($f.FullName.Substring($sa.Length)) $(Groesse $f.Length)" }
        } else { Z "Kein StreamingAssets-Ordner." }

        Z ""
        Z "Lesbare Textdateien in der Installation:"
        Z ""
        $text = Get-ChildItem $inst -Recurse -File -Include *.json, *.xml, *.txt, *.ini, *.cfg, *.yaml, *.yml, *.csv, *.lua -ErrorAction SilentlyContinue | Select-Object -First 80
        if ($text) { foreach ($f in $text) { Z "    $($f.FullName.Substring($inst.Length)) $(Groesse $f.Length)" } } else { Z "    keine" }

        Z ""
        Z "Unity-Datendateien nach Größe (Top 15):"
        Z ""
        foreach ($f in Get-ChildItem $datenOrdner.FullName -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $_.Extension -in '.assets', '.resS', '.resource', '.bundle', '' } | Sort-Object Length -Descending | Select-Object -First 15) {
            Z "    $($f.FullName.Substring($datenOrdner.FullName.Length)) $(Groesse $f.Length)"
        }
    }
    $json.installation = [ordered]@{ ordner = $inst; appid = $appid; unity = $unity; backend = $backend }
} else {
    Z "**VFM nicht gefunden.** Steam-Bibliothek von Hand prüfen und den Pfad melden."
}

# ---------------------------------------------------------------- 2. Datenordner
Z ""
Z "## 2. Datenordner"
Z ""

$wurzeln = @(
    (Join-Path $env:USERPROFILE "AppData\LocalLow"),
    $env:APPDATA,
    $env:LOCALAPPDATA,
    [Environment]::GetFolderPath("MyDocuments"),
    (Join-Path $env:USERPROFILE "Saved Games"),
    (Join-Path $env:USERPROFILE "Videos")
) | Where-Object { $_ -and (Test-Path $_) } | Select-Object -Unique

$muster = 'Boundless|Virtual ?Fighter|VFM|Fighter ?Maneuvers'
$treffer = New-Object System.Collections.Generic.List[string]
foreach ($w in $wurzeln) {
    foreach ($d in Get-ChildItem $w -Directory -ErrorAction SilentlyContinue) {
        if ($d.Name -match $muster) { $treffer.Add($d.FullName) }
        else {
            foreach ($d2 in Get-ChildItem $d.FullName -Directory -ErrorAction SilentlyContinue) {
                if ($d2.Name -match $muster) { $treffer.Add($d2.FullName) }
            }
        }
    }
}
if ($steam -and $appid) {
    foreach ($u in Get-ChildItem (Join-Path $steam "userdata") -Directory -ErrorAction SilentlyContinue) {
        $c = Join-Path $u.FullName $appid
        if (Test-Path $c) { $treffer.Add($c) }
    }
}
$treffer = $treffer | Select-Object -Unique
if (-not $treffer) { Z "Keine Ordner mit $muster gefunden. Suchmuster prüfen." }
foreach ($t in $treffer) {
    $f = Get-ChildItem $t -Recurse -File -ErrorAction SilentlyContinue
    $s = ($f | Measure-Object Length -Sum).Sum
    Z "- ``$(Anon $t)``: $($f.Count) Dateien, $(Groesse $s)"
    $json.datenordner += (Anon $t)
}

# ---------------------------------------------------------------- 3. Dateien beschreiben
Z ""
Z "## 3. Dateien"
Z ""
Z "Magic = erkanntes Format aus den ersten Bytes. Entropie (bit/Byte, erste 16 KB): < 5 Text oder Rohdaten mit viel Struktur, 6-7,5 Binär mit Struktur (Floats), > 7,9 komprimiert oder verschlüsselt."
Z ""

$alle = foreach ($t in $treffer) { Get-ChildItem $t -Recurse -File -ErrorAction SilentlyContinue }
$alle = $alle | Sort-Object LastWriteTime -Descending | Select-Object -First $MaxDateien

$gruppen = $alle | Group-Object { if ($_.Extension) { $_.Extension.ToLower() } else { "(ohne)" } } | Sort-Object Count -Descending
Z "Endungen: $(($gruppen | ForEach-Object { "$($_.Name) x$($_.Count) ($(Groesse (($_.Group | Measure-Object Length -Sum).Sum)))" }) -join ', ')"
Z ""

foreach ($f in $alle) {
    $kopf = Lies-Kopf $f.FullName 16384
    $art = Magic $kopf
    $eintrag = [ordered]@{
        pfad = (Anon $f.FullName); groesse = $f.Length; geaendert = $f.LastWriteTime.ToString("s")
        magic = $art; hex = (Hex $kopf 32); ascii = (Ascii $kopf 32); entropie = (Entropie $kopf); druckbar = (Druckbar $kopf); entpackt = $null
    }
    $eintrag.entpackt = Probe-Entpacken $f.FullName $art
    $json.dateien += $eintrag

    Z "### $(Anon $f.FullName)"
    Z ""
    Z "- $(Groesse $f.Length), geändert $($f.LastWriteTime.ToString('yyyy-MM-dd HH:mm:ss')), Magic **$art**, Entropie $($eintrag.entropie), druckbar $($eintrag.druckbar)"
    Z "- Hex: ``$($eintrag.hex)``"
    Z "- ASCII: ``$($eintrag.ascii)``"
    if ($eintrag.entpackt) { Z "- $($eintrag.entpackt)" }
    if ($eintrag.druckbar -gt 0.95 -and $f.Length -lt 200KB -and $f.Name -notmatch 'log') {
        Z "- Anfang:"
        Z '```'
        foreach ($l in (Get-Content $f.FullName -TotalCount 15 -ErrorAction SilentlyContinue)) { Z (Anon $l) }
        Z '```'
    }
    Z ""
}

# Player.log: nur Zeilen zu Replays, Dateien und Speicherorten
$logs = $alle | Where-Object { $_.Name -match '^Player(-prev)?\.log$' }
foreach ($l in $logs) {
    Z "### Auszug aus $(Anon $l.FullName) (nur Zeilen mit replay/record/save/path)"
    Z '```'
    Select-String -Path $l.FullName -Pattern 'replay|record|playback|save|path|file' -ErrorAction SilentlyContinue | Select-Object -First 60 | ForEach-Object { Z (Anon $_.Line) }
    Z '```'
    Z ""
}

# ---------------------------------------------------------------- 4. Bezeichner (optional)
if ($Bezeichner) {
    Z "## 4. Bezeichner im Spielcode (Text-Scan)"
    Z ""
    if ($metaQuelle -and (Test-Path $metaQuelle)) {
        $bytes = [System.IO.File]::ReadAllBytes($metaQuelle)
        $ascii = [System.Text.Encoding]::ASCII.GetString($bytes)
        $utf16 = [System.Text.Encoding]::Unicode.GetString($bytes)
        $id = [regex]::Matches($ascii, '[A-Za-z_][A-Za-z0-9_<>]*(Replay|Record|Playback|Snapshot|Recorder|Ghost|Telemetry|Flight[A-Z]\w*Data)[A-Za-z0-9_<>]*') | ForEach-Object { $_.Value } | Sort-Object -Unique
        $str = [regex]::Matches($utf16, '[\w ./\\{}:%-]*(?i:replay|record|\.rpl|\.rep|telemetry)[\w ./\\{}:%-]*') | ForEach-Object { $_.Value.Trim() } | Where-Object { $_.Length -ge 4 -and $_.Length -le 120 } | Sort-Object -Unique
        Z "Quelle: $(Split-Path $metaQuelle -Leaf), $($id.Count) Bezeichner, $($str.Count) Zeichenketten"
        Z ""
        Z "Bezeichner:"
        Z '```'
        $id | Select-Object -First 400 | ForEach-Object { Z $_ }
        Z '```'
        Z "Zeichenketten (Dateinamen, Endungen, Ordner):"
        Z '```'
        $str | Select-Object -First 200 | ForEach-Object { Z $_ }
        Z '```'
        $json.bezeichner = [ordered]@{ quelle = (Split-Path $metaQuelle -Leaf); bezeichner = @($id); zeichenketten = @($str) }
    } else { Z "Keine Assembly-CSharp.dll oder global-metadata.dat gefunden." }
    Z ""
}

# ---------------------------------------------------------------- 5. Proben (optional)
if ($Proben -gt 0) {
    $probenOrdner = Join-Path $Ausgabe "proben"
    New-Item -ItemType Directory -Force -Path $probenOrdner | Out-Null
    $kandidaten = $alle | Where-Object { $_.Length -gt 10KB -and $_.Name -notmatch '\.(log|png|jpg|txt|json|ini|cfg)$' -and $_.FullName -match '(?i)replay|record' }
    if (-not $kandidaten) { $kandidaten = $alle | Where-Object { $_.Length -gt 10KB -and $_.Name -notmatch '\.(log|png|jpg)$' } }
    Z "## 5. Proben kopiert nach proben\"
    Z ""
    foreach ($k in $kandidaten | Select-Object -First $Proben) {
        Copy-Item $k.FullName -Destination $probenOrdner
        Z "- $($k.Name) ($(Groesse $k.Length))"
    }
    Z ""
}

$md = Join-Path $Ausgabe "bericht.md"
[System.IO.File]::WriteAllLines($md, $bericht, (New-Object System.Text.UTF8Encoding($false)))
[System.IO.File]::WriteAllText((Join-Path $Ausgabe "bericht.json"), ($json | ConvertTo-Json -Depth 6), (New-Object System.Text.UTF8Encoding($false)))
Write-Host ""
Write-Host "Fertig: $md"

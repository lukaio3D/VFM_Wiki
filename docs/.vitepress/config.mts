import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid(
  defineConfig({
    title: "VFM Flight Academy",
    description: "Taktische Doktrin für Virtual Fighter Maneuvers",
    lang: 'de-DE',
    base: '/VFM_Wiki/',

    head: [
      ['meta', { name: 'theme-color', content: '#1a1a2e' }]
    ],

    themeConfig: {
      nav: [
        { text: 'Start', link: '/' },
        { text: 'Einstieg', link: '/einstieg/hardware' },
        { text: 'Grundlagen', link: '/grundlagen/golden-rules' },
        { text: 'Avionik', link: '/avionik/radar' },
        { text: 'Flugzeuge', link: '/flugzeuge/vergleich' },
        { text: 'Training', link: '/grundlagen/uebungen' }
      ],

      sidebar: [
        {
          text: 'Einstieg',
          collapsed: false,
          items: [
            { text: 'Hardware & Plattformen', link: '/einstieg/hardware' },
            { text: 'Steuerung & Einstellungen', link: '/einstieg/cockpit' },
            { text: 'Spielmodi & Ranked', link: '/einstieg/spielmodi' }
          ]
        },
        {
          text: 'Stufe 0 · Regeln & Begriffe',
          collapsed: false,
          items: [
            { text: 'Golden Rules', link: '/grundlagen/golden-rules' },
            { text: 'Begriffe & Brevity', link: '/grundlagen/begriffe' }
          ]
        },
        {
          text: 'Stufe 1 · Flugphysik',
          collapsed: false,
          items: [
            { text: 'Kurvenphysik & Lift Vector', link: '/grundlagen/kurvenphysik' },
            { text: 'Energie & E-M-Diagramm', link: '/grundlagen/energie-management' },
            { text: 'Das VFM-Flugmodell', link: '/grundlagen/physik' }
          ]
        },
        {
          text: 'Stufe 2 · Geometrie',
          collapsed: false,
          items: [
            { text: 'Relative Geometrie', link: '/grundlagen/geometrie' },
            { text: 'Verfolgungskurven', link: '/grundlagen/verfolgungskurven' }
          ]
        },
        {
          text: 'Stufe 3 · Offensiv',
          collapsed: true,
          items: [
            { text: 'Ziele & Entscheidungen', link: '/grundlagen/offensiv-manoever' },
            { text: 'High & Low Yo-Yo', link: '/grundlagen/offensiv/yo-yos' },
            { text: 'Lag Roll & Barrel Roll Attack', link: '/grundlagen/offensiv/lag-roll' },
            { text: 'Overshoot', link: '/grundlagen/offensiv/overshoot' },
            { text: 'Schusslösung', link: '/grundlagen/offensiv/schussloesung' }
          ]
        },
        {
          text: 'Stufe 4 · Defensiv',
          collapsed: true,
          items: [
            { text: 'Prioritäten', link: '/grundlagen/defensiv-manoever' },
            { text: 'Break Turn', link: '/grundlagen/defensiv/break-turn' },
            { text: 'Guns Defense (Jink)', link: '/grundlagen/defensiv/guns-defense' },
            { text: 'Slice (Nose-low Turn)', link: '/grundlagen/defensiv/slice-turn' },
            { text: 'Defensive Spirale', link: '/grundlagen/defensiv/spirale' },
            { text: 'Separation & Bugout', link: '/grundlagen/defensiv/separation' }
          ]
        },
        {
          text: 'Stufe 5 · Neutral',
          collapsed: true,
          items: [
            { text: 'Der Merge', link: '/grundlagen/neutral/der-merge' },
            { text: 'One-Circle vs. Two-Circle', link: '/grundlagen/neutral/one-two-circle' },
            { text: 'Scissors', link: '/grundlagen/neutral/scissors' },
            { text: 'Vertikaler Kampf', link: '/grundlagen/neutral/vertikal-kampf' }
          ]
        },
        {
          text: 'Stufe 6 · Training',
          collapsed: false,
          items: [
            { text: 'Trainingsplan & Übungen', link: '/grundlagen/uebungen' }
          ]
        },
        {
          text: 'Avionik & Waffen',
          collapsed: true,
          items: [
            { text: 'Radar', link: '/avionik/radar' },
            { text: 'Head-Up Display (HUD)', link: '/avionik/hud' },
            { text: 'RWR & Raketenwarner', link: '/avionik/rwr' },
            { text: 'Waffen', link: '/avionik/waffen' },
            { text: 'Flares', link: '/avionik/gegenmassnahmen' }
          ]
        },
        {
          text: 'Flugzeuge',
          collapsed: false,
          items: [
            { text: 'Performance-Daten & Vergleich', link: '/flugzeuge/vergleich' },
            { text: 'T-15 Excalibur', link: '/flugzeuge/t15' },
            { text: 'T-16 Falchion', link: '/flugzeuge/t16' },
            { text: 'T-18 Cutlass', link: '/flugzeuge/t18' },
            {
              text: 'Matchups',
              collapsed: false,
              items: [
                { text: 'T-15 vs. T-16', link: '/flugzeuge/matchups/t15-vs-t16' },
                { text: 'T-15 vs. T-18', link: '/flugzeuge/matchups/t15-vs-t18' },
                { text: 'T-16 vs. T-18', link: '/flugzeuge/matchups/t16-vs-t18' }
              ]
            },
            { text: 'Team-Taktik', link: '/flugzeuge/team' }
          ]
        }
      ],

      socialLinks: [
        { icon: 'github', link: 'https://github.com/lukaio3D/VFM_Wiki' }
      ],

      outline: {
        level: [2, 3],
        label: 'Auf dieser Seite'
      },

      docFooter: {
        prev: 'Vorherige Seite',
        next: 'Nächste Seite'
      },

      search: {
        provider: 'local',
        options: {
          translations: {
            button: {
              buttonText: 'Suchen',
              buttonAriaLabel: 'Suchen'
            },
            modal: {
              noResultsText: 'Keine Ergebnisse für',
              resetButtonTitle: 'Suche zurücksetzen',
              footer: {
                selectText: 'auswählen',
                navigateText: 'navigieren',
                closeText: 'schließen'
              }
            }
          }
        }
      }
    },

    appearance: 'dark',

    mermaid: {
      theme: 'dark'
    }
  })
)

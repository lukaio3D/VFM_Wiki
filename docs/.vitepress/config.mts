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
        { text: 'Grundlagen', link: '/grundlagen/golden-rules' },
        { text: 'Flugzeuge', link: '/flugzeuge/t15-excalibur' },
        { text: 'Taktiken', link: '/taktiken/t15/vs-t16' }
      ],

      sidebar: [
        {
          text: 'Grundlagen',
          collapsed: false,
          items: [
            { text: 'Golden Rules', link: '/grundlagen/golden-rules' },
            { text: 'Begriffe & Definitionen', link: '/grundlagen/begriffe' },
            { text: 'Kampf-Geometrie', link: '/grundlagen/geometrie' },
            { text: 'Der Merge', link: '/grundlagen/der-merge' },
            { text: 'Energie-Management', link: '/grundlagen/energie-management' },
            { text: 'Verfolgungskurven', link: '/grundlagen/verfolgungskurven' },
            {
              text: 'Offensiv-Manöver',
              collapsed: true,
              items: [
                { text: 'Einführung', link: '/grundlagen/offensiv-manoever' },
                { text: 'High Yo-Yo', link: '/grundlagen/offensiv/high-yo-yo' },
                { text: 'Low Yo-Yo', link: '/grundlagen/offensiv/low-yo-yo' },
                { text: 'Lag Displacement Roll', link: '/grundlagen/offensiv/lag-displacement' },
                { text: 'Schusslösung', link: '/grundlagen/offensiv/schussloesung' }
              ]
            },
            {
              text: 'Defensiv-Manöver',
              collapsed: true,
              items: [
                { text: 'Einführung', link: '/grundlagen/defensiv-manoever' },
                { text: 'Break Turn', link: '/grundlagen/defensiv/break-turn' },
                { text: 'Scissors', link: '/grundlagen/defensiv/scissors' },
                { text: 'Slice Turn', link: '/grundlagen/defensiv/slice-turn' },
                { text: 'Defensive Spirale', link: '/grundlagen/defensiv/spirale' },
                { text: 'Jinking & Overshoots', link: '/grundlagen/defensiv/jinking' }
              ]
            },
            {
              text: 'Vertikal-Manöver',
              collapsed: true,
              items: [
                { text: 'Einführung', link: '/grundlagen/vertikal-manoever' },
                { text: 'Taktische Spirale', link: '/grundlagen/vertikal/taktische-spirale' },
                { text: 'Zoom Climb', link: '/grundlagen/vertikal/zoom-climb' },
                { text: 'Speed Regeln', link: '/grundlagen/vertikal/speed-regeln' }
              ]
            }
          ]
        },
        {
          text: 'Virtual Fighter Maneuvers',
          collapsed: false,
          items: [
            { text: 'Übersicht & Vergleich', link: '/flugzeuge/vergleich' },
            {
              text: 'Handbuch: T-15 Excalibur',
              collapsed: true,
              items: [
                { text: '1. Daten & Performance', link: '/flugzeuge/t15/daten' },
                { text: '2. Taktik & Einsatzprofil', link: '/flugzeuge/t15/taktik' },
                { text: '3. Bedrohungs-Analyse', link: '/flugzeuge/t15/matchups' },
                { text: '4. Empfohlene Manöver', link: '/flugzeuge/t15/manoever' },
                { text: '5. Team-Taktiken', link: '/flugzeuge/t15/team' }
              ]
            },
            {
              text: 'Handbuch: T-16 Falchion',
              collapsed: true,
              items: [
                { text: '1. Daten & Performance', link: '/flugzeuge/t16/daten' },
                { text: '2. Taktik & Einsatzprofil', link: '/flugzeuge/t16/taktik' },
                { text: '3. Bedrohungs-Analyse', link: '/flugzeuge/t16/matchups' },
                { text: '4. Empfohlene Manöver', link: '/flugzeuge/t16/manoever' },
                { text: '5. Team-Taktiken', link: '/flugzeuge/t16/team' }
              ]
            },
            {
              text: 'Handbuch: T-18 Cutlass',
              collapsed: true,
              items: [
                { text: '1. Daten & Performance', link: '/flugzeuge/t18/daten' },
                { text: '2. Taktik & Einsatzprofil', link: '/flugzeuge/t18/taktik' },
                { text: '3. Bedrohungs-Analyse', link: '/flugzeuge/t18/matchups' },
                { text: '4. Empfohlene Manöver', link: '/flugzeuge/t18/manoever' },
                { text: '5. Team-Taktiken', link: '/flugzeuge/t18/team' }
              ]
            }
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

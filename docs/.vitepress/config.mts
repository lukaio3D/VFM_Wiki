import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid(
  defineConfig({
    title: "VFM Flight Academy",
    description: "Taktische Doktrin für Virtual Fighter Maneuvers",
    lang: 'de-DE',

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
            { text: 'Kampf-Geometrie', link: '/grundlagen/geometrie' },
            { text: 'Energie-Management', link: '/grundlagen/energie-management' },
            { text: 'Verfolgungskurven', link: '/grundlagen/verfolgungskurven' },
            { text: 'Offensiv-Manöver', link: '/grundlagen/offensiv-manoever' },
            { text: 'Defensiv-Manöver', link: '/grundlagen/defensiv-manoever' },
            { text: 'Vertikal-Manöver', link: '/grundlagen/vertikal-manoever' }
          ]
        },
        {
          text: 'Flugzeug-Daten',
          collapsed: false,
          items: [
            { text: 'T-15 Excalibur', link: '/flugzeuge/t15-excalibur' },
            { text: 'T-16 Falchion', link: '/flugzeuge/t16-falchion' },
            { text: 'T-18 Cutlass', link: '/flugzeuge/t18-cutlass' }
          ]
        },
        {
          text: 'T-15 Taktiken',
          collapsed: false,
          items: [
            { text: 'vs T-16 Falchion', link: '/taktiken/t15/vs-t16' },
            { text: 'vs T-18 Cutlass', link: '/taktiken/t15/vs-t18' },
            { text: 'vs T-15 (Spiegel)', link: '/taktiken/t15/vs-t15' }
          ]
        },
        {
          text: 'T-16 Taktiken',
          collapsed: false,
          items: [
            { text: 'vs T-15 Excalibur', link: '/taktiken/t16/vs-t15' },
            { text: 'vs T-18 Cutlass', link: '/taktiken/t16/vs-t18' },
            { text: 'vs T-16 (Spiegel)', link: '/taktiken/t16/vs-t16' }
          ]
        },
        {
          text: 'T-18 Taktiken',
          collapsed: false,
          items: [
            { text: 'vs T-15 Excalibur', link: '/taktiken/t18/vs-t15' },
            { text: 'vs T-16 Falchion', link: '/taktiken/t18/vs-t16' },
            { text: 'vs T-18 (Spiegel)', link: '/taktiken/t18/vs-t18' }
          ]
        }
      ],

      socialLinks: [
        { icon: 'github', link: 'https://github.com/lukasschaab/VFM_Wiki' }
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

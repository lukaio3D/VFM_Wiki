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
        { text: 'Golden Rules', link: '/golden-rules' },
        { text: 'Flugzeuge', link: '/aircraft/t15-excalibur' },
        { text: 'Theorie', link: '/academy/geometry' },
        { text: 'Taktiken', link: '/playbook/t15-vs-t16' }
      ],

      sidebar: [
        {
          text: 'Grundlagen',
          collapsed: false,
          items: [
            { text: 'Golden Rules', link: '/golden-rules' }
          ]
        },
        {
          text: 'Flugzeug-Daten',
          collapsed: false,
          items: [
            { text: 'T-15 Excalibur', link: '/aircraft/t15-excalibur' },
            { text: 'T-16 Falchion', link: '/aircraft/t16-falchion' },
            { text: 'T-18 Cutlass', link: '/aircraft/t18-cutlass' }
          ]
        },
        {
          text: 'BFM Theorie',
          collapsed: false,
          items: [
            { text: 'Kampf-Geometrie', link: '/academy/geometry' },
            { text: 'Energie-Management', link: '/academy/energy-management' },
            { text: 'Verfolgungskurven', link: '/academy/pursuit-curves' }
          ]
        },
        {
          text: 'Manöver',
          collapsed: false,
          items: [
            { text: 'Offensiv', link: '/maneuvers/offensive' },
            { text: 'Defensiv', link: '/maneuvers/defensive' },
            { text: 'Vertikal', link: '/maneuvers/vertical' }
          ]
        },
        {
          text: 'Taktiken',
          collapsed: false,
          items: [
            { text: 'T-15 vs T-16', link: '/playbook/t15-vs-t16' },
            { text: 'T-15 vs T-18', link: '/playbook/t15-vs-t18' },
            { text: 'T-15 vs T-15', link: '/playbook/t15-vs-t15' }
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

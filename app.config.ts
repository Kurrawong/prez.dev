export default defineAppConfig<DefaultConfig>({
  shadcnDocs: {
    site: {
      name: 'Prez',
      description: 'A highly customisable stack of tools for organising, accessing and presenting Linked Data',
    },
    theme: {
      customizable: false,
      color: 'orange',
      radius: 0.5,
    },
    header: {
      title: 'Prez',
      showTitle: true,
      darkModeToggle: true,
      languageSwitcher: {
        enable: false,
        triggerType: 'icon',
        dropdownType: 'select',
      },
      logo: {
        light: '/prez-logo.png',
        dark: '/prez-logo.png',
      },
      nav: [
        {
          title: "Docs",
          to: "/getting-started",
          showLinkIcon: false,
        },
        {
          title: "Examples",
          to: "/examples",
          showLinkIcon: false,
        },
        {
          title: "Demo",
          to: "https://demo.prez.dev",
          target: "_blank",
        }
      ],
      links: [{
        icon: 'lucide:github',
        to: 'https://github.com/RDFLib/prez-ui',
        target: '_blank',
      }],
    },
    aside: {
      useLevel: true,
      collapse: false,
      // levelStyle: "header",
    },
    main: {
      breadCrumb: true,
      showTitle: true,
    },
    footer: {
      credits: 'Copyright © 2026',
      links: [{
        icon: 'lucide:github',
        to: 'https://github.com/RDFLib/prez-ui',
        target: '_blank',
      }],
    },
    toc: {
      enable: true,
      links: [{
        title: 'Star on GitHub',
        icon: 'lucide:star',
        to: 'https://github.com/RDFLib/prez-ui',
        target: '_blank',
      }, {
        title: 'Create Issues',
        icon: 'lucide:circle-dot',
        to: 'https://github.com/RDFLib/prez-ui/issues',
        target: '_blank',
      }],
    },
    search: {
      enable: true,
      inAside: false,
    }
  }
});
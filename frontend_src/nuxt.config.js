export default () => {
  const publicRuntimeConfig = {
    PRODUCTION: process.env.PRODUCTION || 'true',
    BASE_URL: process.env.BASE_URL || 'http://web:8000/api',
    BROWSER_BASE_URL: process.env.BROWSER_BASE_URL || 'http://localhost/api',
    BUILD_DIR: process.env.BUILD_DIR || 'hui',
    AVAILABLE_LOCALES: process.env.AVAILABLE_LOCALES || 'fr,en,es',
    DEFAULT_LOCALE: process.env.DEFAULT_LOCALE || 'ru'
  }
  const privateRuntimeConfig = {}

  return {
    publicRuntimeConfig,
    privateRuntimeConfig,

    ...process.env.PRODUCTION == 'true' && { server: { host: '0.0.0.0'} },

    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
      title: 'scherbakov',
      htmlAttrs: {
        lang: 'ru'
      },
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { hid: 'description', name: 'description', content: '' },
        { name: 'format-detection', content: 'telephone=no' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ]
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [
    ],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [
    ],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: true,

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [
      // https://go.nuxtjs.dev/typescript
      '@nuxt/typescript-build',
      // https://go.nuxtjs.dev/tailwindcss
      '@nuxtjs/tailwindcss'
    ],

    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
      // https://go.nuxtjs.dev/axios
      '@nuxtjs/axios',
      '@nuxtjs/i18n'
    ],

    i18n: {
      locales:
        process.env.AVAILABLE_LOCALES.split(',').map((l) => {
        return { code: l, file: `${l}.js` }
      }),
      defaultLocale: process.env.DEFAULT_LOCALE,
      langDir: 'i18n/',
      detectBrowserLanguage: {
        useCookie: true,
        cookieKey: 'i18n_redirected'
      },
      vueI18n: {
        fallbackLocale: process.env.DEFAULT_LOCALE
      }
    },

    // Axios module configuration: https://go.nuxtjs.dev/config-axios
    axios: {
      // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
      baseURL: process.env.BASE_URL,
      browserBaseURL: process.env.BROWSER_BASE_URL
    },

    tailwindcss: {
      cssPath: '~/assets/css/tailwind.css'
    },

    buildDir: process.env.BUILD_DIR,

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {
      extend(config) {
        config.module.rules.push({
          test: /\.ya?ml$/,
          use: 'js-yaml-loader'
        })
      },
      postcss: {
        // Add plugin names as key and arguments as value
        // Install them before as dependencies with npm or yarn
        plugins: {
          // Disable a plugin by passing false as value
          'tailwindcss/nesting': {},
          'postcss-nested': {
            bubble: ['screen']
          },
          'postcss-hexrgba': {},
          tailwindcss: {}
        }
      }
    }
  }
}

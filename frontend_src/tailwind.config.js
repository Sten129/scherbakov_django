module.exports = {
  mode: 'jit',
  future: {
    // removeDeprecatedGapUtilities: true,
    // purgeLayersByDefault: true,
  },
  purge: {
    content: [
      './assets/css/**/*.css',
      './components/**/*.vue',
      './pages/**/*.vue',
      './layout/**/*.vue',
      './store/**/*.js'
    ]
  },
  corePlugins: {
    container: false,
    outline: false,
    ringWidth: false
  },
  theme: {
    screens: {
      'xs': '480px',
      // => @media (min-width: 480px) { ... }

      'sm': '640px',
      // => @media (min-width: 640px) { ... }

      'md': '768px',
      // => @media (min-width: 768px) { ... }

      'lg': '1024px',
      // => @media (min-width: 1024px) { ... }

      'navbar': '1024px',
      // => @media (min-width: 1024px) { ... }

      'xl': '1280px',
      // => @media (min-width: 1280px) { ... }

      '2xl': '1440px',
      // => @media (min-width: 1440px) { ... }

      'max': '1920px'
      // => @media (min-width: 1920px) { ... }
    },
    fontFamily: {
      sans: ['Inter', 'sans-serif'],
      serif: ['Playfair Display', 'serif']
    },
    extend: {
      borderWidth: {
        '5': '5px'
      },
      spacing: {
        '10px': '10px',
        '60px': '60px',
        '100px': '100px',
        '120px': '120px'
      },
      maxWidth: {
        '3/4': '75%',
        '2/3': '66.66%'
      },
      minHeight: {
        '10': '40px'
      },
      lineHeight: {
        'leading-normal': '1.625',
        'leading-34px': '34px'
      },
      fontSize: {
        's13': ['.813rem', '1.538'], // 13px
        's15': ['.938rem', '1.667'], // 15px
        's30': ['1.875rem', '1.333'], // 30px
        's36': ['2.25rem', '1.333'], // 36px
        's40': ['2.5rem', '1.25'], // 40px
        's60': ['3.75rem', '1'] // 60px
      },
      colors: {
        primary: '#5e2750',
        secondary: '#8c9aaa', // gray-mediumblue
        gray: {
          dark: '#262626',
          superlight: '#f7f7f7',
          light: '#d1d7dd',
          medium: '#6f6f6e',
          charcoal: '#4d4f53',
          darkblue: '#3a566d',
          mediumblue: '#8c9aaa'
        },
        gunmetal: '#5b6f69',
        sapphire: '#244fb5',
        lightplum: '#97587d',
        orange: '#e94e1b',
        lipstick: '#be2750',
        ocean: '#00718f',
        brown: '#7a615a'
      },
      zIndex: {
        'topbar': 110,
        'menu': 100,
        'backdrop': 90
      }
    }
  },
  variants: {
  },
  plugins: [
  ]
}

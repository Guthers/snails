const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  purge: [
  "./src/**/*.jsx",
  "./src/**/*.tsx",
  "./public/**/*.html"
  ],
  theme: {
    extend: {
      colors: {
        'snail-gray': '#191919',
        'snail-gray-800': '#212121',
      }, 
      gridTemplateColumns: {
        '3-1': 'auto 25%',
        '1-3': '25% auto',
        '2-3': '40% auto',
        '3-2': 'auto 40%',
      },
      gridTemplateRows: {
        '3-1': 'auto 25%',
        '1-3': '25% auto',
        '2-3': '40% auto',
        '3-2': 'auto 40%',
      },
    },
  },
  variants: {},
  plugins: [],
}

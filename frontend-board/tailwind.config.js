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
      }, 
    },
  },
  variants: {},
  plugins: [],
}

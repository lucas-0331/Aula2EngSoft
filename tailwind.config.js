/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./templates/*.html",
  ],
  theme: {
    extend: {
      colors: {
        'browniest': '#5c2217',
        'browniest-light': '#6C382E',
        'browniest-dark': '#491b12',
      },
    },
  },
  plugins: [
    require('tailwindcss'),
    require('postcss-import'),
    require('autoprefixer'),
  ],
}

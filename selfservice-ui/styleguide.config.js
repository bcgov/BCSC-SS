var path = require('path');
module.exports = {
  // set your styleguidist configuration here
  title: 'BC Style Guide',
  // components: 'src/components/**/[A-Z]*.vue',
  defaultExample: true,
  copyCodeButton: true,
  usageMode: 'expand',
  sections: [
    {
      name: 'Atomic Components Section',
      components: 'src/Atomic/**/[A-Z]*.vue'
    },
    {
      name: 'Components Section',
      components: 'src/components/**/[A-Z]*.vue',
      ignore: ['src/components/Header/Header.vue']
    }
  ],
  // webpackConfig: {
  //   // custom config goes here
  // },
  styleguideDir: 'styleguide',
  exampleMode: 'expand',
  require: [path.join(__dirname, 'styleguide-config/global.requires.js')],
  renderRootJsx: path.join(__dirname, 'styleguide-config/styleguide.root.js')
};

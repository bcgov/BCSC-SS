module.exports = {
  transpileDependencies: ['vuetify'],

  pluginOptions: {
    i18n: {
      locale: 'en',
      fallbackLocale: 'en',
      localeDir: 'locales',
      enableInSFC: true
    }
  },
  configureWebpack: {
    module: {
      rules: [
        {
          test: /\.(html)$/,
          use: {
            loader: 'html-loader',
            options: {
              attributes: {
                list: [
                  {
                    // only for img tags
                    tag: 'img',
                    // Attribute name
                    attribute: 'src',
                    // Type of processing, can be `src` or `scrset`
                    type: 'src',
                    // Allow to filter some attributes (optional)
                  },
                ],
              },

            }
          }
        }
      ]
    }
  }
};

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
            loader: 'vue2-html-loader',
            options: {
              removeComments: true,
              removeWhiteSpace: true,
              removeNewline: true
            }
          }
        }
      ]
    }
  }
};

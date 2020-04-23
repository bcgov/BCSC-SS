import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: 'mdi',
  },
  theme: {
    themes: {
      light: {
        error: '#D8292F',
        success: '#2E8540',
        warning: '#FFC107',
      },
    },
    options: {
      cspNonce: 'cLv1G2y8KtMdR',
    },
  },
});

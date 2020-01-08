import VueI18n from 'vue-i18n';
import Vuetify from 'vuetify';
import { loadLocaleMessages } from './../src/i18n';

const i18n = new VueI18n({
  locale: 'en',
  messages: loadLocaleMessages()
});

export default previewComponent => {
  // https://vuejs.org/v2/guide/render-function.html
  return {
    vuetify: new Vuetify(),
    i18n,
    render(createElement) {
      return createElement(
        'v-app',
        {
          props: {
            id: 'v-app'
          }
        },
        [createElement(Object.assign(previewComponent))]
      );
    }
  };
};

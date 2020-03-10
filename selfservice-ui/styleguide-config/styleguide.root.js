import Vue from 'vue';
import VueI18n from 'vue-i18n';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
import { loadLocaleMessages } from './../src/i18n';
import store from '@/store';
import VueRouter from 'vue-router';

const i18n = new VueI18n({
  locale: 'en',
  messages: loadLocaleMessages()
});
Vue.use(Vuex);
const router = new VueRouter();
Vue.use(router);
Vue.component('RouterLink', {
  props: {
    tag: { type: String, default: 'a' },
    to: { type: String, default: 'href' }
  },
  render(createElement) {
    return createElement(this.tag, {}, this.$slots.default);
  }
});

export default previewComponent => {
  // https://vuejs.org/v2/guide/render-function.html
  return {
    vuetify: new Vuetify(),
    store,
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

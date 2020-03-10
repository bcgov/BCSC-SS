import '@mdi/font/css/materialdesignicons.css';
import 'animate.css';
import 'vuetify/dist/vuetify.min.css';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';
import '@/assets/styles/_mixins.scss';
import '@/assets/styles/base.scss';
import '@/assets/styles/layout.scss';
import '@/assets/styles/overrides.scss';
import i18n from './i18n';
import VueClipboard from 'vue-clipboard2';

Vue.config.productionTip = false;
Vue.use(VueClipboard);

new Vue({
  router,
  store,
  vuetify,
  i18n,
  render: h => h(App)
}).$mount('#app');

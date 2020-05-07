import Vue from 'vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';

Vue.use(Vuetify);
Vue.use(Vuex);

(global as any).IntersectionObserver = class IntersectionObserver {
  constructor() {} // tslint:disable-line

  private observe() {
    return null;
  }

  private disconnect() {
    return null;
  }

  private unobserve() {
    return null;
  }
};

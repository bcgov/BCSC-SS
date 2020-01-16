import Vue from 'vue';
import Vuex, { StoreOptions } from 'vuex';
import { RootState } from './types';
import KeyCloakModule from './modules/KeyCloak';
import ProjectInfoModule from './modules/ProjectInfo';
Vue.use(Vuex);

/**
 * Main store with modules
 */
const store: StoreOptions<RootState> = {
  modules: { KeyCloakModule, ProjectInfoModule },
  strict: true
};

export default new Vuex.Store<RootState>(store);

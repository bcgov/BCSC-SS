import Vue from 'vue';
import Vuex, { StoreOptions } from 'vuex';
import { RootState } from './types';
import KeyCloakModule from './modules/KeyCloak';
import ProjectInfoModule from './modules/ProjectInfo';
import TechnicalReqModule from './modules/TechnicalReq';

import PackageAndTestModule from './modules/PackageAndTest';
Vue.use(Vuex);

/**
 * Main store with modules
 */
const store: StoreOptions<RootState> = {
  modules: {
    KeyCloakModule,
    ProjectInfoModule,
    TechnicalReqModule,
    PackageAndTestModule
  },
  strict: true
};

export default new Vuex.Store<RootState>(store);

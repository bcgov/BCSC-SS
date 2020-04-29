import Vue from 'vue';
import Vuex, { StoreOptions } from 'vuex';
import { RootState } from './types';
import KeyCloakModule from './modules/KeyCloak';
import ProjectInfoModule from './modules/ProjectInfo';
import TechnicalReqModule from './modules/TechnicalReq';

import PackageAndTestModule from './modules/PackageAndTest';
import ClientIdModule from './modules/ClientID';
import SharedModule from './modules/Shared';
import TestAccountModule from './modules/TestAccount';
import TeamRolesModule from './modules/TeamRoles';
import ContactUsModule from './modules/ContactUs';

Vue.use(Vuex);

/**
 * Main store with modules
 */
const store: StoreOptions<RootState> = {
  modules: {
    KeyCloakModule,
    ProjectInfoModule,
    TechnicalReqModule,
    PackageAndTestModule,
    ClientIdModule,
    SharedModule,
    TestAccountModule,
    TeamRolesModule,
    ContactUsModule,
  },
  strict: true,
};

export default new Vuex.Store<RootState>(store);

import { ActionTree } from 'vuex';
import { PackageState } from './types';
import { RootState } from '../../types';
// import i18n from '../../../i18n';

import { PackageAndTest } from '@/services/PackageAndTest';
import router from '@/router';

/**
 * package Actions
 *
 */
export const actions: ActionTree<PackageState, RootState> = {
  /**
   * load package from server and set to store
   * @param {*} { commit }
   */
  async loadPackage({ commit }) {
    commit('SET_LOADING', true);
    const packageData = await PackageAndTest.getPackages();
    commit('SET_PACKAGELIST', packageData.data.scopePackages);
    commit('SET_LOADING', false);
  },

  /**
   * load package from server and set to store
   * @param {*} { commit }
   */

  async addPackagetoProject({ commit, rootState }, data) {
    commit('SET_LOADING', true);
    const { projectId, slectedPackage } = data;
    await PackageAndTest.updatePackageProject(projectId, slectedPackage);
    // commit('SET_PACKAGELIST', packageData.data.scopePackage);
    router.push(`/project/${projectId}/test-account/`);
    commit('SET_LOADING', false);
  },

  /**
   * load package from server and set to store
   * @param {*} { commit }
   */

  async addTestAccountRequestToProject({ commit, rootState }, data) {
    commit('SET_LOADING', true);
    const { projectId, noOfTestAccount, noteTestAccount } = data;
    // const packageData =
    await PackageAndTest.updateTestRequestProject(
      projectId,
      noOfTestAccount,
      noteTestAccount
    );
    // router.push('/project/test-account/' + projectId);
    commit('SET_LOADING', false);
  }
};

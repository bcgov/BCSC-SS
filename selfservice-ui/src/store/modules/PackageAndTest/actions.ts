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

  async addPackagetoProject({ commit, dispatch }, data) {
    commit('SET_LOADING', true);
    const { projectId, slectedPackage } = data;
    await PackageAndTest.updatePackageProject(projectId, slectedPackage);
    // commit('SET_PACKAGELIST', packageData.data.scopePackage);
    dispatch('redirect', { projectId, nextPageTogo: 'test-account' });
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
    router.push(`/project-container/${projectId}`);
    commit('SET_LOADING', false);
  },
  redirect(state, { projectId, nextPageTogo }) {
    const isredirectFromSummaryPage =
      state.rootState.SharedModule.isSummaryPage;
    const nextPage = isRedirectFromSummaryPage
      ? `/project-container/${projectId}/`
      : `/project/${projectId}/${nextPageTogo}/`;

    router.push(nextPage);
  },
};

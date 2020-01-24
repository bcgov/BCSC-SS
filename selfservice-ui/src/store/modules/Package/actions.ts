import { ActionTree } from 'vuex';
import { PackageState } from './types';
import { RootState } from '../../types';
// import i18n from '../../../i18n';

import { PackageService } from '@/services/PackageService';

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
    const packageData = await PackageService.getPackages();
    commit('SET_PACKAGELIST', packageData.data.scopePackages);
    commit('SET_LOADING', false);
  },

  /**
   * load package from server and set to store
   * @param {*} { commit }
   */

  async addPackagetoProject({ commit }, data) {
    commit('SET_LOADING', true);
    const { projectId, slectedPackage } = data;
    // const packageData =
    await PackageService.updatePackageProject(projectId, slectedPackage);
    // commit('SET_PACKAGELIST', packageData.data.scopePackage);
    commit('SET_LOADING', false);
  }
};

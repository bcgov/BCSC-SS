import { GetterTree } from 'vuex';
import { PackageState } from './types';
import { RootState } from '../../types';

/**
 * Getters Package
 */
export const getters: GetterTree<PackageState, RootState> = {
  /**
   * package
   * @param {*} state
   * @returns  {object} package
   */

  getPackageList(state) {
    return state.packageList;
  },
  successStatus(state) {
    return state.successStatus;
  },
  errorStatus(state) {
    return state.errorStatus;
  }
};

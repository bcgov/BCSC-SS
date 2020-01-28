import { MutationTree } from 'vuex';
import { PackageState } from './types';

/**
 * mutation
 */
export const mutations: MutationTree<PackageState> = {
  /**
   * Sets loading
   * @param {*} state
   * @param {boolean} flag - loading
   */

  SET_LOADING(state, flag: boolean) {
    state.loading = flag;
  },
  /**
   * Sets package
   * @param {*} state
   * @param payload package list
   */

  SET_PACKAGELIST(state, payload: any) {
    state.packageList = payload;
  },

  /**
   * set stae on success
   * @param {*} state
   * @param {*} payload
   */
  SET_PACKAGE_SUCCESSFULLY(state, payload: any) {
    state.successStatus = payload;
  },

  /**
   * set stae on error
   * @param {*} state
   * @param {*} payload
   */
  SET_PACKAGE_ERROR(state, payload: any) {
    state.errorStatus = payload;
  },

  /**
   * Sets message package
   * @param {*} state
   * @param payload package   data
   */

  SET_PACKAGE_MESSAGE(state, payload: string) {
    state.message = payload;
  }
};

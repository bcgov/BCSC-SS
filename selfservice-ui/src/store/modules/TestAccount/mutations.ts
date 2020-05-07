import { MutationTree } from 'vuex';
import { TestAccountState } from './types';

/**
 * mutation
 */
export const mutations: MutationTree<TestAccountState> = {
  /**
   * Sets loadinf
   * @param {*} state
   * @param {boolean} flag
   */

  SET_LOADING(state, flag: boolean) {
    state.isLoading = flag;
  },
  /**
   * set stae on success
   * @param {*} state
   * @param {*} payload
   */
  SET_SUCESS(state, payload: any) {
    state.successStatus = payload;
  },

  /**
   * set stae on error
   * @param {*} state
   * @param {*} payload
   */
  SET_ERROR(state, payload: any) {
    state.errorStatus = payload;
  }
};

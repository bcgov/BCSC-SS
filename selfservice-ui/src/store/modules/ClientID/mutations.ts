import { MutationTree } from 'vuex';
import { ClientIdState } from './types';

/**
 * mutation
 */
export const mutations: MutationTree<ClientIdState> = {
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

  SET_APIDETAILS(state, payload: any) {
    state.apiData = payload;
  }
};

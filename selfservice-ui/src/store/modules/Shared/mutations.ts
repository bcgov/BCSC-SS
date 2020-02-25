import { MutationTree } from 'vuex';
import { SharedState } from './types';

/**
 * mutation
 */
export const mutations: MutationTree<SharedState> = {
  /**
   * Sets loading
   * @param {*} state
   * @param {boolean} flag - loading
   */

  SET_REDIRECT_FROM(state, flag: boolean) {
    state.isSummaryPage = flag;
  }
};

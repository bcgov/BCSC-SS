import { MutationTree } from 'vuex';
import { SharedState } from './types';

/**
 * mutation
 */
export const mutations: MutationTree<SharedState> = {
  /**
   * Sets redirect from summary page or not
   * @param {*} state
   * @param {boolean} flag
   */

  SET_REDIRECT_FROM(state, flag: boolean) {
    state.isSummaryPage = flag;
  }
};

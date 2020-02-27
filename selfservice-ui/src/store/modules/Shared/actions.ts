import { ActionTree } from 'vuex';
import { SharedState } from './types';
import { RootState } from '../../types';

/**
 * shared Actions
 *
 */
export const actions: ActionTree<SharedState, RootState> = {
  /**
   * @param  {} {commit}
   * @param  {} flag redirectfromsummary page
   */
  async redirectFromSummaryPage({ commit }, flag: boolean) {
    commit('SET_REDIRECT_FROM', flag);
  }
};

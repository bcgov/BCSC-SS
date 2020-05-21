import { ActionTree } from 'vuex';
import { SharedState } from './types';
import { RootState } from '../../types';
import router from '@/router';

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
  },
  /**
   * @param  {} {commit}
   * @param  {} flag redirect to unauthorized page page
   */
  async unAuthorized({ commit }, flag: boolean) {
    router.push('/unauthorized');
  },
};

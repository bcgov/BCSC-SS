import { ActionTree } from 'vuex';
import { TestAccountState } from './types';
import { RootState } from '../../types';
import { TestAccounts } from '@/services/TestAccounts';

/**
 * shared Actions
 *
 */
export const actions: ActionTree<TestAccountState, RootState> = {
  /**
   * @param  {} {commit}
   * @param  {} flag redirectfromsummary page
   */
  async addTestAccounts({ commit, dispatch }, data: any) {
    commit('SET_LOADING', true);
    dispatch('clearStatus');
    try {
      const { testAccounts } = data;
      await TestAccounts.addTestAccounts({ testAccounts });
      commit('SET_SUCESS', true);
      commit('SET_ERROR', false);
      commit('SET_LOADING', false);
    } catch {
      commit('SET_ERROR', true);
      commit('SET_SUCESS', false);
      commit('SET_LOADING', false);
    }
  },
  /**
   * clear message
   * @param {*} { commit }
   */
  async clearStatus({ commit }) {
    commit('SET_SUCESS', false);
    commit('SET_ERROR', false);
    commit('SET_LOADING', false);
  }
};

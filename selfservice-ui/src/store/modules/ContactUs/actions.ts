import { ActionTree } from 'vuex';
import { TestAccountState } from './types';
import { RootState } from '../../types';
import { ContactUs } from '@/services/ContactUs';

/**
 * contact us Actions
 *
 */
export const actions: ActionTree<TestAccountState, RootState> = {
  /**
   * @param  {} {commit}
   * @param  {} data contact us data
   */
  async addContactUs({ commit, dispatch }, data: any) {
    commit('SET_LOADING', true);
    dispatch('clearStatus');

    try {
      const { contactDetails } = data;
      await ContactUs.addContactUs({ ...contactDetails });
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
  },
};

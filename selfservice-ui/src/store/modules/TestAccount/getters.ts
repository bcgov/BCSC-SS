import { GetterTree } from 'vuex';
import { TestAccountState } from './types';
import { RootState } from '../../types';

/**
 * Getters Shared
 */
export const getters: GetterTree<TestAccountState, RootState> = {
  /**
   * isLoading  status
   * @param {*} state
   * @returns {boolean} - loading status
   */
  isLoading(state) {
    return state.isLoading;
  },
  successStatus(state) {
    return state.successStatus;
  },
  errorStatus(state) {
    return state.errorStatus;
  }
};
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
  getChangeStatus(state) {
    return {
      successStatus: state.successStatus,
      errorStatus: state.errorStatus,
    };
  },
};

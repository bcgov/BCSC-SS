import { GetterTree } from 'vuex';
import { SharedState } from './types';
import { RootState } from '../../types';

/**
 * Getters Shared
 */
export const getters: GetterTree<SharedState, RootState> = {
  /**
   * projectinfo
   * @param {*} state
   * @returns  {boolean} summary page redirect
   */

  isRedirectFromSummaryPage(state) {
    return state.isSummaryPage;
  }
};

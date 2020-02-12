import { GetterTree } from 'vuex';
import { ClientIdState } from './types';
import { RootState } from '../../types';

/**
 * Getters Package
 */
export const getters: GetterTree<ClientIdState, RootState> = {
  /**
   * getApiData
   * @param {*} state
   * @returns  {object} package
   */

  getApiData(state) {
    return state.apiData;
  },
  successStatus(state) {
    return state.successStatus;
  },
  errorStatus(state) {
    return state.errorStatus;
  }
};

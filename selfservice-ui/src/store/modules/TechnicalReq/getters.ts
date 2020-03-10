import { GetterTree } from 'vuex';
import { TechnicalReqState } from './types';
import { RootState } from '../../types';

/**
 * Getters TechnicalReq
 */
export const getters: GetterTree<TechnicalReqState, RootState> = {
  /**
   * isLoading
   * @param {*} state
   * @returns {boolean} - lading status
   */
  isLoading(state) {
    return state.loading;
  },
  /**
   * technicalreq
   * @param {*} state
   * @returns  {object} technicalreq
   */

  successStatus(state) {
    return state.successStatus;
  },
  errorStatus(state) {
    return state.errorStatus;
  },
  /**
   * getTechnicalReq
   * @param {*} state
   * @returns  {object} technicalreq
   */
  getTechnicalReq(state) {
    return state.singleTechnicalReq;
  },
  /**
   * getTechnicalReqMessage
   * @param {*} state
   * @returns  {object}  technicalreq
   */
  getTechnicalReqMessage(state) {
    return state.message;
  }
};

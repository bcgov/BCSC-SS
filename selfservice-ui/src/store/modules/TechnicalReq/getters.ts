import { GetterTree } from 'vuex';
import { TechnicalReqState } from './types';
import { RootState } from '../../types';

/**
 * Getters TechnicalReq
 */
export const getters: GetterTree<TechnicalReqState, RootState> = {
  /**
   * technicalreq
   * @param {*} state
   * @returns  {object} technicalreq
   */

  getTechnicalReqList(state) {
    return state.technicalreqList;
  },
  successStatus(state) {
    return state.successStatus;
  },
  errorStatus(state) {
    return state.errorStatus;
  },
  /**
   * getSingleTechnicalReq
   * @param {*} state
   * @returns  {object} technicalreq
   */
  getSingleTechnicalReq(state) {
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

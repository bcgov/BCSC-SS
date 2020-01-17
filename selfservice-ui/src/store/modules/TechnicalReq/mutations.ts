import { MutationTree } from 'vuex';
import { TechnicalReqState } from './types';

/**
 * mutation
 */
export const mutations: MutationTree<TechnicalReqState> = {
  /**
   * Sets loading
   * @param {*} state
   * @param {boolean} flag - loading
   */

  SET_LOADING(state, flag: boolean) {
    state.loading = flag;
  },

  /**
   * set stae on success
   * @param {*} state
   * @param {*} payload
   */
  SET_TECHNICALREQ_SUCCESSFULLY(state, payload: any) {
    state.successStatus = payload;
  },

  /**
   * set stae on error
   * @param {*} state
   * @param {*} payload
   */
  SET_TECHNICALREQ_ERROR(state, payload: any) {
    state.errorStatus = payload;
  },
  /**
   * Sets single technicalreq
   * @param {*} state
   * @param payload technicalreq  data
   */

  SET_EDIT_TECHNICALREQ(state, payload: any) {
    state.singleTechnicalReq = payload;
  },
  /**
   * Sets message technicalreq
   * @param {*} state
   * @param payload technicalreq   data
   */

  SET_TECHNICALREQ_MESSAGE(state, payload: string) {
    state.message = payload;
  }
};

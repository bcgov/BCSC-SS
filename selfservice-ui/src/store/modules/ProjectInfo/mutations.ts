import { MutationTree } from 'vuex';
import { ProjectInfoState } from './types';

/**
 * mutation
 */
export const mutations: MutationTree<ProjectInfoState> = {
  /**
   * Sets loading
   * @param {*} state
   * @param {boolean} flag - loading
   */

  SET_LOADING(state, flag: boolean) {
    state.loading = flag;
  },
  /**
   * Sets projectinfo
   * @param {*} state
   * @param payload projectinfo list
   */

  SET_PROJECTINFOLIST(state, payload: any) {
    state.projectinfoList = payload;
  },

  /**
   * set stae on success
   * @param {*} state
   * @param {*} payload
   */
  SET_PROJECTINFO_SUCCESSFULLY(state, payload: any) {
    state.successStatus = payload;
  },

  /**
   * set stae on error
   * @param {*} state
   * @param {*} payload
   */
  SET_PROJECTINFO_ERROR(state, payload: any) {
    state.errorStatus = payload;
  },
  /**
   * Sets single projectinfo
   * @param {*} state
   * @param payload projectinfo  data
   */

  SET_EDIT_PROJECTINFO(state, payload: any) {
    state.singleProjectInfo = payload;
  },
  /**
   * Sets message projectinfo
   * @param {*} state
   * @param payload projectinfo   data
   */

  SET_PROJECTINFO_MESSAGE(state, payload: string) {
    state.message = payload;
  },
  /**
   * set stae on success of final submit
   * @param {*} state
   * @param {*} payload
   */
  SET_PROJECT_SUBMIT_SUCESS(state, payload: any) {
    state.finalSuccessStatus = payload;
  },

  /**
   * set stae on error of final submit
   * @param {*} state
   * @param {*} payload
   */
  SET_PROJECT_SUBMIT_ERROR(state, payload: any) {
    state.finalErrorStatus = payload;
  },

  /**
   * set state on test account mapping status after submit
   * @param {*} state
   * @param {*} payload
   */
  SET_TEST_ACCOUNT_SUCCESS(state, payload: any) {
    state.testAccountSuccess = payload;
  }
};

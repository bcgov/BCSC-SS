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
  },
  /**
   * set stae on error change
   * @param {*} state
   * @param {*} payload
   */
  SET_STATUS_CHANGE_ERROR(state, payload: any) {
    state.statusChangeError = payload;
  },
  /**
   * set stae on success of status change
   * @param {*} state
   * @param {*} payload
   */
  SET_STATUS_CHANGE_SUCESS(state, payload: any) {
    state.statusChangeSuccess = payload;
  },
  /**
   * set stae on error change
   * @param {*} state
   * @param {*} payload
   */
  SET_DELETE_ERROR(state, payload: any) {
    state.deleteProjectError = payload;
  },
  /**
   * set stae on success of status change
   * @param {*} state
   * @param {*} payload
   */
  SET_DELETE_SUCESS(state, payload: any) {
    state.deleteProjectSuccess = payload;
  },
  /**
   * set is created
   * @param {*} state
   * @param {*} payload
   */
  SET_IS_CREATED(state, payload: any) {
    state.isCreated = payload;
  },
  /**
   * set is updated
   * @param {*} state
   * @param {*} payload
   */
  SET_IS_UPDATED(state, payload: any) {
    state.isUpdated = payload;
  },
  /**
   * set is updated
   * @param {*} state
   * @param {*} payload
   */
  SET_PROJECTHISTORY(state, payload: any) {
    state.history = payload;
  },
};

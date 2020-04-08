import { GetterTree } from 'vuex';
import { TeamRoleState } from './types';
import { RootState } from '../../types';

/**
 * Getters Shared
 */
export const getters: GetterTree<TeamRoleState, RootState> = {
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
  },
  getTeamList(state) {
    return state.teamRoles;
  },
  memberErrorStatus(state) {
    return state.memberAddedError;
  },
  getMemberErrorList(state) {
    return state.memberAddedErrorList;
  },
  getMemberDetails(state) {
    return state.memberDetails;
  }
};

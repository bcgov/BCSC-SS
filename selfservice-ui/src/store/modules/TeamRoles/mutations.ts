import { MutationTree } from 'vuex';
import { TeamRoleState } from './types';

/**
 * mutation
 */
export const mutations: MutationTree<TeamRoleState> = {
  /**
   * Sets loadinf
   * @param {*} state
   * @param {boolean} flag
   */

  SET_LOADING(state, flag: boolean) {
    state.isLoading = flag;
  },
  /**
   * set stae on success
   * @param {*} state
   * @param {*} payload
   */
  SET_ROLESLIST(state, payload: any) {
    state.teamRoles = payload;
  },

  /**
   * set stae on error
   * @param {*} state
   * @param {*} payload
   */
  SET_ERROR(state, payload: any) {
    state.errorStatus = payload;
  }
};

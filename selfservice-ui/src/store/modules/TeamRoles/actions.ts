import { ActionTree } from 'vuex';
import { TeamRoleState } from './types';
import { RootState } from '../../types';
import { TeamRoles } from '@/services/TeamRoles';

/**
 * TeamRoles Actions
 *
 */
export const actions: ActionTree<TeamRoleState, RootState> = {
  /**
   * load roles from server and set to store
   * @param {*} { commit }
   */
  async loadTeam({ commit }, projectId) {
    commit('SET_LOADING', true);
    try {
      const roles = await TeamRoles.getTeamRoles(projectId);
      commit('SET_ROLESLIST', roles.data.team);
      commit('SET_LOADING', false);
    } catch {
      commit('SET_ERROR', true);
      commit('SET_LOADING', false);
    }
  },
  /**
   * clear message
   * @param {*} { commit }
   */
  async clearStatus({ commit }) {
    commit('SET_SUCESS', false);
    commit('SET_ERROR', false);
    commit('SET_LOADING', false);
  },
  /**
   * add team member
   * @param {*} { commit }
   */
  async addTeamMember({ commit }, { userDetails, projectId }) {
    commit('SET_LOADING', true);
    try {
      const roles = await TeamRoles.addTeamMember(userDetails, projectId);
      commit('SET_MEMBER_ADDED', true);
      commit('SET_MEMBER_ADDED_ERROR', false);
      commit('SET_LOADING', false);
    } catch {
      commit('SET_MEMBER_ADDED', false);
      commit('SET_MEMBER_ADDED_ERROR', true);
      commit('SET_LOADING', false);
    }
  }
};

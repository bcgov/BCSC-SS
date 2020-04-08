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
      commit('SET_MEMBER_ADDED_ERROR_LIST', {});
    } catch (error) {
      commit('SET_MEMBER_ADDED_ERROR_LIST', {});
      if (error.response.status === 400) {
        commit('SET_MEMBER_ADDED_ERROR_LIST', error.response.data.errors);
      }
      commit('SET_MEMBER_ADDED', false);
      commit('SET_MEMBER_ADDED_ERROR', true);
      commit('SET_LOADING', false);
    }
  },
  /**
   * get team member detail
   * @param {*} { commit }
   */
  async getTeamMember({ commit }, { projectId, memberId }) {
    commit('SET_LOADING', true);
    try {
      const memberDetails = await TeamRoles.getTeamMember(projectId, memberId);
      commit('SET_MEMBER_DETAILS', memberDetails.data);
      commit('SET_MEMBER_ADDED_ERROR', false);
      commit('SET_LOADING', false);
      commit('SET_MEMBER_ADDED_ERROR_LIST', {});
    } catch (error) {
      commit('SET_MEMBER_ADDED_ERROR_LIST', {});
      if (error && error.response && error.response.status === 400) {
        commit('SET_MEMBER_ADDED_ERROR_LIST', error.response.data.errors);
      }
      commit('SET_MEMBER_ADDED', false);
      commit('SET_MEMBER_ADDED_ERROR', true);
      commit('SET_LOADING', false);
    }
  },
  /**
   * update team member
   * @param {*} { commit }
   */
  async updateTeamMember({ commit }, { userDetails, projectId, memberId }) {
    commit('SET_LOADING', true);
    try {
      const roles = await TeamRoles.updateTeamMember(
        userDetails,
        projectId,
        memberId
      );
      commit('SET_MEMBER_ADDED', true);
      commit('SET_MEMBER_ADDED_ERROR', false);
      commit('SET_LOADING', false);
      commit('SET_MEMBER_ADDED_ERROR_LIST', {});
    } catch (error) {
      commit('SET_MEMBER_ADDED_ERROR_LIST', {});
      if (error && error.response && error.response.status === 400) {
        commit('SET_MEMBER_ADDED_ERROR_LIST', error.response.data.errors);
      }
      commit('SET_MEMBER_ADDED', false);
      commit('SET_MEMBER_ADDED_ERROR', true);
      commit('SET_LOADING', false);
    }
  }
};

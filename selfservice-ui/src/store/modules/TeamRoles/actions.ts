import { ActionTree } from 'vuex';
import { TeamRoleState } from './types';
import { RootState } from '../../types';
import { TeamRoles } from '@/services/TeamRoles';
import { memberDetails } from './defaults';
/**
 * TeamRoles Actions
 *
 */
export const actions: ActionTree<TeamRoleState, RootState> = {
  /**
   * load roles from server and set to store
   * @param {*} { commit }
   */
  async loadTeam({ commit, dispatch }, projectId) {
    commit('SET_LOADING', true);
    try {
      const roles = await TeamRoles.getTeamRoles(projectId);
      commit('SET_ROLESLIST', roles.data.team);
      commit('SET_LOADING', false);
    } catch (error) {
      if (error.response.status === 401) {
        dispatch('SharedModule/unAuthorized', null, { root: true });
      }
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
   * clear message
   * @param {*} { commit }
   */
  async clearMemberStatus({ commit }) {
    commit('SET_MEMBER_ADDED', false);
    commit('SET_MEMBER_ADDED_ERROR', false);
    commit('SET_LOADING', false);
    commit('SET_MEMBER_ADDED_ERROR_LIST', {});
  },
  /**
   * add team member
   * @param {*} { commit }
   */
  async addTeamMember({ commit, dispatch }, { userDetails, projectId }) {
    commit('SET_LOADING', true);
    dispatch('clearMemberStatus');
    try {
      await TeamRoles.addTeamMember(userDetails, projectId);
      commit('SET_MEMBER_ADDED', true);
      commit('SET_MEMBER_ADDED_ERROR', false);
      commit('SET_LOADING', false);
      commit('SET_MEMBER_ADDED_ERROR_LIST', {});
      dispatch('loadTeam', projectId);
      dispatch('clearMemberData');
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
   * get team member detail
   * @param {*} { commit }
   */
  async getTeamMember({ commit, dispatch }, { projectId, memberId }) {
    commit('SET_LOADING', true);
    dispatch('clearMemberStatus');
    try {
      const memberDetailsData = await TeamRoles.getTeamMember(
        projectId,
        memberId
      );
      commit('SET_MEMBER_DETAILS', memberDetailsData.data);
      commit('SET_MEMBER_ADDED_ERROR', false);
      commit('SET_LOADING', false);
      commit('SET_MEMBER_ADDED_ERROR_LIST', {});
    } catch (error) {
      commit('SET_MEMBER_ADDED_ERROR_LIST', {});
      if (error && error.response && error.response.status === 400) {
        commit('SET_MEMBER_ADDED_ERROR_LIST', error.response.data.errors);
      } else if (error.response.status === 401) {
        dispatch('SharedModule/unAuthorized', null, { root: true });
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
  async updateTeamMember(
    { commit, dispatch },
    { userDetails, projectId, memberId }
  ) {
    dispatch('clearMemberStatus');
    commit('SET_LOADING', true);

    try {
      await TeamRoles.updateTeamMember(userDetails, projectId, memberId);
      commit('SET_MEMBER_ADDED', true);
      commit('SET_MEMBER_ADDED_ERROR', false);
      commit('SET_LOADING', false);
      commit('SET_MEMBER_ADDED_ERROR_LIST', {});
      dispatch('loadTeam', projectId);
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
  async deleteTeamMember({ commit, dispatch }, { projectId, memberId }) {
    try {
      await TeamRoles.deleteTeamMember(projectId, memberId);
      commit('SET_LOADING', false);
      dispatch('loadTeam', projectId);
    } catch (error) {
      commit('SET_LOADING', false);
    }
  },
  clearMemberData({ commit }) {
    commit('SET_MEMBER_DETAILS', memberDetails());
  },
  clearErrors({ commit }) {
    commit('SET_MEMBER_ADDED_ERROR_LIST', {});
    commit('SET_MEMBER_ADDED_ERROR', false);
    commit('SET_MEMBER_ADDED', false);
  },
};

import { ActionTree } from 'vuex';
import { ProjectInfoState } from './types';
import { RootState } from '../../types';

import i18n from '../../../i18n';
import { ProjectInfoService } from '@/services/ProjectInfoService';
import router from '@/router';

let projectCallInProgress = false;
let lastProjectId = 0;

/**
 * projectinfo Actions
 *
 */
export const actions: ActionTree<ProjectInfoState, RootState> = {
  /**
   * @param  {} {commit, dispatch}
   * @param  {} projectinfo  list
   */
  async addProjectInfo({ commit, dispatch }, data) {
    commit('SET_LOADING', true);
    try {
      const projectinfo = await ProjectInfoService.createProjectInfo(data);
      commit('SET_LOADING', false);
      commit('SET_PROJECTINFO_SUCCESSFULLY', true);
      commit('SET_PROJECTINFO_ERROR', false);
      commit('SET_PROJECTINFO_MESSAGE', i18n.t('PROJECTINFO_ADD_MESSAGE'));
      commit('SET_EDIT_PROJECTINFO', projectinfo.data);
      const id = projectinfo.data.id;
      router.push(`/project/${id}/team/`);
      // dispatch('loadProjectInfo');
    } catch {
      commit('SET_PROJECTINFO_SUCCESSFULLY', false);
      commit('SET_PROJECTINFO_ERROR', true);
      commit('SET_PROJECTINFO_MESSAGE', '');
    }
  },

  /**
   * load projectinfo from server and set to store
   * @param {*} { commit }
   */
  async loadProjectInfo({ commit, dispatch }) {
    commit('SET_LOADING', true);
    try {
      const projectinfo = await ProjectInfoService.getProjectInfos();
      commit('SET_PROJECTINFOLIST', projectinfo.data.projects);
      commit('SET_LOADING', false);
    } catch (error) {
      if (error.response.status === 401) {
        dispatch('SharedModule/unAuthorized', null, { root: true });
      }
      commit('SET_PROJECTINFO_ERROR', true);
      commit('SET_LOADING', false);
    }
  },
  /**
   * clear message
   * @param {*} { commit }
   */
  async clearStatus({ commit }) {
    commit('SET_PROJECTINFO_SUCCESSFULLY', false);
    commit('SET_PROJECTINFO_ERROR', false);
    commit('SET_PROJECTINFO_MESSAGE', '');
  },
  /**
   * load single projectinfo   by id from server and set to store
   * @param {*} { commit }
   */

  async loadSingleProjectInfo({ commit, dispatch }, id) {
    commit('SET_LOADING', true);

    if (!projectCallInProgress) {
      if (lastProjectId !== id) {
        projectCallInProgress = true;
        lastProjectId = id;
      }
      try {
        const projectinfo = await ProjectInfoService.getProjectInfoById(id);
        commit('SET_EDIT_PROJECTINFO', projectinfo.data);
        commit('SET_LOADING', false);
        projectCallInProgress = false;
        lastProjectId = 0;
      } catch (error) {
        if (error.response.status === 401) {
          dispatch('SharedModule/unAuthorized', null, { root: true });
        }
        commit('SET_PROJECTINFO_SUCCESSFULLY', false);
        commit('SET_PROJECTINFO_ERROR', true);
        commit('SET_LOADING', false);
        projectCallInProgress = false;
        lastProjectId = 0;
      }
    }
  },
  /**
   * update projectinfo
   * @param  {} {commit, dispatch}
   * @param  {} projectinfo   list
   */
  async updateProjectInfo({ commit, dispatch, rootState }, data) {
    commit('SET_LOADING', true);
    try {
      // const { data, redirect } = projectData;
      const { id } = data;
      const isRedirectFromSummaryPage = rootState.SharedModule.isSummaryPage;
      const redirect = !isRedirectFromSummaryPage
        ? `/project/${id}/team/`
        : `/project-container/${id}/`;

      await ProjectInfoService.updateProjectInfo(data);
      commit('SET_LOADING', false);
      commit('SET_PROJECTINFO_SUCCESSFULLY', true);
      commit('SET_PROJECTINFO_ERROR', false);
      commit('SET_PROJECTINFO_MESSAGE', i18n.t('PROJECTINFO_UPDATE_MESSAGE'));
      dispatch('loadProjectInfo');
      router.push(redirect);
    } catch {
      commit('SET_LOADING', false);
      commit('SET_PROJECTINFO_SUCCESSFULLY', false);
      commit('SET_PROJECTINFO_ERROR', true);
      commit('SET_PROJECTINFOMESSAGE', '');
    }
  },

  /**
   * submitProject to server
   * @param {*} { commit }
   */

  async submitProject({ commit, dispatch }, data) {
    commit('SET_LOADING', true);
    try {
      const { projectId } = data;
      const response = await ProjectInfoService.updateStatusOfProject(
        projectId,
        2
      );
      if (response.data.testAccountSuccess) {
        commit('SET_TEST_ACCOUNT_SUCCESS', true);
      } else {
        commit('SET_TEST_ACCOUNT_SUCCESS', false);
      }
      if (response.data.isCreated) {
        commit('SET_IS_CREATED', true);
        commit('SET_IS_UPDATED', false);
      }
      if (response.data.isUpdated) {
        commit('SET_IS_UPDATED', true);
        commit('SET_IS_CREATED', false);
      }
      dispatch('loadSingleProjectInfo', projectId);
      commit('SET_PROJECT_SUBMIT_ERROR', false);
      commit('SET_PROJECT_SUBMIT_SUCESS', true);
      commit('SET_LOADING', false);
    } catch {
      commit('SET_PROJECT_SUBMIT_SUCESS', false);
      commit('SET_PROJECT_SUBMIT_ERROR', true);
      commit('SET_LOADING', false);
    }
  },
  /**
   * clear message
   * @param {*} { commit }
   */
  clearSubmitProjectStatus({ commit }) {
    commit('SET_PROJECT_SUBMIT_SUCESS', false);
    commit('SET_PROJECT_SUBMIT_ERROR', false);
  },
  /**
   * reset project call status
   */
  resetprogress() {
    projectCallInProgress = false;
  },
  /**
   * updateProjectStatus to server
   * @param {*} { commit }
   */
  async updateProjectStatus({ commit, dispatch }, data) {
    commit('SET_LOADING', true);
    try {
      const { projectId, statusId } = data;
      await ProjectInfoService.updateStatusOfProject(projectId, statusId);
      dispatch('loadSingleProjectInfo', projectId);
      commit('SET_STATUS_CHANGE_ERROR', false);
      commit('SET_STATUS_CHANGE_SUCESS', true);
      commit('SET_LOADING', false);
    } catch {
      commit('SET_STATUS_CHANGE_SUCESS', false);
      commit('SET_STATUS_CHANGE_ERROR', true);
      commit('SET_LOADING', false);
    }
  },
  /**
   * delete Project
   * @param {*} { commit }
   */
  async deleteProject({ commit }, data) {
    commit('SET_LOADING', true);
    try {
      const { projectId } = data;
      commit('SET_DELETE_SUCESS', false);
      await ProjectInfoService.deleteProject(projectId);

      commit('SET_DELETE_ERROR', false);
      commit('SET_DELETE_SUCESS', true);
      commit('SET_LOADING', false);
    } catch {
      commit('SET_DELETE_SUCESS', false);
      commit('SET_DELETE_ERROR', true);
      commit('SET_LOADING', false);
    }
  },

  /**
   * load projectinfo from server and set to store
   * @param {*} { commit }
   */
  async loadProjectHistory({ commit }, id) {
    commit('SET_LOADING', true);
    try {
      const projectHistory = await ProjectInfoService.getProjectHistory(id);
      commit('SET_PROJECTHISTORY', projectHistory.data.history);
      commit('SET_LOADING', false);
    } catch {
      commit('SET_PROJECTHISTORY_ERROR', true);
      commit('SET_LOADING', false);
    }
  },
};

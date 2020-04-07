import { ActionTree } from 'vuex';
import { ProjectInfoState } from './types';
import { RootState } from '../../types';

import i18n from '../../../i18n';
import { ProjectInfoService } from '@/services/ProjectInfoService';
import router from '@/router';

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
      router.push(`/project/${id}/technical/`);
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
  async loadProjectInfo({ commit }) {
    commit('SET_LOADING', true);
    try {
      const projectinfo = await ProjectInfoService.getProjectInfos();
      commit('SET_PROJECTINFOLIST', projectinfo.data.projects);
      commit('SET_LOADING', false);
    } catch {
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
  async loadSingleProjectInfo({ commit }, id) {
    commit('SET_LOADING', true);
    try {
      const projectinfo = await ProjectInfoService.getProjectInfoById(id);
      commit('SET_EDIT_PROJECTINFO', projectinfo.data);
      commit('SET_LOADING', false);
    } catch {
      commit('SET_PROJECTINFO_SUCCESSFULLY', false);
      commit('SET_PROJECTINFO_ERROR', true);
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
      const isRedirectFromSummaryPage = rootState.SharedModule.isSummaryPage;
      const redirect = !isRedirectFromSummaryPage ? 'technical' : 'summary';
      const { id } = data;
      await ProjectInfoService.updateProjectInfo(data);
      commit('SET_LOADING', false);
      commit('SET_PROJECTINFO_SUCCESSFULLY', true);
      commit('SET_PROJECTINFO_ERROR', false);
      commit('SET_PROJECTINFO_MESSAGE', i18n.t('PROJECTINFO_UPDATE_MESSAGE'));
      dispatch('loadProjectInfo');
      router.push(`/project/${id}/${redirect}/`);
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

  async submitProject({ commit, rootState }, data) {
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
  }
};

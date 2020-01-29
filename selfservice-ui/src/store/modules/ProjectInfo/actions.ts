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
    const projectinfo = await ProjectInfoService.getProjectInfos();
    commit('SET_PROJECTINFOLIST', projectinfo.data);
    commit('SET_LOADING', false);
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
  async updateProjectInfo({ commit, dispatch }, data: any) {
    commit('SET_LOADING', true);
    try {
      await ProjectInfoService.updateProjectInfo(data);
      commit('SET_LOADING', false);
      commit('SET_PROJECTINFO_SUCCESSFULLY', true);
      commit('SET_PROJECTINFO_ERROR', false);
      commit('SET_PROJECTINFO_MESSAGE', i18n.t('PROJECTINFO_UPDATE_MESSAGE'));
      dispatch('loadProjectInfo');
    } catch {
      commit('SET_LOADING', false);
      commit('SET_PROJECTINFO_SUCCESSFULLY', false);
      commit('SET_PROJECTINFO_ERROR', true);
      commit('SET_PROJECTINFOMESSAGE', '');
    }
  },
  /**
   * remove projectinfo
   * @param  {} {commit, dispatch}
   * @param  {} projectinfo   list
   */
  async removeProjectInfo({ commit, dispatch }, id: any) {
    commit('SET_LOADING', true);
    try {
      await ProjectInfoService.deleteProjectInfo(id);
      commit('SET_LOADING', false);
      commit('SET_PROJECTINFO_SUCCESSFULLY', true);
      commit('SET_PROJECTINFO_MESSAGE', i18n.t('PROJECTINFO_DELETE_MESSAGE'));
      commit('SET_PROJECTINFO_ERROR', false);
      dispatch('loadProjectInfo');
    } catch {
      commit('SET_LOADING', false);
      commit('SET_PROJECTINFO_SUCCESSFULLY', false);
      commit('SET_PROJECTINFO_ERROR', true);
      commit('SET_PROJECTINFO_MESSAGE', '');
    }
  }
};

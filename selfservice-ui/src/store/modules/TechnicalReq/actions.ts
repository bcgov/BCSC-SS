import router from '@/router';
import i18n from '@/i18n';
import { ActionTree } from 'vuex';
import { TechnicalReqState } from './types';
import { RootState } from '../../types';
import { TechnicalReqService } from '@/services/TechnicalReqService';

/**
 * technicalreq Actions
 *
 */
export const actions: ActionTree<TechnicalReqState, RootState> = {
  /**
   * @param  {} {commit, dispatch}
   * @param  {} technicalreq  list
   */
  async addTechnicalReq({ commit, rootState, dispatch }, data) {
    commit('SET_LOADING', true);
    try {
      await TechnicalReqService.createTechnicalReq(data);

      commit('SET_LOADING', false);
      commit('SET_TECHNICALREQ_SUCCESSFULLY', true);
      commit('SET_TECHNICALREQ_ERROR', false);
      commit('SET_TECHNICALREQ_MESSAGE', i18n.t('TECHNICALREQ_ADD_MESSAGE'));
      // dispatch('loadTechnicalReq');
      const projectId =
        data.projectId || rootState.ProjectInfoModule.singleProjectInfo;
      dispatch('redirect', projectId);
      // router.push(`/project/${projectId}/package/`);
    } catch {
      commit('SET_TECHNICALREQ_SUCCESSFULLY', false);
      commit('SET_TECHNICALREQ_ERROR', true);
      commit('SET_TECHNICALREQ_MESSAGE', '');
    }
  },

  /**
   * clear message
   * @param {*} { commit }
   */
  async clearStatus({ commit }) {
    commit('SET_TECHNICALREQ_SUCCESSFULLY', false);
    commit('SET_TECHNICALREQ_ERROR', false);
    commit('SET_TECHNICALREQ_MESSAGE', '');
  },
  /**
   * load single technicalreq   by project id from server and set to store
   * @param {*} { commit }
   */
  async loadTechnicalReqDetails({ commit }, id) {
    commit('SET_LOADING', true);
    try {
      const technicalreq = await TechnicalReqService.getTechnicalReqByProjectId(
        id
      );
      commit('SET_EDIT_TECHNICALREQ', technicalreq.data);
      commit('SET_LOADING', false);
    } catch {
      commit('SET_TECHNICALREQ_SUCCESSFULLY', false);
      commit('SET_TECHNICALREQ_ERROR', true);
      commit('SET_LOADING', false);
    }
  },
  /**
   * update technicalreq
   * @param  {} {commit, dispatch}
   * @param  {} technicalreq   list
   */
  async updateTechnicalReq(state, data: any) {
    const { commit, rootState, dispatch } = state;
    const isRedirectFromSummaryPage =
      state.rootState.SharedModule.isSummaryPage;
    commit('SET_LOADING', true);
    try {
      const technicalreq = await TechnicalReqService.updateTechnicalReq(data);
      commit('SET_LOADING', false);
      commit('SET_TECHNICALREQ_SUCCESSFULLY', true);
      commit('SET_TECHNICALREQ_ERROR', false);
      commit('SET_TECHNICALREQ_MESSAGE', i18n.t('TECHNICALREQ_UPDATE_MESSAGE'));
      const projectId =
        data.projectId || rootState.ProjectInfoModule.singleProjectInfo;
      dispatch('redirect', projectId);
    } catch {
      commit('SET_LOADING', false);
      commit('SET_TECHNICALREQ_SUCCESSFULLY', false);
      commit('SET_TECHNICALREQ_ERROR', true);
      commit('SET_TECHNICALREQMESSAGE', '');
    }
  },
  redirect(state, projectId) {
    const isRedirectFromSummaryPage =
      state.rootState.SharedModule.isSummaryPage;
    const nextPage = isRedirectFromSummaryPage ? 'summary' : 'package';
    router.push(`/project/${projectId}/${nextPage}/`);
  }
};

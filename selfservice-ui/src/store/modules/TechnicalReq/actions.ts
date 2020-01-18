import { ActionTree } from 'vuex';
import { TechnicalReqState } from './types';
import { RootState } from '../../types';

import i18n from '@/i18n';
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
  async addTechnicalReq({ commit, dispatch }, data) {
    commit('SET_LOADING', true);

    try {
      await TechnicalReqService.createTechnicalReq(data);
      commit('SET_LOADING', false);
      commit('SET_TECHNICALREQ_SUCCESSFULLY', true);
      commit('SET_TECHNICALREQ_ERROR', false);
      commit('SET_TECHNICALREQ_MESSAGE', i18n.t('TECHNICALREQ_ADD_MESSAGE'));
      //   dispatch('loadTechnicalReq');
    } catch {
      commit('SET_TECHNICALREQ_SUCCESSFULLY', false);
      commit('SET_TECHNICALREQ_ERROR', true);
      commit('SET_TECHNICALREQ_MESSAGE', '');
    }
  },

  /**
   * load technicalreq from server and set to store
   * @param {*} { commit }
   */
  async loadTechnicalReq({ commit }) {
    commit('SET_LOADING', true);
    const technicalreq = await TechnicalReqService.getTechnicalReqs();
    commit('SET_TECHNICALREQLIST', technicalreq.data);
    commit('SET_LOADING', false);
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
   * load single technicalreq   by id from server and set to store
   * @param {*} { commit }
   */
  async loadSingleTechnicalReq({ commit }, id) {
    commit('SET_LOADING', true);

    try {
      const technicalreq = await TechnicalReqService.getTechnicalReqById(id);
      commit('SET_EDIT_TECHNICALREQ', technicalreq.data);
      commit('SET_LOADING', false);
    } catch {
      commit('SET_TECHNICALREQ_SUCCESSFULLY', false);
      commit('SET_TECHNICALREQ_ERROR', true);
    }
  },
  /**
   * update technicalreq
   * @param  {} {commit, dispatch}
   * @param  {} technicalreq   list
   */
  async updateTechnicalReq({ commit, dispatch }, data: any) {
    commit('SET_LOADING', true);
    try {
      const technicalreq = await TechnicalReqService.updateTechnicalReq(data);
      commit('SET_LOADING', false);
      commit('SET_TECHNICALREQ_SUCCESSFULLY', true);
      commit('SET_TECHNICALREQ_ERROR', false);
      commit('SET_TECHNICALREQ_MESSAGE', i18n.t('TECHNICALREQ_UPDATE_MESSAGE'));
      dispatch('loadTechnicalReq');
    } catch {
      commit('SET_LOADING', false);
      commit('SET_TECHNICALREQ_SUCCESSFULLY', false);
      commit('SET_TECHNICALREQ_ERROR', true);
      commit('SET_TECHNICALREQMESSAGE', '');
    }
  },
  /**
   * remove technicalreq
   * @param  {} {commit, dispatch}
   * @param  {} technicalreq   list
   */
  async removeTechnicalReq({ commit, dispatch }, id: any) {
    commit('SET_LOADING', true);
    try {
      await TechnicalReqService.deleteTechnicalReq(id);
      commit('SET_LOADING', false);
      commit('SET_TECHNICALREQ_SUCCESSFULLY', true);
      commit('SET_TECHNICALREQ_MESSAGE', i18n.t('TECHNICALREQ_DELETE_MESSAGE'));
      commit('SET_TECHNICALREQ_ERROR', false);
      dispatch('loadTechnicalReq');
    } catch {
      commit('SET_LOADING', false);
      commit('SET_TECHNICALREQ_SUCCESSFULLY', false);
      commit('SET_TECHNICALREQ_ERROR', true);
      commit('SET_TECHNICALREQ_MESSAGE', '');
    }
  }
};

import { ActionTree } from 'vuex';
import { SharedState } from './types';
import { RootState } from '../../types';

import i18n from '../../../i18n';
// import { ProjectInfoService } from '@/services/ProjectInfoService';
import router from '@/router';

/**
 * projectinfo Actions
 *
 */
export const actions: ActionTree<SharedState, RootState> = {
  /**
   * @param  {} {commit}
   * @param  {} flag redirectfromsummary page
   */
  async rediectFromSummaryPage({ commit }, flag: boolean) {
    commit('SET_REDIRECT_FROM', flag);
  }
};

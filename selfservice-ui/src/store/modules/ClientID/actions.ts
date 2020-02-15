import { ActionTree } from 'vuex';
import { ClientIdState } from './types';
import { RootState } from '../../types';
// import i18n from '../../../i18n';

import ClientID from '@/services/ClientID';

/**
 * package Actions
 *
 */
export const actions: ActionTree<ClientIdState, RootState> = {
  /**
   * load getApiDetails from server and set to store
   * @param {*} { commit }
   */
  async getClientIdDetails({ commit }, id: number) {
    commit('SET_LOADING', true);
    const apiData = await ClientID.getApiData(id);

    commit('SET_APIDETAILS', apiData.data);
    commit('SET_LOADING', false);
  }
};

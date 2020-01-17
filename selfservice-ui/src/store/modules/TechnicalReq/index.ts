import { Module } from 'vuex';
import { getters } from './getters';
import { actions } from './actions';
import { mutations } from './mutations';
import { TechnicalReqState } from './types';
import { RootState } from '../../types';

/**
 * technicalreq state
 */
export const state: TechnicalReqState = {
  technicalreqList: [],
  loading: false,
  successStatus: false,
  errorStatus: false,
  singleTechnicalReq: [],
  message: ''
};

const namespaced: boolean = true;

const TechnicalReqModule: Module<TechnicalReqState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations
};

export default TechnicalReqModule;

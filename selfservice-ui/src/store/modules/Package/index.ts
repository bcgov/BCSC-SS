import { Module } from 'vuex';
import { getters } from './getters';
import { actions } from './actions';
import { mutations } from './mutations';
import { PackageState } from './types';
import { RootState } from '../../types';

/**
 * package state
 */
export const state: PackageState = {
  packageList: [],
  loading: false,
  successStatus: false,
  errorStatus: false,
  message: ''
};

const namespaced: boolean = true;

const PackageModule: Module<PackageState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations
};

export default PackageModule;

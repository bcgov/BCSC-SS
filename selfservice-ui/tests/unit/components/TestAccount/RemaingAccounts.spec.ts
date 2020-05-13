import { shallowMount } from '@vue/test-utils';
import RemaingAccounts from '@/components/TestAccount/RemaingAccounts.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
let vuetify: any;
vuetify = new Vuetify();

describe('RemaingAccounts.vue', () => {
  const store = new Vuex.Store({
    modules: {
      TestAccountModule: {
        namespaced: true,
        state: {},
        getters: {
          getTestAccountCount: jest.fn(),
          isLoading: jest.fn(),
        },
        actions: {
          loadTestAccountCount: jest.fn(),
          clearStatus: jest.fn(),
        },
      },
    },
  });

  const mountFunction = (options: any) => {
    return shallowMount(RemaingAccounts, {
      store,
      vuetify,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options,
    });
  };

  it('renders props when passed with gettors', () => {
    const RemaingAccountsPage = mountFunction({});
    expect(RemaingAccountsPage.element).toMatchSnapshot();
  });
});

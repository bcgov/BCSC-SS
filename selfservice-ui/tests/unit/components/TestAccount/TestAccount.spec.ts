import { shallowMount } from '@vue/test-utils';
import TestAccount from '@/components/TestAccount/TestAccount.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
let vuetify: any;
vuetify = new Vuetify();

describe('TestAccount.vue', () => {
  const store = new Vuex.Store({
    modules: {
      TestAccountModule: {
        namespaced: true,
        state: {},
        getters: {
          successStatus: jest.fn(),
          errorStatus: jest.fn(),
          isLoading: jest.fn()
        },
        actions: {
          addTestAccounts: jest.fn(),
          clearStatus: jest.fn()
        }
      }
    }
  });

  const mountFunction = (options: any) => {
    return shallowMount(TestAccount, {
      store,
      vuetify,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options
    });
  };

  it('renders props when passed with gettors', () => {
    const TestAccountPage = mountFunction({});
    expect(TestAccountPage.element).toMatchSnapshot();
  });
});

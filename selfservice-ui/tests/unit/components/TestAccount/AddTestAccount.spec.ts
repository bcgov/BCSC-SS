import { shallowMount } from '@vue/test-utils';
import AddTestAccount from '@/components/TestAccount/AddTestAccount.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
let vuetify: any;
vuetify = new Vuetify();

describe('AddTestAccount.vue', () => {
  const store = new Vuex.Store({
    modules: {
      AddTestAccountModule: {
        namespaced: true,
        state: {},
        getters: {
          successStatus: jest.fn(),
          errorStatus: jest.fn(),
          isLoading: jest.fn(),
        },
        actions: {
          addAddTestAccounts: jest.fn(),
          clearStatus: jest.fn(),
        },
      },
    },
  });

  const mountFunction = (options: any) => {
    return shallowMount(AddTestAccount, {
      store,
      vuetify,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options,
    });
  };

  it('renders props when passed with gettors', () => {
    const AddTestAccountPage = mountFunction({});
    expect(AddTestAccountPage.element).toMatchSnapshot();
  });
});

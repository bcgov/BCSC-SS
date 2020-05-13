import { shallowMount, mount } from '@vue/test-utils';
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
      TestAccountModule: {
        namespaced: true,
        state: {},
        getters: {
          getTestAccountCount: jest.fn(),
          isLoading: jest.fn(),
          getTestAccountSuccessData: jest.fn(),
        },
        actions: {
          loadTestAccountCount: jest.fn(),
          clearStatus: jest.fn(),
          addTestAccounts: jest.fn(),
        },
      },
    },
  });

  const mountFunction = (options: any) => {
    return mount(AddTestAccount, {
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

  it('renders props when delete member', () => {
    const AddTestAccountPage = mountFunction({});
    const toggleAddMember = jest.fn();

    AddTestAccountPage.setData({ testAccounts: 'test' });
    const button = AddTestAccountPage.find('.submit-test-account');
    AddTestAccountPage.vm.$on('action-btn:clicked', toggleAddMember);
    button.trigger('click');

    expect(AddTestAccountPage.element).toMatchSnapshot();
  });
});

import { shallowMount } from '@vue/test-utils';
import AddTeamMember from '@/components/TeamRoles/AddTeamMember.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
let vuetify: any;
vuetify = new Vuetify();

describe('AddTeamMember.vue', () => {
  const store = new Vuex.Store({
    modules: {
      TeamRolesModule: {
        namespaced: true,
        state: {},
        getters: {
          successStatus: jest.fn(),
          errorStatus: jest.fn(),
          isLoading: jest.fn(),

          getMemberDetails: jest.fn(() => {
            return {};
          }),
          getMemberErrorList: jest.fn(),
          memberSucessStatus: jest.fn(),
          memberErrorStatus: jest.fn(),
        },
        actions: {
          clearMemberData: jest.fn(),
          getTeamMember: jest.fn(),
        },
      },
      KeyCloakModule: {
        namespaced: true,
        state: {},
        getters: {
          isAdmin: jest.fn(() => {
            return true;
          }),
        },
        actions: { setLogout: jest.fn() },
      },
    },
  });

  const mountFunction = (options: any) => {
    return shallowMount(AddTeamMember, {
      store,
      vuetify,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options,
      stubs: {
        VForm: {
          render: () => jest.fn(),
          methods: {
            resetValidation: () => jest.fn(),
          },
        },
      },
    });
  };

  it('renders props when passed with gettors', () => {
    const AddTeamMemberPage = mountFunction({});
    expect(AddTeamMemberPage.element).toMatchSnapshot();
  });
  it('renders props when passed with gettors with member id', () => {
    const AddTeamMemberPage = mountFunction({
      propsData: {
        memberId: 2,
      },
    });
    expect(AddTeamMemberPage.element).toMatchSnapshot();
  });
});

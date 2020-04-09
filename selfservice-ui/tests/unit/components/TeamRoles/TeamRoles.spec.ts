import { shallowMount, mount } from '@vue/test-utils';
import TeamRoles from '@/components/TeamRoles/TeamRoles.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
let vuetify: any;
vuetify = new Vuetify();

describe('TeamRoles.vue', () => {
  const store = new Vuex.Store({
    modules: {
      TeamRolesModule: {
        namespaced: true,
        state: {},
        getters: {
          successStatus: jest.fn(),
          errorStatus: jest.fn(),
          isLoading: jest.fn(),

          getTeamList: jest.fn(() => {
            return [];
          })
        },
        actions: {
          loadTeam: jest.fn(),
          clearStatus: jest.fn()
        }
      }
    }
  });

  const mountFunction = (options: any) => {
    return shallowMount(TeamRoles, {
      store,
      vuetify,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options
    });
  };

  it('renders props when passed with gettors', () => {
    const TeamRolesPage = mountFunction({});
    expect(TeamRolesPage.element).toMatchSnapshot();
  });
});

describe('TeamRoles Mount.vue', () => {
  const store = new Vuex.Store({
    modules: {
      TeamRolesModule: {
        namespaced: true,
        state: {},
        getters: {
          successStatus: jest.fn(),
          errorStatus: jest.fn(),
          isLoading: jest.fn(),

          getTeamList: jest.fn(() => {
            return [];
          }),
          getMemberDetails: jest.fn(() => {
            return {};
          }),
          getMemberErrorList: jest.fn(),
          memberSucessStatus: jest.fn(),
          memberErrorStatus: jest.fn()
        },
        actions: {
          loadTeam: jest.fn(),
          clearMemberData: jest.fn()
        }
      }
    }
  });

  const mountFunction = (options: any) => {
    return mount(TeamRoles, {
      store,
      vuetify,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options
    });
  };

  it('renders props when passed with gettors', () => {
    const TeamRolesPage = mountFunction({});
    const toggleAddMember = jest.fn();
    TeamRolesPage.setData({ isLoading: false });
    const button = TeamRolesPage.find('.team-roles');
    TeamRolesPage.vm.$on('action-btn:clicked', toggleAddMember);
    button.trigger('click');

    expect(TeamRolesPage.element).toMatchSnapshot();
  });
});

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
          }),
        },
        actions: {
          loadTeam: jest.fn(),
          clearStatus: jest.fn(),
        },
      },
    },
  });

  const mountFunction = (options: any) => {
    return shallowMount(TeamRoles, {
      store,
      vuetify,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options,
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
            return [
              {
                email: 'asd@gov.bc.ca',
                firstName: 'John',
                id: 118,
                isCurrentUser: true,
                lastName: 'Doe',
                phone: '0987654321',
                projectId: 36,
                role: 1,
                userId: 28,
              },
            ];
          }),
          getMemberDetails: jest.fn(() => {
            return {};
          }),
          getMemberErrorList: jest.fn(),
          memberSucessStatus: jest.fn(),
          memberErrorStatus: jest.fn(),
        },
        actions: {
          loadTeam: jest.fn(),
          clearMemberData: jest.fn(),
        },
      },
      KeyCloakModule: {
        namespaced: true,
        state: {},
        getters: {
          isLoggedin: jest.fn(() => {
            return true;
          }),
          isAdmin: jest.fn(() => {
            return true;
          }),
        },
        actions: { setLogout: jest.fn() },
      },
    },
  });

  const mountFunction = (options: any) => {
    return mount(TeamRoles, {
      store,
      vuetify,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options,
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
  it('renders props when delete member', () => {
    const TeamRolesPage = mountFunction({});
    const toggleAddMember = jest.fn();

    TeamRolesPage.setData({ isLoading: false });
    const button = TeamRolesPage.find('.delete-member');
    TeamRolesPage.vm.$on('action-btn:clicked', toggleAddMember);
    button.trigger('click');

    expect(TeamRolesPage.element).toMatchSnapshot();
  });
});

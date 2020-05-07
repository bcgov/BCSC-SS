import { shallowMount } from '@vue/test-utils';
import Profile from '@/components/Profile/Profile.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
let vuetify: any;
vuetify = new Vuetify();

describe('Profile.vue', () => {
  const store = new Vuex.Store({
    modules: {
      KeyCloakModule: {
        namespaced: true,
        state: {},
        getters: {
          filedsToShow: jest.fn(() => {
            return { email: true, phone: true };
          }),
          userProfile: jest.fn(() => {
            return { firstName: 'john', lastName: 'Deo' };
          }),
          errorStatus: jest.fn(() => {
            return false;
          }),
          profileErrorStatus: jest.fn(),
        },
        actions: {
          updateProfile: jest.fn(),
          errorStatus: jest.fn(),
        },
      },
    },
  });

  const mountFunction = (options: any) => {
    return shallowMount(Profile, {
      store,
      vuetify,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options,
    });
  };

  it('renders props when passed with gettors', () => {
    const dashboard = mountFunction({});
    expect(dashboard.element).toMatchSnapshot();
  });
});

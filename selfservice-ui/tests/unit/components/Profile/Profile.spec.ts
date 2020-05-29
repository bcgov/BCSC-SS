import { shallowMount, mount } from '@vue/test-utils';
import Profile from '@/components/Profile/Profile.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
import Vue from 'vue';
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
            return {
              email: 'asd1@gov.bc.ca',
              firstName: 'John',
              id: 28,
              lastName: 'Doe',
              phone: '0987654321',
            };
          }),
          errorStatus: jest.fn(() => {
            return false;
          }),
          profileErrorStatus: jest.fn(),
          emailExistErrorStatus: jest.fn(),
        },
        actions: {
          updateProfile: jest.fn(),
          errorStatus: jest.fn(),
        },
      },
    },
  });

  const mountFunction = (options: any) => {
    return mount(Profile, {
      store,
      vuetify,
      sync: false,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options,
    });
  };

  it('renders props when passed with gettors', () => {
    const profilePage = mountFunction({});
    expect(profilePage.element).toMatchSnapshot();
  });

  it('renders popup on button click', async () => {
    const profilePage = mountFunction({});
    const toggleDisclaimer = jest.fn();
    profilePage.setData({
      phone: '0987654321',
      email: 'asd2@gov.bc.ca',
    });
    await Vue.nextTick();
    profilePage.setData({ valid: true });
    await Vue.nextTick();
    const button = profilePage.find('.btn-profile-update');
    profilePage.vm.$on('action-btn:clicked', toggleDisclaimer);
    button.trigger('click');
    expect(profilePage.element).toMatchSnapshot();
  });

  it('renders props when passed with gettors', async () => {
    const profilePage = mountFunction({});
    const toggleDisclaimer = jest.fn();
    const createOrUpdateProfile = jest.fn();
    profilePage.setData({
      phone: '0987654321',
      email: 'asd2@gov.bc.ca',
    });
    await Vue.nextTick();
    profilePage.setData({ valid: true });
    await Vue.nextTick();
    const button = profilePage.find('.btn-profile-update');
    profilePage.vm.$on('action-btn:clicked', toggleDisclaimer);
    button.trigger('click');
    await Vue.nextTick();
    profilePage.setData({ buttonEnable: true });
    await Vue.nextTick();
    const button2 = profilePage.find('.btn-submit-terms-profile');
    profilePage.vm.$on('action-btn:clicked', createOrUpdateProfile);
    button2.trigger('click');

    expect(profilePage.element).toMatchSnapshot();
  });
});

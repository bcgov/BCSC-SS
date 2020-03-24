/* tslint:disable */
import { mount, createLocalVue } from '@vue/test-utils';
import Header from '@/components/Header/Header.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
import VueRouter from 'vue-router';

describe('Header.vue', () => {
  let wrapper: any;

  let vuetify: any;
  const localVue = createLocalVue();

  localVue.use(Vuetify);
  vuetify = new Vuetify();
  localVue.use(VueRouter);
  const router = new VueRouter();
  localVue.use(Vuex);
  const store = new Vuex.Store({
    modules: {
      KeyCloakModule: {
        namespaced: true,
        state: {},
        getters: {
          userProfile: jest.fn(() => {
            return {
              firstName: 'user',
              lastName: 'lastName'
            };
          }),
          isLoggedin: jest.fn(() => {
            return true;
          }),
          isAdmin: jest.fn(() => {
            return true;
          })
        },
        actions: { setLogout: jest.fn() }
      }
    }
  });
  const mountFunction = (options: any) => {
    return mount(Header, {
      vuetify,
      localVue,
      router,
      store,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options
    });
  };

  afterEach(() => {
    wrapper.destroy();
  });

  it('renders props when passed', () => {
    wrapper = mountFunction({});
    expect(wrapper.element).toMatchSnapshot();
  });
  it('Toggle menu onlick ', () => {
    wrapper = mountFunction({});
    const event = jest.fn();
    const button = wrapper.find('.toggleMenu');
    wrapper.vm.$on('action-btn:clicked', event);
    button.trigger('click');

    expect(wrapper.element).toMatchSnapshot();
  });

  it('Logout user on logout button onlick ', () => {
    wrapper = mountFunction({});

    const event = jest.fn();
    const button = wrapper.find('.logout');
    wrapper.vm.$on('action-btn:clicked', event);
    button.trigger('click');

    expect(wrapper.element).toMatchSnapshot();
  });
});

/* tslint:disable */
import { shallowMount, createLocalVue } from '@vue/test-utils';
import Header from '@/components/Header/Header.vue';
import vuetify from 'vuetify';
import Vuex from 'vuex';
import VueRouter from 'vue-router';

describe('Header.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);
    localVue.use(VueRouter);
    const router = new VueRouter();
    localVue.use(Vuex);
    const store = new Vuex.Store({
      modules: {
        KeyCloakModule: {
          state: {},
          getters: {
            userProfile: jest.fn(),
            isLoggedin: jest.fn()
          }
        }
      }
    });

    wrapper = shallowMount(Header, {
      localVue,
      router,
      store
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});

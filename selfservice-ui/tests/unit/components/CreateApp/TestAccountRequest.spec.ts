import { mount, createLocalVue } from '@vue/test-utils';
import TestAccountRequest from '@/components/CreateApp/TestAccountRequest.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
import i18n from '@/i18n';
// import Vue from 'vue';

describe('TestAccountRequest.vue', () => {
  let vuetify: any;
  const localVue = createLocalVue();
  // tslint:disable-next-line
  const $t = jest.fn(() => {});

  localVue.use(Vuetify);
  localVue.use(Vuex);
  vuetify = new Vuetify();
  const store = new Vuex.Store({
    modules: {
      PackageAndTestModule: {
        namespaced: true,
        state: {},
        getters: {
          isLoggedin: jest.fn(),
          successStatus: jest.fn(),
          errorStatus: jest.fn()
        },
        actions: {
          addTestAccountRequestToProject: jest.fn()
        }
      }
    }
  });

  const mountFunction = (options: any) => {
    return mount(TestAccountRequest, {
      store,
      vuetify,
      localVue,
      mocks: { $t },
      ...options
    });
  };

  it('renders props when passed', () => {
    const wrapper = mountFunction({});

    expect(wrapper.element).toMatchSnapshot();
  });

  it('select on package on click ', () => {
    const wrapper = mountFunction({});
    const event = jest.fn();
    const button = wrapper.find('.test-account');
    wrapper.vm.$on('action-btn:clicked', event);
    button.trigger('click');

    expect(wrapper.element).toMatchSnapshot();
  });

  it('submit form with selected package on submit click ', () => {
    const wrapper = mountFunction({});
    const event = jest.fn();
    const button = wrapper.find('.submit-account');
    wrapper.vm.$on('action-btn:clicked', event);
    button.trigger('click');

    expect(wrapper.element).toMatchSnapshot();
  });
});

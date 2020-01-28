import { mount, createLocalVue } from '@vue/test-utils';
import PackageSelect from '@/components/CreateApp/PackageSelect.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
// import Vue from 'vue';

describe('PackageSelect.vue', () => {
  let vuetify: any;
  const localVue = createLocalVue();

  localVue.use(Vuetify);
  localVue.use(Vuex);
  vuetify = new Vuetify();
  const store = new Vuex.Store({
    modules: {
      PackageAndTestModule: {
        namespaced: true,
        state: {},
        getters: {
          getPackageList: () => [
            {
              claimNames: ['Given name', 'Surname'],
              description: 'This package contains the following data:',
              id: 1,
              packageName: 'Package 1'
            },
            {
              claimNames: ['Given name', 'Surname'],
              description: 'This package contains the following data:',
              id: 2,
              packageName: 'Package 2'
            }
          ],
          isLoggedin: jest.fn(),
          successStatus: jest.fn(),
          errorStatus: jest.fn()
        },
        actions: { addPackagetoProject: jest.fn(), loadPackage: jest.fn() }
      }
    }
  });

  const mountFunction = (options: any) => {
    return mount(PackageSelect, {
      store,
      vuetify,
      localVue,
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
    const button = wrapper.find('.select-package');
    wrapper.vm.$on('action-btn:clicked', event);
    button.trigger('click');

    expect(wrapper.element).toMatchSnapshot();
  });

  it('submit form with selected package on submit click ', () => {
    const wrapper = mountFunction({});
    const event = jest.fn();
    const button = wrapper.find('.submit-package');
    wrapper.vm.$on('action-btn:clicked', event);
    button.trigger('click');

    expect(wrapper.element).toMatchSnapshot();
  });
});

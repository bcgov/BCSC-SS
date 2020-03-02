import { mount, createLocalVue } from '@vue/test-utils';
import PackageSelect from '@/components/CreateApp/PackageSelect.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
// import Vue from 'vue';

describe('PackageSelect.vue', () => {
  let vuetify: any;
  const router = new VueRouter();
  const localVue = createLocalVue();

  localVue.use(Vuetify);
  localVue.use(VueRouter);
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
      },
      TechnicalReqModule: {
        namespaced: true,
        state: {},
        getters: {
          getSingleTechnicalReq: jest.fn(),
          getTechnicalReq: jest.fn(),
          isLoading: jest.fn()
        },
        actions: {
          getSingleTechnicalReq: jest.fn(),
          addTechnicalReq: jest.fn()
        }
      },
      SharedModule: {
        namespaced: true,
        state: {},
        getters: {
          isRedirectFromSummaryPage: jest.fn(() => {
            return true;
          })
        },
        actions: {
          redirectFromSummaryPage: jest.fn()
        }
      }
    }
  });

  const mountFunction = (options: any) => {
    return mount(PackageSelect, {
      store,
      vuetify,
      localVue,
      router,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
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
  it('should call gotback on back button click ', () => {
    const wrapper = mountFunction({});
    const event2 = jest.fn();
    const button = wrapper.find('.back-btn');
    wrapper.vm.$on('action-btn:clicked', event2);
    button.trigger('click');
    expect(wrapper.element).toMatchSnapshot();
  });
});

describe('PackageSelect.vue from summary page', () => {
  let vuetify: any;
  const router1 = new VueRouter();
  const localVue = createLocalVue();

  localVue.use(Vuetify);
  localVue.use(VueRouter);
  localVue.use(Vuex);
  vuetify = new Vuetify();
  const storeData = new Vuex.Store({
    modules: {
      PackageAndTestModule: {
        namespaced: true,
        state: {},
        getters: {
          getPackageList: () => [
            {
              claimNames: ['name', 'Surname'],
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
      },
      TechnicalReqModule: {
        namespaced: true,
        state: {},
        getters: {
          getSingleTechnicalReq: jest.fn(),
          getTechnicalReq: jest.fn(),
          isLoading: jest.fn()
        },
        actions: {
          getSingleTechnicalReq: jest.fn(),
          addTechnicalReq: jest.fn(),
          loadTechnicalReqDetails: jest.fn()
        }
      },
      SharedModule: {
        namespaced: true,
        state: {},
        getters: {
          isRedirectFromSummaryPage: jest.fn(() => {
            return false;
          })
        },
        actions: {
          redirectFromSummaryPage: jest.fn()
        }
      }
    }
  });

  const mountFunction = (options: any) => {
    return mount(PackageSelect, {
      store: storeData,
      vuetify,
      localVue,
      router1,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options
    });
  };

  it('renders props when passed and redirect from summary page true', () => {
    const wrapper = mountFunction({
      propsData: {
        id: 2
      }
    });

    expect(wrapper.element).toMatchSnapshot();
  });
});

import { shallowMount, createLocalVue } from '@vue/test-utils';
import PackageSelect from '@/components/CreateApp/PackageSelect.vue';
import vuetify from 'vuetify';
import Vuex from 'vuex';

describe('PackageSelect.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);
    localVue.use(Vuex);
    const store = new Vuex.Store({
      modules: {
        PackageModule: {
          namespaced: true,
          state: {},
          getters: {
            getPackageList: () => jest.fn(),
            isLoggedin: jest.fn()
          },
          actions: { addPackagetoProject: jest.fn() }
        }
      }
    });
    wrapper = shallowMount(PackageSelect, {
      localVue,
      store
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});

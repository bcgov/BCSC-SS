import { shallowMount, createLocalVue } from '@vue/test-utils';
import App from '@/App.vue';
import vuetify from 'vuetify';

describe('App.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(App, {
      localVue,
      stubs: ['router-view'],
      mocks: { $route: { meta: { showVerticalMenu: false } } }
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});

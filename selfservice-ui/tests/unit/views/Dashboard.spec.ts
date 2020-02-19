import { shallowMount, createLocalVue } from '@vue/test-utils';
import Dashboard from '@/views/Dashboard.vue';
import vuetify from 'vuetify';

describe('Dashboard.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(Dashboard, {
      localVue
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});

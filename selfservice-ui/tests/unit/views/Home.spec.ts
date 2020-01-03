import { shallowMount, createLocalVue } from '@vue/test-utils';
import Home from '@/views/Home.vue';
import vuetify from 'vuetify';

describe('Home.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(Home, {
      localVue
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});

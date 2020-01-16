import { shallowMount, createLocalVue } from '@vue/test-utils';
import CreateApp from '@/views/CreateApp.vue';
import vuetify from 'vuetify';

describe('CreateApp.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(CreateApp, {
      localVue
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});

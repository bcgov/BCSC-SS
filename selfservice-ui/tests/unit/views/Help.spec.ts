import { shallowMount, createLocalVue } from '@vue/test-utils';
import Help from '@/views/Help.vue';
import vuetify from 'vuetify';

describe('Help.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(Help, {
      localVue
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});

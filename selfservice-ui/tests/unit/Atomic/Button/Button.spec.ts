import { shallowMount, createLocalVue } from '@vue/test-utils';
import Button from '@/Atomic/Button/Button.vue';
import vuetify from 'vuetify';

describe('Button.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);
    wrapper = shallowMount(Button, {
      localVue
    });
  });
  afterEach(() => {
    wrapper.destroy();
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});

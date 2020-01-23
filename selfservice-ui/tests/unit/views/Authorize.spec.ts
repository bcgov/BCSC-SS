import { shallowMount, createLocalVue } from '@vue/test-utils';
import Authorize from '@/views/Authorize.vue';
import vuetify from 'vuetify';

describe('Authorize.vue', () => {
  it('renders without crashing', () => {
    const localVue = createLocalVue();
    localVue.use(vuetify);
    const wrapper = shallowMount(Authorize, {
      localVue
    });
    expect(wrapper.element).toMatchSnapshot();
  });
});

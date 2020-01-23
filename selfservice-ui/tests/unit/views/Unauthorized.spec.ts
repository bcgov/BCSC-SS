import { shallowMount, createLocalVue } from '@vue/test-utils';
import Unauthorized from '@/views/Unauthorized.vue';
import vuetify from 'vuetify';

describe('Unauthorized.vue', () => {
  it('renders without crashing', () => {
    const localVue = createLocalVue();
    localVue.use(vuetify);
    const wrapper = shallowMount(Unauthorized, {
      localVue
    });

    expect(wrapper.element).toMatchSnapshot();
  });
});

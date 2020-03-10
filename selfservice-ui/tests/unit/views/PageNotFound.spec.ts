import { shallowMount, createLocalVue } from '@vue/test-utils';
import PageNotFound from '@/views/PageNotFound.vue';
import vuetify from 'vuetify';

describe('PageNotFound.vue', () => {
  it('renders without crashing', () => {
    const localVue = createLocalVue();
    localVue.use(vuetify);
    const wrapper = shallowMount(PageNotFound, {
      localVue
    });
    expect(wrapper.element).toMatchSnapshot();
  });
});

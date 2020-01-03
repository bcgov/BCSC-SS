import { shallowMount, createLocalVue } from '@vue/test-utils';
import Header from '@/components/Header/Header.vue';
import vuetify from 'vuetify';
import VueRouter from 'vue-router';

describe('Header.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);
    localVue.use(VueRouter);
    const router = new VueRouter();
    wrapper = shallowMount(Header, {
      localVue,
      router
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});

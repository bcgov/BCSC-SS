import { shallowMount, createLocalVue } from '@vue/test-utils';
import HelloWorld from '@/components/HelloWorld.vue';
import vuetify from 'vuetify';

describe('HelloWorld.vue', () => {
  it('renders props.msg when passed', () => {
    const msg = 'new message';
    const localVue = createLocalVue();
    localVue.use(vuetify);

    const wrapper = shallowMount(HelloWorld, {
      propsData: { msg },
      localVue
    });
    expect(wrapper.text()).toMatch(msg);
  });
});

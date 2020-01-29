import { mount, createLocalVue } from '@vue/test-utils';
import Input from '@/Atomic/Input/Input.vue';
import Vuetify from 'vuetify';

describe('Input.vue', () => {
  let wrapper: any;

  let vuetify: any;
  const localVue = createLocalVue();

  localVue.use(Vuetify);
  vuetify = new Vuetify();

  const mountFunction = (options: any) => {
    return mount(Input, {
      vuetify,
      localVue,
      ...options
    });
  };

  afterEach(() => {
    wrapper.destroy();
  });

  it('renders props when passed', () => {
    wrapper = mountFunction({
      propsData: {
        input: jest.fn(),
        value: 'test'
      }
    });
    expect(wrapper.element).toMatchSnapshot();
  });
  it('renders props when passed', async () => {
    wrapper = mountFunction({
      propsData: {
        input: jest.fn(),
        value: 'test'
      }
    });
    const inputElement = wrapper.find('input');
    inputElement.element.value = 'value';
    inputElement.trigger('input');

    await wrapper.vm.$nextTick();

    expect(wrapper.element).toMatchSnapshot();
  });
});

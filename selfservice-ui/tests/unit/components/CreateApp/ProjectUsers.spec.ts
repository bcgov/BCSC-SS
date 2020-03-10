import { shallowMount, createLocalVue } from '@vue/test-utils';
import vuetify from 'vuetify';
import ProjectUsers from '@/components/CreateApp/ProjectUsers.vue';
import validationRules from '@/config/validationRules';

describe('ProjectUsers.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(ProjectUsers, {
      localVue,
      propsData: {
        userDetails: { email: '', phone: '', firstName: '', lastName: '' },
        rules: validationRules
      }
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});

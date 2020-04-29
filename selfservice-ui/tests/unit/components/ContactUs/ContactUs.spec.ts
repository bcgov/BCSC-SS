import { mount } from '@vue/test-utils';
import ContactUs from '@/components/ContactUs/ContactUs.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
import Vue from 'vue';
let vuetify: any;
vuetify = new Vuetify();

describe('ContactUs.vue', () => {
  const store = new Vuex.Store({
    modules: {
      ContactUsModule: {
        namespaced: true,
        state: {},
        getters: {
          getChangeStatus: jest.fn(),
          isLoading: jest.fn(),
        },
        actions: {
          addContactUs: jest.fn(),
        },
      },
    },
  });

  const mountFunction = (options: any) => {
    return mount(ContactUs, {
      store,
      vuetify,
      sync: false,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options,
    });
  };

  it('renders props when passed with gettors', () => {
    const ContactUsPage = mountFunction({});
    expect(ContactUsPage.element).toMatchSnapshot();
  });

  // it('renders data on conact submit click ', async () => {
  //   const ContactUsPage = mountFunction({});
  //   const submitContactMessage = jest.fn();

  //   ContactUsPage.setData({
  //     contactDetails: {
  //       firstName: 'fname',
  //       lastName: 'lname',
  //       email: 'email@email.com',
  //       description: 'test',
  //     },
  //   });

  //   ContactUsPage.setData({
  //     valid: true,
  //   });

  //   await Vue.nextTick();
  //   const button = ContactUsPage.find('.btn-contact-us');
  //   ContactUsPage.vm.$on('action-btn:clicked', submitContactMessage);
  //   button.trigger('click');
  //   expect(ContactUsPage.element).toMatchSnapshot();
  // });
});

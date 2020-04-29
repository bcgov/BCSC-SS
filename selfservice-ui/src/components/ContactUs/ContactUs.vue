/** 
* 
ContactUs component 
*/

<template>
  <v-card class="mx-auto outer-card">
    <v-form ref="form" v-model="valid">
      <h1 class="bc-page-title-h1">{{ $t('contactUs.pagetitle') }}</h1>
      <div class="flex-grow-1"></div>

      <v-container>
        <v-row class="mx-4">
          <v-col cols="12" flat>
            <v-card flat>
              <div class="text-left" v-html="$t('contactUs.pageinfo')"></div>
            </v-card>
          </v-col>
          <v-col class="col-12" v-if="errorStatus || successStatus">
            <Alert
              type="error"
              v-if="errorStatus"
              class="alert-top text-left"
            >{{ $t('contactUs.errorMessage') }}</Alert>
            <Alert
              type="success"
              class="alert-top text-left"
              v-if="successStatus"
            >{{ $t('contactUs.successMessage') }}</Alert>
          </v-col>
          <v-col cols="8">
            <Input
              v-model="contactDetails.firstName"
              :label="$t('contactUs.firstName')"
              type="text"
              :rules="[rules.required,  rules.maxLength(500)]"
              data-test-id="input-firstname"
            />

            <Input
              v-model="contactDetails.lastName"
              :label="$t('contactUs.lastName')"
              type="text"
              :rules="[rules.required, rules.maxLength(500)]"
              data-test-id="input-lastname"
            />
            <Input
              v-model="contactDetails.email"
              :label="$t('contactUs.emailAddress')"
              type="text"
              :rules="[rules.required, rules.email, rules.maxLength(500)]"
              data-test-id="input-email"
            />
          </v-col>
          <v-col cols="12" flat>
            <v-card flat>
              <TextArea
                v-model="contactDetails.description"
                :label="$t('contactUs.description')"
                type="text"
                outlined
                rows="10"
                name="text-contact-us-description"
                id="text-contact-us-description"
                data-test-id="text-contact-us-description"
                :rules="[rules.required]"
              />
            </v-card>
          </v-col>
        </v-row>

        <v-col cols="12">
          <v-card flat>
            <v-divider></v-divider>
            <v-card-actions>
              <v-spacer></v-spacer>

              <Button
                :disabled="!valid"
                class="white--text btn-contact-us ml-6"
                depressed
                @click="submitContactMessage"
                name="btn-contact-us"
                data-test-id="btn-contact-us"
              >{{ $t('contactUs.btnSend') }}</Button>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-container>
    </v-form>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Watch, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import validationRules from '@/config/validationRules';

import Button from '@/Atomic/Button/Button.vue';
import TextArea from '@/Atomic/TextArea/TextArea.vue';
import Alert from '@/Atomic/Alert/Alert.vue';
import Input from '@/Atomic/Input/Input.vue';

import { contactDetailsSample } from '@/store/modules/ContactUs/defaults';

const ContactUsModule = namespace('ContactUsModule');

@Component({
  components: {
    Button,
    TextArea,
    Alert,
    Input
  }
})
export default class ContactUs extends Vue {
  @Prop({ default: 0 })
  public id!: number;

  @ContactUsModule.Action('addContactUs')
  public addContactUs!: any;
  @ContactUsModule.Getter('isLoading')
  public isLoading!: boolean;
  @ContactUsModule.Getter('getChangeStatus')
  public getChangeStatus!: boolean;

  private rules = validationRules;

  private contactDetails: any;
  private valid: boolean = false;
  private successStatus: boolean = false;
  private errorStatus: boolean = false;

  public constructor() {
    super();
    this.contactDetails = contactDetailsSample();
  }

  @Watch('getChangeStatus')
  private ongetChangeStatusChanged(val: any) {
    const { successStatus, errorStatus } = val;
    this.successStatus = successStatus;
    this.errorStatus = errorStatus;
    if (successStatus) {
      (this.$refs.form as Vue & {
        reset: () => any;
      }).reset();
      this.$vuetify.goTo(0, {
        duration: 1000,
        easing: 'easeInOutCubic'
      });
    }
  }

  private submitContactMessage() {
    this.addContactUs({
      contactDetails: this.contactDetails
    });
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
</style>

/** * Create or Update Profile of app */

<template>
  <v-card class="mx-auto card-width">
    <Alert type="error" v-if="errorStatus">Something went wrong...</Alert>
    <v-toolbar flat class="bc-subtitle" dark v-if="!errorStatus">
      <v-toolbar-title>
        {{ $t(isComplete ? 'profile.pageCompleteTitle' : 'profile.pageTitle') }}
      </v-toolbar-title>
      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-divider></v-divider>
    <v-form ref="form" v-model="valid" v-if="!errorStatus">
      <v-container>
        <v-row class="ma-5">
          <v-col cols="12" md="12">
            <Alert
              type="error"
              dense
              outlined
              class="text-left"
              v-if="profileErrorStatus"
            >
              <span v-html="$t('profile.errorMessageDomain')"></span>
            </Alert>
            <v-card-subtitle
              v-if="isComplete"
              class="text-left padding-0 bc-padding-left-0"
              v-html="
                $t(
                  provider == 'idir'
                    ? 'profile.titlePageInfoIDIR'
                    : 'profile.titlePageInfoBCSC'
                )
              "
            ></v-card-subtitle>
            <v-card-subtitle
              v-else
              class="text-left padding-0 bc-padding-left-0"
              v-html="$t('profile.titlePageCompleteInfo')"
            ></v-card-subtitle>
            <v-card-title class="text-left bc-padding-left-0">
              {{ userProfile.firstName }}
              {{ userProfile.lastName }}
            </v-card-title>
            <Input
              v-model="email"
              :label="$t('profile.labelEmail')"
              type="text"
              :rules="[
                rules.required,
                rules.email,
                rules.length(2),
                rules.maxLength(250),
              ]"
              data-test-id="input-profile-email"
              v-if="filedsToShow.email"
            />
            <Input
              v-model="phone"
              :label="$t('profile.labelPhone')"
              type="text"
              :rules="[rules.required, rules.length(9), rules.maxLength(15)]"
              v-if="filedsToShow.phone"
              data-test-id="input-profile-phone"
            />
          </v-col>
          <v-col cols="12">
            <v-card flat>
              <v-divider></v-divider>
              <v-card-actions>
                <v-spacer></v-spacer>
                <Button
                  :disabled="!valid"
                  class="white--text btn-profile-update"
                  depressed
                  @click="toggleDisclaimer()"
                  @keyup.enter="toggleDisclaimer()"
                  data-test-id="btn-profile-update"
                >
                  {{
                    $t(
                      isComplete
                        ? 'profile.btnContinue'
                        : 'profile.btnSaveChanges'
                    )
                  }}
                </Button>
              </v-card-actions>
            </v-card>
          </v-col>
          <v-col class="text-center">
            <v-dialog
              v-model="dialog"
              persistent
              width="90%"
              class="text-left overflow-y-auto"
            >
              <v-card class="pa-8">
                <!-- <h1 class="text-left pa-5 ml-8">
                  {{ $t('profile.titleTerms') }}
                </h1> -->
                <p class="text-left pl-5 ml-8">
                  {{ $t('profile.termsAccept') }}
                </p>
                <v-divider></v-divider>
                <v-card-text
                  class="text-left terms-content pa-0"
                  id="scroll-target"
                  ref="termsDiv"
                >
                  <TermsAndConditions :onIntersect="onIntersect" />
                  <div
                    v-intersect="{
                      handler: onIntersect,
                      options: {
                        threshold: [0, 0.5, 1.0],
                      },
                    }"
                  ></div>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions class="terms-actions">
                  <v-spacer></v-spacer>
                  <Button
                    @click="toggleDisclaimer()"
                    aria-label="Back Button"
                    secondary
                    data-test-id="btn-cancel-terms-profile"
                    >{{ $t('profile.btnCancel') }}</Button
                  >
                  <Button
                    :disabled="!buttonEnable"
                    class="white--text btn-submit-terms-profile ml-6"
                    depressed
                    @click="createOrUpdateProfile"
                    data-test-id="btn-submit-terms-profile"
                    >{{ $t('profile.btnAgree') }}</Button
                  >
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import 'intersection-observer';
import { Getter, namespace, Action } from 'vuex-class';
import Input from '@/Atomic/Input/Input.vue';
import Button from '@/Atomic/Button/Button.vue';
import Alert from '@/Atomic/Alert/Alert.vue';
import TermsAndConditions from '@/components/Profile/TermsAndConditions.vue';

import validationRules from '@/config/validationRules';

const KeyCloakModule = namespace('KeyCloakModule');

@Component({ components: { Input, Button, Alert, TermsAndConditions } })
export default class Dashboard extends Vue {
  @Prop({ default: '' })
  public step!: string;
  private isComplete = this.step === 'complete';

  @KeyCloakModule.Getter('filedsToShow')
  private filedsToShow!: any;
  @KeyCloakModule.Getter('provider')
  private provider!: string;
  @KeyCloakModule.Action('updateProfile')
  private updateProfile!: any;
  @KeyCloakModule.Getter('userProfile') private userProfile!: any;
  @KeyCloakModule.Getter('errorStatus')
  private errorStatus!: any;
  @KeyCloakModule.Getter('profileErrorStatus')
  private profileErrorStatus!: boolean;

  private valid: boolean = false;
  private dialog: boolean = false;

  /* istanbul ignore next */
  private rules = validationRules;
  private email: string = '';
  private phone: string = '';
  private buttonEnable: boolean = false;

  @Watch('userProfile')
  private onUserProfileChanged(val: any) {
    this.userDetails(val);
  }

  private createOrUpdateProfile() {
    const profile = { email: this.email, phone: this.phone };
    this.updateProfile(profile);
    this.toggleDisclaimer();
  }
  private userDetails(val: any) {
    this.email = val.email;
    this.phone = val.phone;
  }
  private toggleDisclaimer() {
    this.dialog = !this.dialog;
  }
  private onIntersect(entries: any, observer: any) {
    this.buttonEnable = entries[0].intersectionRatio >= 0.5;
  }

  private mounted() {
    this.userDetails(this.userProfile);
    if ((!'IntersectionObserver' as any) in window) {
      this.buttonEnable = true;
    }
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.card-width {
  max-width: 80%;
  @include lg {
    max-width: 50%;
  }
}
.terms-content {
  max-height: 60vh;
  overflow-y: auto;
}
</style>

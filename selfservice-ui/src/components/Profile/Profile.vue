/** * Create or Update Profile of app */

<template>
  <v-card class="mx-auto card-width">
    <v-alert type="error" v-if="errorStatus">Something went wrong...</v-alert>
    <v-toolbar flat class="bc-subtitle" dark v-if="!errorStatus">
      <v-toolbar-title>{{ $t(isComplete ? 'profile.pageCompleteTitle' : 'profile.pageTitle') }}</v-toolbar-title>
      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-divider></v-divider>
    <v-form ref="form" v-model="form" v-if="!errorStatus">
      <v-container>
        <v-row class="ma-5">
          <v-col cols="12" md="12">
            <v-alert
              type="error"
              dense
              outlined
              class="text-left"
              v-if="profileErrorStatus"
              v-html="$t('profile.errorMessageDomain')"
            ></v-alert>
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
                rules.maxLength(250)
              ]"
              v-if="filedsToShow.email"
            />
            <Input
              v-model="phone"
              :label="$t('profile.labelPhone')"
              type="text"
              :rules="[rules.required, rules.length(9), rules.maxLength(15)]"
              v-if="filedsToShow.phone"
            />
          </v-col>
          <v-col cols="12">
            <v-card flat>
              <v-divider></v-divider>
              <v-card-actions>
                <v-spacer></v-spacer>
                <Button
                  :disabled="!form"
                  class="white--text"
                  depressed
                  @click="createOrUpdateProfile"
                  @keyup.enter="createOrUpdateProfile"
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
        </v-row>
      </v-container>
    </v-form>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import Input from '@/Atomic/Input/Input.vue';
import Button from '@/Atomic/Button/Button.vue';
import validationRules from '@/config/validationRules';

const KeyCloakModule = namespace('KeyCloakModule');

@Component({ components: { Input, Button } })
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

  private form: boolean = false;

  /* istanbul ignore next */
  private rules = validationRules;
  private email: string = '';
  private phone: string = '';

  @Watch('userProfile')
  private onUserProfileChanged(val: any) {
    this.email = val.email;
    this.phone = val.phone;
  }

  private createOrUpdateProfile() {
    const profile = { email: this.email, phone: this.phone };
    this.updateProfile(profile);
  }

  private mounted() {
    this.onUserProfileChanged(this.userProfile);
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
</style>

/** * Dashboard of app */

<template>
  <v-card class="mx-auto" style="max-width: 80%;">
    <v-toolbar flat class="bc-subtitle" dark>
      <v-toolbar-title>{{ $t('profile.pagetitle') }}</v-toolbar-title>
      <div class="flex-grow-1"></div>

      <div class="flex-grow-1"></div>

      <v-btn
        class="ma-2"
        fab
        dark
        color="#fba30e"
        @click="$router.push(`/project/info`)"
      >
        <v-icon dark large>mdi-plus</v-icon>
      </v-btn>
    </v-toolbar>
    <v-divider></v-divider>
    <v-form ref="form" v-model="form">
      <v-container>
        <v-row class="ma-5">
          <v-col cols="12" md="12">
            <v-card-subtitle
              class="text-left padding-0"
              v-html="$t('profile.titlePageInfo')"
            ></v-card-subtitle>
            <Input
              v-model="email"
              counter="100"
              :label="$t('profile.labelEmail')"
              type="text"
              :rules="[rules.required, rules.length(2), rules.maxLength(100)]"
              v-if="filedsToShow.email"
            />
            <Input
              v-model="phone"
              counter="100"
              :label="$t('profile.labelPhone')"
              type="text"
              :rules="[rules.required, rules.length(2), rules.maxLength(100)]"
              v-if="filedsToShow.phone"
            />
          </v-col>
          <v-col cols="12">
            <v-card flat>
              <v-divider></v-divider>
              <v-card-actions>
                <!-- <v-btn text @click="$refs.form.reset()">Clear</v-btn> -->
                <v-spacer></v-spacer>
                <Button
                  :disabled="!form"
                  class="white--text"
                  color="indigo accent-4"
                  depressed
                  @click="completeProfile"
                  @keyup.enter="completeProfile"
                  >{{ $t('profile.btnContinue') }}</Button
                >
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import Input from '@/Atomic/Input/Input.vue';
import Button from '@/Atomic/Button/Button.vue';
import validationRules from '@/config/validationRules';

const KeyCloakModule = namespace('KeyCloakModule');

@Component({ components: { Input, Button } })
export default class Dashboard extends Vue {
  @KeyCloakModule.Getter('filedsToShow')
  public filedsToShow!: any;
  @KeyCloakModule.Action('updateProfile')
  public updateProfile!: any;
  @KeyCloakModule.Action('errorStatus')
  public errorStatus!: any;

  private form: boolean = false;

  /* istanbul ignore next */
  private rules = validationRules;
  private email: string = '';
  private phone: string = '';

  // private mounted() {
  //   this.loadProjectInfo();
  // }
  private completeProfile() {
    const profile = { email: this.email, phone: this.phone };
    this.updateProfile(profile);
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
</style>

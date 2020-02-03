/** * CreateApp of app */

<template>
  <v-card class="v-form pa-8 pt-6 ma-3">
    <v-card-title class="headline padding-0">{{ title }}</v-card-title>
    <v-card-subtitle class="text-left padding-0">Tell us about your {{ title }}</v-card-subtitle>
    <Input
      v-model="userDetails.firstName"
      label="First Name"
      :rules="[rules.required, rules.length(2), rules.maxLength(250)]"
      type="text"
    />
    <Input
      v-model="userDetails.lastName"
      label="Last Name"
      :rules="[rules.required, rules.length(2), rules.maxLength(250)]"
      type="text"
    />
    <Input
      v-model="userDetails.email"
      label="Work email"
      :rules="[rules.required, rules.email, rules.maxLength(250)]"
      type="text"
    />
    <Input
      v-model="userDetails.phone"
      label="Phone"
      :rules="[rules.required, rules.maxLength(15)]"
      type="text"
    />
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';

import { ProjectUserModel, ProjectInfoModel } from '@/models/ProjectInfoModel';
import Input from '@/Atomic/Input/Input.vue';

@Component({
  components: {
    Input
  }
})
export default class ProjectUsers extends Vue {
  private e6: number = 0;
  @Prop({
    default: { email: '', phone: '', firstName: '', lastName: '' }
  })
  private userDetails!: ProjectUserModel;
  @Prop({
    default: ''
  })
  private title!: string;
  @Prop({})
  private rules!: any;
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.padding-0 {
  padding-left: 0px !important;
}
</style>

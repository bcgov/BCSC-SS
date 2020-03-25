/** * Dashboard of app */

<template>
  <v-card class="mx-auto" style="max-width: 80%;">
    <v-toolbar flat class="bc-subtitle" dark>
      <v-toolbar-title>{{ $t('projectContainer.pagetitle') }}</v-toolbar-title>
      <div class="flex-grow-1"></div>

      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-divider></v-divider>
    <v-container>
      <v-row class="ma-5">
        <v-col>
          <v-tabs slider-color="d-none">
            <v-tab class="font-weight-bold">{{ $t('projectContainer.titleDevSummary') }}</v-tab>
            <v-tab class="font-weight-bold">{{ $t('projectContainer.titleTeamRoles') }}</v-tab>
            <v-tab class="font-weight-bold">{{ $t('projectContainer.titleLiveAccessReq') }}</v-tab>
            <v-tab class="font-weight-bold">{{ $t('projectContainer.titlePrivacy') }}</v-tab>
            <v-tab-item class="custom-tabs-items">
              <v-card flat>
                <v-card-text>
                  <ProjectSummary :id="id" />
                </v-card-text>
              </v-card>
            </v-tab-item>
            <v-tab-item class="custom-tabs-items">
              <v-card flat>
                <v-card-text>content</v-card-text>
              </v-card>
            </v-tab-item>
            <v-tab-item class="custom-tabs-items">
              <v-card flat>
                <v-card-text>
                  <p>content</p>
                </v-card-text>
              </v-card>
            </v-tab-item>
          </v-tabs>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import ProjectSummary from '@/components/CreateApp/ProjectSummary.vue';

@Component({
  components: {
    ProjectSummary
  }
})
export default class ProjectContainer extends Vue {
  @Prop({ default: 0 })
  public id!: number;
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.custom-tabs-items {
  border: 1px solid $gray5;
}
.v-tab {
  color: $BCgovBlue5 !important;
}
.v-tab--active {
  border: 1px solid $gray5;
  background-color: $BCgovGold5;
  color: $BCgovWhite !important;
}
</style>

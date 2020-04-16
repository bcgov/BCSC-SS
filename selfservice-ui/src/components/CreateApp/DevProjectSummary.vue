/** * DevProjectSummary component */

<template>
  <v-card class="mx-auto outer-card">
    <v-toolbar flat class="bc-subtitle padding-0" dark>
      <v-btn icon @click="goBack()" :aria-label="$t('summaryPage.goBack')">
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <v-toolbar-title>{{ $t('summaryPage.pagetitle') }}</v-toolbar-title>
      <div class="flex-grow-1"></div>

      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-container>
      <v-row>
        <v-col cols="8" flat>
          <v-card flat>
            <v-list-item-content
              class="text-left padding-0"
              v-html="$t('summaryPage.subTitle')"
            ></v-list-item-content>
          </v-card>
        </v-col>
        <v-col cols="4"><ProjectActions :id="id" /> </v-col>
        <ProjectSummary :id="id" />
      </v-row>
    </v-container>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Watch, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import ProjectSummary from '@/components/CreateApp/ProjectSummary.vue';
import ProjectActions from '@/components/ProjectActions/ProjectActions.vue';

const SharedModule = namespace('SharedModule');
const ProjectInfoModule = namespace('ProjectInfoModule');

@Component({
  components: {
    ProjectSummary,
    ProjectActions,
  },
})
export default class DevProjectSummary extends Vue {
  @Prop({ default: 0 })
  public id!: number;

  @SharedModule.Action('redirectFromSummaryPage')
  public redirectFromSummaryPage!: any;
  @ProjectInfoModule.Getter('getSingleProjectInfo')
  public getSingleProjectInfo!: any;

  private projectId: number = this.id || 0;

  private mounted() {
    this.redirectFromSummaryPage(true);
  }

  private goBack() {
    this.redirectFromSummaryPage(false);
    this.$router.push(`/project/${this.projectId}/test-account`);
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.active-bg {
  background-color: $BCgovActiveBg;
}
.card-width {
  max-width: 110px;
}
.text-center {
  text-align: center !important;
}
</style>

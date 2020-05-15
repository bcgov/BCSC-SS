/** * ProjectInfoSummary component */

<template>
  <v-card>
    <Loading v-if="isLoading" />
    <v-toolbar dense class="bc-subtitle-2" dark v-else>
      <v-card-title>
        {{ $t('summaryPage.projectInfoTitle') }}
        <v-spacer></v-spacer>
        <span
          @click="$router.push(`/project/${id}/info`)"
          class="edit-wrapper"
          :aria-label="$t('global.edit')"
        >
          <v-icon small class="ml-3">mdi-pencil</v-icon>
          <span class="edit-label">{{ $t('global.edit') }}</span>
        </span>
      </v-card-title>
    </v-toolbar>

    <v-list dense class="px-5" v-if="!isLoading">
      <v-list-item>
        <v-list-item-content class="pr-30">
          {{ $t('summaryPage.labelOrganizationName') }}
          <span
            class="small-hint pad-50"
            v-html="$t('summaryPage.OrganizationNameHint')"
          ></span>
        </v-list-item-content>
        <v-list-item-content class="align-end">
          <div>
            <v-icon small class="mr-1">mdi-office-building</v-icon>
            {{ projectInfo && projectInfo.organizationName }}
          </div>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <v-list-item>
        <v-list-item-content class="pr-30">
          {{ $t('summaryPage.labelProjectTitle') }}
          <span
            class="small-hint pad-50"
            v-html="$t('summaryPage.projectNameHint')"
          ></span>
        </v-list-item-content>
        <v-list-item-content class="align-end">
          <div>
            <v-icon small class="mr-1">mdi-apps</v-icon>
            {{ projectInfo.projectName }}
          </div>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <v-list-item>
        <v-list-item-content class="align-self-start pr-30">
          {{ $t('summaryPage.labelProjectDescription') }}
          <span
            class="small-hint pad-50"
            v-html="$t('summaryPage.labelProjectDescriptionHint')"
          ></span>
        </v-list-item-content>
        <v-list-item-content class="align-end">
          <div class="break-word-all">
            <v-icon small class="mr-1">mdi-apps</v-icon>
            {{ projectInfo.description }}
          </div>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import Loading from '@/Atomic/Loading/Loading.vue';

const ProjectInfoModule = namespace('ProjectInfoModule');

@Component({
  components: { Loading }
})
export default class ProjectInfoSummary extends Vue {
  @Prop({ default: 0 })
  public id!: number;

  @ProjectInfoModule.Getter('getSingleProjectInfo')
  public projectInfo!: any;
  @ProjectInfoModule.Action('loadSingleProjectInfo')
  public loadSingleProjectInfo!: any;

  @ProjectInfoModule.Getter('getFinalProjectSubmissionStatus')
  public getFinalProjectSubmissionStatus!: any;

  @ProjectInfoModule.Action('clearSubmitProjectStatus')
  public clearSubmitProjectStatus!: any;

  private isLoading: boolean = true;

  @Watch('projectInfo')
  private ongetprojectInfoChanged(val: any) {
    this.isLoading = false;
  }

  private mounted() {
    this.isLoading = true;
    this.loadSingleProjectInfo(this.id);
  }
}
</script>
<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
</style>

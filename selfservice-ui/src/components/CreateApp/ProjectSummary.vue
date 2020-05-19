/** * ProjectSummary component */

<template>
  <div>
    <Loading v-if="isLoading" />
    <v-row v-else>
      <Alert
        type="success"
        class="alert-top text-left alert-msg"
        dense
        outlined
        v-if="isCreated"
        data-test-id="alert-add-sucess-project-summary"
      >{{ $t('summaryPage.createSuccessMessage') }}</Alert>

      <Alert
        type="success"
        class="alert-top text-left alert-msg"
        dense
        outlined
        v-if="isUpdated"
        data-test-id="alert-update-sucess-project-summary"
      >{{ $t('summaryPage.updateSuccessMessage') }}</Alert>
      <v-col cols="12" flat>
        <v-list-item-content class="text-left padding-0" v-html="$t('summaryPage.subTitle')"></v-list-item-content>
      </v-col>
      <v-col cols="12" flat>
        <ClientID
          :id="projectId"
          :showTestAccountWarning="showTestAccountWarning"
          :key="componentKey"
        />
      </v-col>
      <v-col cols="12" flat>
        <ProjectInfoSummary :id="projectId" />
      </v-col>
      <v-col cols="12" flat>
        <TeamSummary :id="projectId" :team="team" :isTeamAvailable="isTeamAvailable" />
      </v-col>
      <v-col cols="12" flat>
        <TechnicalReqSummary
          :id="projectId"
          :technicalReq="technicalReq"
          :isTechnicalInfoAvailable="isTechnicalInfoAvailable"
          :showCannotSubmitError="showCannotSubmitError"
        />
      </v-col>

      <v-col cols="12" flat>
        <PackageSelectSummary
          :id="projectId"
          :technicalReq="technicalReq"
          :getDataScopeClasses="getDataScopeClasses"
        />
      </v-col>
      <v-col cols="12" flat></v-col>

      <v-col cols="12" flat>
        <TestAccountSummary
          :technicalReq="technicalReq"
          :projectId="projectId"
          :class="getDataScopeClasses('noOfTestAccount')"
        />
      </v-col>
      <v-col cols="12">
        <Alert
          type="error"
          dense
          outlined
          class="text-left"
          v-if="showCannotSubmitError"
        >{{ $t('summaryPage.cantSubmitErrorMessage') }}</Alert>
        <Alert
          type="error"
          dense
          outlined
          class="text-left"
          v-if="showSystemError"
        >{{ $t('summaryPage.systemError') }}</Alert>
      </v-col>
      <v-col cols="12">
        <v-card flat class="mt-1">
          <v-divider></v-divider>
          <v-card-actions class="mt-2 py-2 px-0">
            <v-spacer></v-spacer>
            <Button
              @click="goBack()"
              @keyup.enter="goBack()"
              :aria-label="$t('summaryPage.goBack')"
              secondary
              class="back-btn"
              v-if="isDraft"
              data-test-id="btn-cancel-summary"
            >{{ $t('summaryPage.goBack') }}</Button>
            <Button
              :loading="isLoading"
              class="white--text submit-package ml-6"
              depressed
              data-test-id="btn-submit-summary"
              @click="submitFinalRequest"
              @keyup.enter="submitFinalRequest"
            >
              {{
              isDraft
              ? $t('summaryPage.submitRequest')
              : $t('summaryPage.commitChanges')
              }}
            </Button>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>
<script lang="ts">
import { Component, Vue, Watch, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import Button from '@/Atomic/Button/Button.vue';
import TextArea from '@/Atomic/TextArea/TextArea.vue';
import Loading from '@/Atomic/Loading/Loading.vue';
import Alert from '@/Atomic/Alert/Alert.vue';

import ClientID from '@/components/CreateApp/ClientID.vue';
import TestAccountSummary from '@/components/CreateApp/TestAccountSummary.vue';
import ProjectInfoSummary from '@/components/CreateApp/ProjectInfoSummary.vue';
import TeamSummary from '@/components/CreateApp/TeamSummary.vue';
import TechnicalReqSummary from '@/components/CreateApp/TechnicalReqSummary.vue';
import PackageSelectSummary from '@/components/CreateApp/PackageSelectSummary.vue';
import { projectStatus, projectRoles } from '@/constants/enums';

const ProjectInfoModule = namespace('ProjectInfoModule');
const TeamModule = namespace('TeamRolesModule');
const TechnicalReqModule = namespace('TechnicalReqModule');
const SharedModule = namespace('SharedModule');

@Component({
  components: {
    Button,
    TextArea,
    Loading,
    ClientID,
    TestAccountSummary,
    ProjectInfoSummary,
    TeamSummary,
    TechnicalReqSummary,
    PackageSelectSummary,
    Alert
  }
})
export default class ProjectSummary extends Vue {
  @Prop({ default: 0 })
  public id!: number;

  @ProjectInfoModule.Action('clearSubmitProjectStatus')
  public clearSubmitProjectStatus!: any;

  @TeamModule.Getter('getTeamList')
  public team!: any;
  @TeamModule.Action('loadTeam')
  public loadTeam!: any;

  @TechnicalReqModule.Getter('getTechnicalReq')
  public technicalReq!: any;
  @TechnicalReqModule.Action('loadTechnicalReqDetails')
  public loadTechnicalReqDetails!: any;

  @ProjectInfoModule.Action('submitProject') public submitProject!: any;
  @SharedModule.Action('redirectFromSummaryPage')
  public redirectFromSummaryPage!: any;
  @SharedModule.Getter('isRedirectFromSummaryPage')
  public isRedirectFromSummaryPage!: boolean;

  @ProjectInfoModule.Getter('getSingleProjectInfo')
  public getSingleProjectInfo!: any;
  @ProjectInfoModule.Getter('getFinalProjectSubmissionStatus')
  public getFinalProjectSubmissionStatus!: any;

  private isLoading: boolean = true;
  private projectId: number = this.id || 0;
  private isTeamAvailable: boolean = false;
  private isTechnicalInfoAvailable: boolean = false;
  private canSubmit: boolean = false;
  private showCannotSubmitError: boolean = false;
  private showTestAccountWarning: boolean = false;
  private showSystemError: boolean = false;
  private componentKey: number = 0;
  private isDraft: boolean = false;
  private isCreated: boolean = false;
  private isUpdated: boolean = false;

  private selectedPackage: any = {
    claimNames: '',
    description: '',
    id: '',
    packageName: ''
  };

  @Watch('getFinalProjectSubmissionStatus')
  private ongetFinalProjectSubmissionStatusChanged(val: any) {
    const {
      finalErrorStatus,
      finalSuccessStatus,
      testAccountSuccess,
      isCreated,
      isUpdated
    } = val;
    if (finalSuccessStatus) {
      this.isCreated = isCreated;
      this.isUpdated = isUpdated;
      this.loadFullData();
      this.$vuetify.goTo(0, {
        duration: 1000,
        easing: 'easeInOutCubic'
      });
      this.showTestAccountWarning = !testAccountSuccess;
    } else if (finalErrorStatus) {
      this.showSystemError = true;
    }
    this.clearSubmitProjectStatus();
  }

  @Watch('team')
  private onTeamChanged(val: any) {
    this.setCanSubmit();
  }

  @Watch('technicalReq')
  private ongetTechnicalReqInfoChanged(val: any) {
    this.setCanSubmit();
  }

  @Watch('getSingleProjectInfo')
  private ongetSingleProjectInfoChanged(val: any) {
    if (val) {
      this.isDraft = val.statusId === projectStatus.draft;
      if (
        this.isRedirectFromSummaryPage &&
        val.statusId === projectStatus.dev
      ) {
        this.scrollToBottom();
      }
      this.redirectFromSummaryPage(true);
    }
  }

  private setCanSubmit() {
    this.isLoading = false;
    this.isTeamAvailable = this.team && this.team.length > 0;
    this.isTechnicalInfoAvailable =
      this.technicalReq && this.technicalReq.id ? true : false;
    this.canSubmit =
      this.technicalReq &&
      this.technicalReq.id &&
      this.technicalReq.scopePackageId &&
      this.technicalReq.noOfTestAccount &&
      this.team.length > 0
        ? true
        : false;
  }

  private submitFinalRequest() {
    if (this.canSubmit) {
      this.showCannotSubmitError = false;
      this.submitProject({ projectId: this.projectId });
    } else {
      this.showCannotSubmitError = true;
    }
  }

  private getDataScopeClasses(field: string) {
    let allowedClass = '';
    if (!this.isTechnicalInfoAvailable) {
      allowedClass += 'bc-disabled-section';
    }
    if (
      field &&
      (!this.technicalReq[field] || this.technicalReq[field] === null) &&
      this.showCannotSubmitError
    ) {
      allowedClass += ' red-border';
    }
    return allowedClass;
  }

  private mounted() {
    this.loadFullData();
  }

  private scrollToBottom() {
    this.$vuetify.goTo(document.body.scrollHeight, {
      duration: 1000,
      easing: 'easeInOutCubic'
    });
  }

  private loadFullData() {
    this.showSystemError = false;
    this.loadTeam(this.id);
    this.loadTechnicalReqDetails(this.id);

    this.componentKey = this.componentKey + 1;
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
.alert-msg {
  width: 100%;
  margin: 10px 15px;
}
</style>

/** * TestAccountRequest component */

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
      <Loading v-if="isLoading" />
      <v-row class="ma-5" v-else>
        <v-col cols="12" flat>
          <v-card flat>
            <v-list-item-content class="text-left padding-0" v-html="$t('summaryPage.subTitle')"></v-list-item-content>
          </v-card>
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
          <v-alert
            type="error"
            dense
            outlined
            class="text-left"
            v-if="showCannotSubmitError"
          >{{$t('summaryPage.cantSubmitErrorMessage')}}</v-alert>
          <v-alert
            type="error"
            dense
            outlined
            class="text-left"
            v-if="showSystemError"
          >{{$t('summaryPage.systemError')}}</v-alert>
        </v-col>
        <v-col cols="12">
          <v-card flat class="mt-1">
            <v-divider></v-divider>
            <v-card-actions class="mt-2 py-2 px-0">
              <v-spacer></v-spacer>
              <Button
                @click="goBack()"
                :aria-label="$t('summaryPage.goBack')"
                secondary
                class="back-btn"
              >{{ $t('summaryPage.goBack') }}</Button>
              <Button
                :loading="isLoading"
                class="white--text submit-package ml-6"
                depressed
                @click="showDisclimer"
              >{{ $t('summaryPage.submitRequest') }}</Button>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <v-divider></v-divider>
    <div class="text-center">
      <v-dialog v-model="dialog" persistent width="70%" class="text-left">
        <v-card>
          <v-card-title class="bc-subtitle padding-0" primary-title>
            {{
            $t('summaryPage.disclaimerTitle')
            }}
          </v-card-title>

          <v-card-text class="text-left">
            <div v-html="$t('summaryPage.disclaimerContent')"></div>
          </v-card-text>

          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <Button
              @click="dialog = false"
              aria-label="Back Button"
              secondary
            >{{ $t('summaryPage.btnAgreeBack') }}</Button>
            <Button
              class="white--text submit-package ml-6"
              depressed
              @click="submitFinalRequest"
            >{{ $t('summaryPage.btnAgree') }}</Button>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Watch, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import { ProjectUserModel } from '@/models/ProjectInfoModel';
import Button from '@/Atomic/Button/Button.vue';
import TextArea from '@/Atomic/TextArea/TextArea.vue';
import Loading from '@/Atomic/Loading/Loading.vue';
import ClientID from '@/components/CreateApp/ClientID.vue';
import TestAccountSummary from '@/components/CreateApp/TestAccountSummary.vue';
import ProjectInfoSummary from '@/components/CreateApp/ProjectInfoSummary.vue';
import TechnicalReqSummary from '@/components/CreateApp/TechnicalReqSummary.vue';
import PackageSelectSummary from '@/components/CreateApp/PackageSelectSummary.vue';

const TechnicalReqModule = namespace('TechnicalReqModule');
const ProjectInfoModule = namespace('ProjectInfoModule');
// const PackageAndTestModule = namespace('PackageAndTestModule');
const SharedModule = namespace('SharedModule');

@Component({
  components: {
    Button,
    TextArea,
    Loading,
    ClientID,
    TestAccountSummary,
    ProjectInfoSummary,
    TechnicalReqSummary,
    PackageSelectSummary
  }
})
export default class TestAccountRequest extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  // @ProjectInfoModule.Getter('getSingleProjectInfo')
  // public projectInfo!: any;
  // @ProjectInfoModule.Action('loadSingleProjectInfo')
  // public loadSingleProjectInfo!: any;

  // @ProjectInfoModule.Getter('getFinalProjectSubmissionStatus')
  // public getFinalProjectSubmissionStatus!: any;

  @ProjectInfoModule.Action('clearSubmitProjectStatus')
  public clearSubmitProjectStatus!: any;

  @TechnicalReqModule.Getter('getTechnicalReq')
  public technicalReq!: any;
  @TechnicalReqModule.Action('loadTechnicalReqDetails')
  public loadTechnicalReqDetails!: any;

  // @PackageAndTestModule.Action('loadPackage') public loadPackage!: any;
  // @PackageAndTestModule.Getter('getPackageList') public getPackageList!: [];
  @ProjectInfoModule.Action('submitProject') public submitProject!: any;
  @SharedModule.Action('redirectFromSummaryPage')
  public redirectFromSummaryPage!: any;

  private isLoading: boolean = true;
  private projectId: number = this.id || 0;
  private dialog: boolean = false;
  private isTechnicalInfoAvailable: boolean = false;
  private canSubmit: boolean = false;
  private showCannotSubmitError: boolean = false;
  private showTestAccountWarning: boolean = false;
  private showSystemError: boolean = false;
  private componentKey: number = 0;

  private selectedPackage: any = {
    claimNames: '',
    description: '',
    id: '',
    packageName: ''
  };

  @Watch('getFinalProjectSubmissionStatus')
  private ongetFinalProjectSubmissionStatusChanged(val: any) {
    const { finalErrorStatus, finalSuccessStatus, testAccountSuccess } = val;
    if (finalSuccessStatus) {
      this.hideDisclimer();
      this.loadFullData();
      this.$vuetify.goTo(0, {
        duration: 1000,
        easing: 'easeInOutCubic'
      });
      this.showTestAccountWarning = !testAccountSuccess;
    } else if (finalErrorStatus) {
      this.hideDisclimer();
      this.showSystemError = true;
    }
    this.clearSubmitProjectStatus();
  }

  @Watch('technicalReq')
  private ongetTechnicalReqInfoChanged(val: any) {
    this.isLoading = false;
    this.isTechnicalInfoAvailable = val && val.id ? true : false;
    this.canSubmit =
      val && val.id && val.scopePackageId && val.noOfTestAccount ? true : false;
  }

  private hideDisclimer() {
    this.dialog = false;
  }

  private showDisclimer() {
    if (this.canSubmit) {
      this.dialog = true;
      this.showCannotSubmitError = false;
    } else {
      this.dialog = false;
      this.showCannotSubmitError = true;
    }
  }
  private submitFinalRequest() {
    this.submitProject({ projectId: this.projectId });
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

  private loadFullData() {
    this.showSystemError = false;

    this.loadTechnicalReqDetails(this.id);
    this.redirectFromSummaryPage(true);

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
</style>

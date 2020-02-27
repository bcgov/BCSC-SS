/** * TestAccountRequest component */

<template>
  <v-card class="mx-auto" style="max-width: 80%;">
    <v-toolbar flat class="bc-subtitle padding-0" dark>
      <v-btn
        icon
        @click="$router.push(`/project/${projectId}/test-account/`)"
        aria-label="Back Button"
      >
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <v-toolbar-title>{{ $t('summaryPage.pagetitle') }}</v-toolbar-title>
      <div class="flex-grow-1"></div>

      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-container>
      <Loading v-if="isLoading" />
      <v-row class="ma-5" v-if="!isLoading">
        <v-col cols="12" flat>
          <v-card flat>
            <v-list-item-content
              class="text-left padding-0"
              v-html="$t('summaryPage.subTitle')"
            ></v-list-item-content>
          </v-card>
        </v-col>
        <v-col cols="12" flat>
          <v-card>
            <v-toolbar dense color="#38598a" dark>
              <v-card-title>
                {{ $t('summaryPage.projectInfoTitle') }}
                <v-spacer></v-spacer>
                <v-icon
                  small
                  class="ml-3"
                  @click="$router.push(`/project/${projectId}/info`)"
                  >mdi-pencil</v-icon
                >
              </v-card-title>
            </v-toolbar>

            <v-list dense class="px-5">
              <v-list-item>
                <v-list-item-content>{{
                  $t('summaryPage.labelOrganizationName')
                }}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div>
                    <v-icon small class="mr-1">mdi-office-building</v-icon>
                    {{ projectInfo && projectInfo.organizationName }}
                  </div>
                </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item>
                <v-list-item-content>{{
                  $t('summaryPage.labelProjectTitle')
                }}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div>
                    <v-icon small class="mr-1">mdi-apps</v-icon>
                    {{ projectInfo.projectName }}
                  </div>
                </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item>
                <v-list-item-content class="align-self-start">{{
                  $t('summaryPage.labelTechnicalContact')
                }}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div>
                    <v-icon small class="mr-1">mdi-account</v-icon>
                    {{ selectedTechnical.firstName }}
                    {{ selectedTechnical.lastName }}
                  </div>
                  <div v-if="selectedTechnical.phone !== ''" class="ml-6">
                    {{ selectedTechnical.phone }}
                  </div>
                  <div v-if="selectedManager.email !== ''" class="ml-6">
                    {{ selectedTechnical.email }}
                  </div>
                </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item>
                <v-list-item-content class="align-self-start">{{
                  $t('summaryPage.labelManagerContact')
                }}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div>
                    <v-icon small class="mr-1">mdi-account</v-icon>
                    {{ selectedManager.firstName }}
                    {{ selectedManager.lastName }}
                  </div>
                  <div v-if="selectedManager.phone !== ''" class="ml-6">
                    {{ selectedManager.phone }}
                  </div>
                  <div v-if="selectedManager.email !== ''" class="ml-6">
                    {{ selectedManager.email }}
                  </div>
                </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item>
                <v-list-item-content class="align-self-start">{{
                  $t('summaryPage.labelCtoContact')
                }}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div>
                    <v-icon small class="mr-1">mdi-account</v-icon>
                    {{ selectedCto.firstName }} {{ selectedCto.lastName }}
                  </div>
                  <div class="ml-6">{{ selectedManager.phone }}</div>
                  <div class="ml-6">{{ selectedManager.email }}</div>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>
        <v-col cols="12" flat>
          <v-card class="mt-5">
            <v-toolbar dense color="#38598a" dark>
              <v-card-title>
                {{ $t('summaryPage.technicalReqTitle') }}
                <v-icon
                  small
                  class="ml-3"
                  @click="$router.push(`/project/${projectId}/technical`)"
                  >mdi-pencil</v-icon
                >
              </v-card-title>
            </v-toolbar>
            <v-list dense class="px-5">
              <v-list-item>
                <v-list-item-content>{{
                  $t('summaryPage.labelApplicationUrl')
                }}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div>
                    <v-icon small class="mr-1">mdi-link</v-icon>
                    {{ technicalReq.clientUri }}
                  </div>
                </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item>
                <v-list-item-content class="align-self-start">{{
                  $t('summaryPage.labelRedirectUrl')
                }}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div
                    v-for="redirectUri in technicalReq.redirectUris"
                    :key="redirectUri"
                  >
                    <v-icon small class="mr-1" v-if="redirectUri !== ''"
                      >mdi-link</v-icon
                    >
                    {{ redirectUri }}
                  </div>
                </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item>
                <v-list-item-content>{{
                  $t('summaryPage.labelJWKSUrl')
                }}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div>
                    <v-icon small class="mr-1">mdi-link</v-icon>
                    {{ technicalReq.jwksUri }}
                  </div>
                </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item>
                <v-list-item-content>{{
                  $t('summaryPage.labelIdTokenSignedResponseAlg')
                }}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <v-list-item-content class="align-end">
                    <div>
                      <v-icon small class="mr-1">mdi-shield-key</v-icon>
                      {{ technicalReq.idTokenSignedResponseAlg }}
                    </div>
                  </v-list-item-content>
                </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item>
                <v-list-item-content>{{
                  $t('summaryPage.labelUserinfoSignedResponseAlg')
                }}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <v-list-item-content class="align-end">
                    <div>
                      <v-icon small class="mr-1">mdi-shield-key</v-icon>
                      {{ technicalReq.userinfoSignedResponseAlg }}
                    </div>
                  </v-list-item-content>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>
        <v-col cols="12" flat>
          <v-card class="mt-5">
            <v-toolbar dense color="#38598a" dark>
              <v-card-title>{{
                $t('summaryPage.packageTestTitle')
              }}</v-card-title>
            </v-toolbar>

            <v-list dense v-if="getPackageList.length > 0" class="px-5">
              <v-list-item>
                <v-list-item-content class="align-self-start">{{
                  $t('summaryPage.labelDataPackageReqd')
                }}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div>
                    <v-icon small class="mr-1">mdi-package-variant</v-icon>
                    {{ selectedPackage.packageName }}
                    <v-icon
                      small
                      class="ml-3"
                      @click="$router.push(`/project/${projectId}/package`)"
                      >mdi-pencil</v-icon
                    >
                  </div>
                  <div
                    v-for="claimName in selectedPackage.claimNames"
                    :key="claimName"
                    class="ml-5"
                  >
                    <v-icon color="#969798" x-small>mdi-check-circle</v-icon>
                    {{ claimName }}
                  </div>
                </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item>
                <v-list-item-content>{{
                  $t('summaryPage.labelTestAccounts')
                }}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div>
                    <v-icon small class="mr-1"
                      >mdi-account-badge-horizontal</v-icon
                    >
                    {{ technicalReq.noOfTestAccount }}
                    <v-icon
                      small
                      class="ml-3"
                      @click="
                        $router.push(`/project/${projectId}/test-account`)
                      "
                      >mdi-pencil</v-icon
                    >
                  </div>
                </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item>
                <v-list-item-content>{{
                  $t('summaryPage.labelSpecialReq')
                }}</v-list-item-content>
                <v-list-item-content class="align-end">{{
                  technicalReq.noteTestAccount
                }}</v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>
        <v-col cols="12">
          <v-card flat class="mt-1">
            <v-divider></v-divider>
            <v-card-actions class="mt-2 py-2 px-0">
              <v-spacer></v-spacer>
              <Button
                @click="$router.push(`/project/${projectId}/test-account/`)"
                aria-label="Back Button"
                secondary
                >{{ $t('summaryPage.goBack') }}</Button
              >
              <Button
                :loading="isLoading"
                class="white--text submit-package ml-6"
                color="indigo accent-4"
                depressed
                @click="dialog = true"
                >{{ $t('summaryPage.submitRequest') }}</Button
              >
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <v-divider></v-divider>
    <div class="text-center">
      <v-dialog v-model="dialog" persistent width="70%" class="text-left">
        <v-card>
          <v-card-title class="bc-subtitle padding-0" primary-title>{{
            $t('summaryPage.disclaimerTitle')
          }}</v-card-title>

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
              >{{ $t('summaryPage.btnAgreeBack') }}</Button
            >
            <Button
              class="white--text submit-package ml-6"
              depressed
              @click="submitFinalRequest"
              >{{ $t('summaryPage.btnAgree') }}</Button
            >
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

const TechnicalReqModule = namespace('TechnicalReqModule');
const ProjectInfoModule = namespace('ProjectInfoModule');
const PackageAndTestModule = namespace('PackageAndTestModule');
const SharedModule = namespace('SharedModule');

@Component({
  components: {
    Button,
    TextArea,
    Loading
  }
})
export default class TestAccountRequest extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  @ProjectInfoModule.Getter('getSingleProjectInfo')
  public projectInfo!: any;
  @ProjectInfoModule.Action('loadSingleProjectInfo')
  public loadSingleProjectInfo!: any;

  @TechnicalReqModule.Getter('getTechnicalReq')
  public technicalReq!: any;
  @TechnicalReqModule.Action('loadTechnicalReqDetails')
  public loadTechnicalReqDetails!: any;

  @PackageAndTestModule.Action('loadPackage') public loadPackage!: any;
  @PackageAndTestModule.Getter('getPackageList') public getPackageList!: [];
  @ProjectInfoModule.Action('submitProject') public submitProject!: any;
  @SharedModule.Action('redirectFromSummaryPage')
  public redirectFromSummaryPage!: any;

  private isLoading: boolean = true;
  private projectId: number = this.id || 0;
  private dialog: boolean = false;
  private selectedTechnical: ProjectUserModel = {
    email: '',
    phone: '',
    firstName: '',
    lastName: '',
    role: 1
  };
  private selectedManager: ProjectUserModel = {
    email: '',
    phone: '',
    firstName: '',
    lastName: '',
    role: 1
  };
  private selectedCto: ProjectUserModel = {
    email: '',
    phone: '',
    firstName: '',
    lastName: '',
    role: 1
  };
  private selectedPackage: any = {
    claimNames: '',
    description: '',
    id: '',
    packageName: ''
  };

  @Watch('projectInfo')
  private ongetprojectInfoChanged(val: any) {
    if (this.technicalReq && this.technicalReq.projectId !== 0) {
      this.isLoading = false;
      this.setUsers(this.projectInfo);
    }
  }
  @Watch('technicalReq')
  private ongetTechnicalReqInfoChanged(val: any) {
    if (this.projectInfo && this.projectInfo.id) {
      this.isLoading = false;
      this.setUsers(this.projectInfo);
    }
  }

  @Watch('getPackageList')
  private ongetPackageListChanged() {
    if (
      this.technicalReq.scopePackageId &&
      this.technicalReq.scopePackageId !== null
    ) {
      this.selectedPackage = this.getSelectedPackage(
        this.technicalReq.scopePackageId
      );
    }
  }

  private getUserDetailsByRole(users: any, selectedRole: number) {
    return users.find((userData: any) => userData.role === selectedRole);
  }
  private getSelectedPackage(packageId: number) {
    const selectedPack = this.getPackageList.find(
      (packageData: any) => packageData.id === packageId
    );
    return selectedPack;
  }

  private setUsers(projectInfo: any) {
    this.selectedTechnical = this.getUserDetailsByRole(projectInfo.users, 1);
    this.selectedManager = this.getUserDetailsByRole(projectInfo.users, 2);
    this.selectedCto = this.getUserDetailsByRole(projectInfo.users, 3);
  }
  private submitFinalRequest() {
    this.submitProject({ projectId: this.projectId });
  }

  private mounted() {
    if (
      this.projectInfo &&
      this.projectInfo.id &&
      this.technicalReq &&
      this.technicalReq.id
    ) {
      this.projectId = this.projectInfo.id;
      this.isLoading = false;
      this.setUsers(this.projectInfo);
    } else {
      this.isLoading = true;
      this.loadSingleProjectInfo(this.id);
      this.loadTechnicalReqDetails(this.id);
    }
    this.loadPackage();
    this.redirectFromSummaryPage(true);
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

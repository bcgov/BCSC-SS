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
      <v-toolbar-title>{{$t('summaryPage.pagetitle')}}</v-toolbar-title>
      <div class="flex-grow-1"></div>

      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-container>
      <Loading v-if="isLoading" />
      <v-row class="ma-5" v-if="!isLoading">
        <v-col cols="12" flat>
          <v-card flat>
            <!-- <v-list-item-content>Summary Page</v-list-item-content> -->
            <v-card-subtitle class="text-left padding-0" v-html="$t('summaryPage.subTitle')"></v-card-subtitle>
          </v-card>
          <v-card>
            <v-card-title>
              {{$t('summaryPage.projectInfoTitle')}}
              <v-icon
                small
                class="ml-3"
                @click="$router.push(`/project/${projectId}/info`)"
              >mdi-pencil</v-icon>
            </v-card-title>
            <v-list dense>
              <v-list-item>
                <v-list-item-content>{{$t('summaryPage.labelOrganizationName')}}</v-list-item-content>
                <v-list-item-content
                  class="align-end"
                >{{projectInfo && projectInfo.organizationName}}</v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>{{$t('summaryPage.labelProjectTitle')}}</v-list-item-content>
                <v-list-item-content class="align-end">{{ projectInfo.projectName}}</v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>{{$t('summaryPage.labelTechnicalContact')}}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div>{{selectedTechnical.firstName }} {{selectedTechnical.lastName }}</div>
                  <div>{{selectedTechnical.phone }}</div>
                  <div>{{selectedTechnical.email }}</div>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>{{$t('summaryPage.labelManagerContact')}}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div>{{selectedManager.firstName}} {{selectedManager.lastName }}</div>
                  <div>{{selectedManager.phone }}</div>
                  <div>{{selectedManager.email }}</div>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>{{$t('summaryPage.labelCtoContact')}}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div>{{selectedCto.firstName}} {{selectedCto.lastName }}</div>
                  <div>{{selectedManager.phone }}</div>
                  <div>{{selectedManager.email }}</div>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
          <v-card class="mt-3">
            <v-card-title>
              {{$t('summaryPage.technicalReqTitle')}}
              <v-icon
                small
                class="ml-3"
                @click="$router.push(`/project/${projectId}/technical`)"
              >mdi-pencil</v-icon>
            </v-card-title>
            <v-list dense>
              <v-list-item>
                <v-list-item-content>{{$t('summaryPage.labelApplicationUrl')}}</v-list-item-content>
                <v-list-item-content
                  class="align-end"
                >{{projectInfo && projectInfo.organizationName}}</v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>{{$t('summaryPage.labelRedirectUrl')}}</v-list-item-content>
                <v-list-item-content class="align-end">{{ projectInfo.projectName}}</v-list-item-content>
              </v-list-item>

              <v-list-item>
                <v-list-item-content>{{$t('summaryPage.labelJWKSUrl')}}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div>{{selectedManager.firstName}} {{selectedManager.lastName }}</div>
                  <div>{{selectedManager.phone }}</div>
                  <div>{{selectedManager.email }}</div>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>{{$t('summaryPage.labelIdTokenSignedResponseAlg')}}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div>{{selectedCto.firstName}} {{selectedCto.lastName }}</div>
                  <div>{{selectedManager.phone }}</div>
                  <div>{{selectedManager.email }}</div>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>{{$t('summaryPage.labelUserinfoSignedResponseAlg')}}</v-list-item-content>
                <v-list-item-content class="align-end">
                  <div>{{selectedTechnical.firstName }} {{selectedTechnical.lastName }}</div>
                  <div>{{selectedTechnical.phone }}</div>
                  <div>{{selectedTechnical.email }}</div>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <v-divider></v-divider>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Watch, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import { ProjectUserModel } from '@/models/ProjectInfoModel';
import Button from '@/Atomic/Button/Button.vue';
import TextArea from '@/Atomic/TextArea/TextArea.vue';
import Loading from '@/Atomic/Loading/Loading.vue';
// const PackageAndTestModule = namespace('PackageAndTestModule');
const TechnicalReqModule = namespace('TechnicalReqModule');
const ProjectInfoModule = namespace('ProjectInfoModule');

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
  // @PackageAndTestModule.Getter('errorStatus') public errorStatus!: boolean;
  // @PackageAndTestModule.Action('loadPackage') public loadPackage!: any;
  // @PackageAndTestModule.Getter('getPackageList') public getPackageList!: [];
  // @PackageAndTestModule.Action('clearStatus') public clearStatus!: any;
  // @PackageAndTestModule.Action('addTestAccountRequestToProject')
  // public addTestAccountRequestToProject!: any;

  // private noOfTestAccounts: any = [1, 2, 3, 5];
  // private notes: string = '';

  // private slectedNumber: number = 1;
  private isLoading: boolean = true;
  private projectId: number = this.id || 0;
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

  // private selectedTestAccount(packageVal: number) {
  //   this.slectedNumber = packageVal;
  // }

  @Watch('projectInfo')
  private ongetSingleProjectInfoChanged(val: any) {
    this.projectId = this.projectInfo.id;
    this.isLoading = false;
    this.setUsers(this.projectInfo);
  }
  private getUserDetailsByRole(users: any, selectedRole: number) {
    return users.find((userData: any) => userData.role === selectedRole);
  }

  private setUsers(projectInfo: any) {
    this.selectedTechnical = this.getUserDetailsByRole(projectInfo.users, 1);
    this.selectedManager = this.getUserDetailsByRole(projectInfo.users, 2);
    this.selectedCto = this.getUserDetailsByRole(projectInfo.users, 3);
  }

  private mounted() {
    if (this.projectInfo && this.projectInfo.id) {
      this.projectId = this.projectInfo.id;
      this.isLoading = false;
    } else {
      this.isLoading = true;
      this.loadSingleProjectInfo(this.id);
    }
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

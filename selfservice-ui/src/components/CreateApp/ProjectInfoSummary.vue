/** * ClientID component */

<template>
  <v-card>
    <Loading v-if="isLoading" />
    <v-toolbar dense class="bc-subtitle-2" dark v-else>
      <v-card-title>
        {{ $t('summaryPage.projectInfoTitle') }}
        <v-spacer></v-spacer>
        <v-icon small class="ml-3" @click="$router.push(`/project/${projectId}/info`)">mdi-pencil</v-icon>
      </v-card-title>
    </v-toolbar>

    <v-list dense class="px-5">
      <v-list-item>
        <v-list-item-content class="pr-30">
          {{
          $t('summaryPage.labelOrganizationName')
          }}
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
          {{
          $t('summaryPage.labelProjectTitle')
          }}
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
          {{
          $t('summaryPage.labelTechnicalContact')
          }}
          <span
            class="small-hint pad-50"
            v-html="$t('summaryPage.developerHint')"
          ></span>
        </v-list-item-content>
        <v-list-item-content class="align-end">
          <div>
            <v-icon small class="mr-1">mdi-account</v-icon>
            {{ selectedTechnical.firstName }}
            {{ selectedTechnical.lastName }}
          </div>
          <div v-if="selectedTechnical.phone !== ''" class="ml-6">{{ selectedTechnical.phone }}</div>
          <div v-if="selectedTechnical.email !== ''" class="ml-6">{{ selectedTechnical.email }}</div>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <v-list-item>
        <v-list-item-content class="align-self-start pr-30">
          {{
          $t('summaryPage.labelManagerContact')
          }}
          <span
            class="small-hint pad-50"
            v-html="$t('summaryPage.managerHint')"
          ></span>
        </v-list-item-content>
        <v-list-item-content class="align-end">
          <div>
            <v-icon small class="mr-1">mdi-account</v-icon>
            {{ selectedManager.firstName }}
            {{ selectedManager.lastName }}
          </div>
          <div v-if="selectedManager.phone !== ''" class="ml-6">{{ selectedManager.phone }}</div>
          <div v-if="selectedManager.email !== ''" class="ml-6">{{ selectedManager.email }}</div>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <v-list-item>
        <v-list-item-content class="align-self-start pr-30">
          {{
          $t('summaryPage.labelCtoContact')
          }}
          <span
            class="small-hint pad-50"
            v-html="$t('summaryPage.ctoHint')"
          ></span>
        </v-list-item-content>
        <v-list-item-content class="align-end">
          <div>
            <v-icon small class="mr-1">mdi-account</v-icon>
            {{ selectedCto.firstName }} {{ selectedCto.lastName }}
          </div>
          <div class="ml-6">{{ selectedCto.phone }}</div>
          <div class="ml-6">{{ selectedCto.email }}</div>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import { ProjectUserModel } from '@/models/ProjectInfoModel';
import Loading from '@/Atomic/Loading/Loading.vue';

const ClientIdModule = namespace('ClientIdModule');
const ProjectInfoModule = namespace('ProjectInfoModule');

@Component({
  components: { Loading }
})
export default class ProjectInfoSummary extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  // @Prop({ default: {} })
  // public projectInfo!: any;
  @ProjectInfoModule.Getter('getSingleProjectInfo')
  public projectInfo!: any;
  @ProjectInfoModule.Action('loadSingleProjectInfo')
  public loadSingleProjectInfo!: any;

  @ProjectInfoModule.Getter('getFinalProjectSubmissionStatus')
  public getFinalProjectSubmissionStatus!: any;

  @ProjectInfoModule.Action('clearSubmitProjectStatus')
  public clearSubmitProjectStatus!: any;

  private isLoading: boolean = true;

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

  @Watch('projectInfo')
  private ongetprojectInfoChanged(val: any) {
    // if (this.technicalReq && this.technicalReq.projectId !== 0) {
    //   this.isTechnicalInfoAvailable = this.technicalReq.id ? true : false;
    this.isLoading = false;
    this.setUsers(this.projectInfo);
    // }
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
    this.isLoading = true;
    this.loadSingleProjectInfo(this.id);
  }
}
</script>


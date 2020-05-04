/** * Dashboard of app */

<template>
  <v-card class="mx-auto" style="max-width: 80%;">
    <v-toolbar flat class="bc-subtitle" dark>
      <v-toolbar-title>{{ $t('dashboard.pagetitle') }}</v-toolbar-title>
      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-divider></v-divider>
    <v-container>
      <v-row class="ma-2">
        <v-col cols="12">
          <v-card-subtitle
            class="text-left bc-padding-left-0 page-info pa-2"
            v-html="$t('dashboard.createProjectInfo')"
          ></v-card-subtitle>
        </v-col>
        <Button
          class="white--text ml-3 yellow-btn"
          depressed
          :yellowBtn="true"
          @click="$router.push(`/project/info`)"
          name="btn-create-project"
          data-test-id="btn-create-project"
        >{{ $t('dashboard.btnCreateProject') }}</Button>
        <v-col cols="12" md="12" v-if="projectInfoList.length > 0">
          <h2 class="bc-page-title-h1 px-2 mb-2">{{ $t('dashboard.myprojectTitle') }}</h2>

          <v-simple-table class="text-left">
            <template v-slot:default>
              <thead class="table-head">
                <tr>
                  <th
                    :scope="$t('dashboard.tblTitleProjectName')"
                  >{{ $t('dashboard.tblTitleProjectName') }}</th>
                  <th
                    :scope="$t('dashboard.tblTitleReferenceNo')"
                  >{{ $t('dashboard.tblTitleReferenceNo') }}</th>
                  <th :scope="$t('dashboard.tblTitlCreated')">{{ $t('dashboard.tblTitlCreated') }}</th>
                  <th
                    :scope="$t('dashboard.tblTitlrole')"
                    v-if="isClient"
                  >{{ $t('dashboard.tblTitlrole') }}</th>
                  <th
                    :scope="$t('dashboard.tblTitleProjectStatus')"
                  >{{ $t('dashboard.tblTitleProjectStatus') }}</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="project in projectInfoList"
                  :key="project.id"
                  @click="redirectToProject(project)"
                  style="cursor: pointer"
                >
                  <td>{{ project.name }}</td>
                  <td>{{ project.id }}</td>
                  <td>{{ project.created }}</td>
                  <td v-if="isClient">{{ project.role }}</td>

                  <td>
                    {{
                    $t(`dashboard.role${projectStatusList[project.statusId]}`)
                    }}
                  </td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-col>
        <v-col cols="12" md="12" v-else>
          <v-card flat class="text-left">
            <v-card-text>{{ $t('dashboard.noData') }}</v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import { projectStatus } from '@/constants/enums';

import Button from '@/Atomic/Button/Button.vue';

const ProjectInfoModule = namespace('ProjectInfoModule');
const KeyCloakModule = namespace('KeyCloakModule');
const SharedModule = namespace('SharedModule');

@Component({
  components: {
    Button
  }
})
export default class Dashboard extends Vue {
  @KeyCloakModule.Getter('isClient')
  public isClient!: any;

  @ProjectInfoModule.Getter('getProjectInfoList')
  public projectInfoList!: any;
  @ProjectInfoModule.Action('loadProjectInfo')
  public loadProjectInfo!: any;
  @ProjectInfoModule.Action('errorStatus')
  public errorStatus!: any;
  @SharedModule.Action('redirectFromSummaryPage')
  public redirectFromSummaryPage!: any;

  @SharedModule.Getter('isRedirectFromSummaryPage')
  public isRedirectFromSummaryPage!: boolean;

  private projectStatusList: any = projectStatus;

  private mounted() {
    this.loadProjectInfo();
  }

  private redirectToProject(project: any) {
    if (project.statusId === projectStatus.development) {
      this.redirectFromSummaryPage(false);
    }
    this.$router.push(`/project-container/${project.id}`);
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.table-head {
  background-color: $BCgovBlue5 !important;
  color: $BCgovWhite !important;
  & tr {
    & th {
      color: $BCgovWhite !important;
      font-size: 14px;
    }
  }
}
</style>

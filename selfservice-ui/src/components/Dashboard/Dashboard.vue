/** * Dashboard of app */

<template>
  <v-card class="mx-auto" style="max-width: 80%;">
    <v-toolbar flat class="bc-subtitle" dark>
      <v-toolbar-title>{{ $t('dashboard.pagetitle') }}</v-toolbar-title>
      <div class="flex-grow-1"></div>

      <div class="flex-grow-1"></div>

      <v-btn
        class="ma-2"
        fab
        dark
        color="#fba30e"
        @click="$router.push(`/project/info`)"
        data-test-id="btn-create-project"
      >
        <v-icon dark large>mdi-plus</v-icon>
      </v-btn>
    </v-toolbar>
    <v-divider></v-divider>
    <v-container>
      <v-row class="ma-5">
        <v-col cols="12" md="12" v-if="projectInfoList.length > 0">
          <v-simple-table class="text-left">
            <template v-slot:default>
              <thead>
                <tr>
                  <th
                    :scope="$t('dashboard.tblTitleReferenceNo')"
                  >{{ $t('dashboard.tblTitleReferenceNo') }}</th>
                  <th
                    :scope="$t('dashboard.tblTitleProjectName')"
                  >{{ $t('dashboard.tblTitleProjectName') }}</th>
                  <th
                    :scope="$t('dashboard.tblTitlrole')"
                    v-if="isClient"
                  >{{ $t('dashboard.tblTitlrole') }}</th>
                  <th :scope="$t('dashboard.tblTitlCreated')">{{ $t('dashboard.tblTitlCreated') }}</th>
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
                  <td>{{ project.id }}</td>
                  <td>{{ project.name }}</td>
                  <td v-if="isClient">{{ project.role }}</td>
                  <td>{{ project.created }}</td>
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

const ProjectInfoModule = namespace('ProjectInfoModule');
const KeyCloakModule = namespace('KeyCloakModule');
const SharedModule = namespace('SharedModule');

@Component
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
    this.$router.push(`project-container/${project.id}`);
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
</style>

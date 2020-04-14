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
                  <th :scope="$t('dashboard.tblTitleSi')">
                    {{ $t('dashboard.tblTitleSi') }}
                  </th>
                  <th :scope="$t('dashboard.tblTitleProjectName')">
                    {{ $t('dashboard.tblTitleProjectName') }}
                  </th>
                  <!-- <th :scope="$t('dashboard.tblTitleProjectId')">
                    {{ $t('dashboard.tblTitleProjectId') }}
                  </th>-->
                  <th :scope="$t('dashboard.tblTitlrole')" v-if="isClient">
                    {{ $t('dashboard.tblTitlrole') }}
                  </th>
                  <th :scope="$t('dashboard.tblTitlCreated')">
                    {{ $t('dashboard.tblTitlCreated') }}
                  </th>
                  <th :scope="$t('dashboard.tblTitleProjectStatus')">
                    {{ $t('dashboard.tblTitleProjectStatus') }}
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="(project, idx) in projectInfoList"
                  :key="project.id"
                  @click="$router.push(`/project/${project.id}/summary`)"
                  style="cursor: pointer"
                >
                  <td>{{ idx + 1 }}</td>
                  <td>{{ project.name }}</td>
                  <!-- <td>{{ project.id }}</td> -->
                  <td v-if="isClient">{{ project.role }}</td>
                  <td>{{ project.created }}</td>
                  <td>{{ project.status }}</td>
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
const ProjectInfoModule = namespace('ProjectInfoModule');
const KeyCloakModule = namespace('KeyCloakModule');

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

  private mounted() {
    this.loadProjectInfo();
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
</style>

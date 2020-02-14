/** * CreateApp of app */

<template>
  <v-card class="mx-auto" style="max-width: 80%;">
    <v-toolbar flat class="bc-subtitle" dark>
      <v-toolbar-title>{{ $t('dashboard.pagetitle') }}</v-toolbar-title>
      <div class="flex-grow-1"></div>
      <!-- <v-col class="col-lg-4 col-md-5 col-8">
        <v-alert type="error" v-if="errorStatus" class="alert-top"
          >Something went wrong...</v-alert
        >
      </v-col> -->
      <div class="flex-grow-1"></div>
      <v-icon x-large @click="$router.push(`/project/info`)"
        >mdi-plus-circle</v-icon
      >
    </v-toolbar>
    <v-divider></v-divider>
    <!-- <v-item-group mandatory :value="slectedPackage"> -->
    <v-container>
      <v-row class="ma-5">
        <v-col cols="12" md="12">
          <v-simple-table>
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-left">
                    {{ $t('dashboard.tblTitleProjectName') }}
                  </th>
                  <th class="text-left">
                    {{ $t('dashboard.tblTitleProjectId') }}
                  </th>
                  <th class="text-left">
                    {{ $t('dashboard.tblTitlCreated') }}
                  </th>
                  <th class="text-left">
                    {{ $t('dashboard.tblTitleProjectStatus') }}
                  </th>
                  <th class="text-left">
                    {{ $t('dashboard.tblTitleProjectActions') }}
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="project in projectInfoList" :key="project.id">
                  <td class="text-left">{{ project.projectName }}</td>
                  <td class="text-left">{{ project.id }}</td>
                  <td class="text-left">{{ project.createdAt }}</td>
                  <td class="text-left">{{ project.status }}</td>
                  <td class="text-left">view</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import AddProjectInfo from '@/components/CreateApp/AddProjectInfo.vue';
import { Getter, namespace, Action } from 'vuex-class';
const ProjectInfoModule = namespace('ProjectInfoModule');

@Component({
  components: {
    AddProjectInfo
  }
})
export default class Dashboard extends Vue {
  @Prop({ default: 'info' })
  public step!: string;
  @Prop({ default: '' })
  public id!: number;
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

/** * ProjectHistory of app */

<template>
  <v-card class="mx-auto">
    <v-container>
      <v-row class="ma-2" v-if="isLoading">
        <Loading />
      </v-row>
      <v-row class="ma-2" v-else>
        <v-col cols="12">
          <v-col cols="12" md="12" v-if="projectHistoryData.length > 0">
            <h2 class="bc-container-title-h1 px-2 mb-5">
              {{ $t('projectHistory.tabSubTitle') }}
            </h2>

            <v-simple-table class="text-left">
              <template v-slot:default>
                <thead class="table-head">
                  <tr>
                    <th :scope="$t('projectHistory.tblTitleProjectStatus')">
                      {{ $t('projectHistory.tblTitleProjectStatus') }}
                    </th>
                    <th :scope="$t('projectHistory.tblTitleDateAssigned')">
                      {{ $t('projectHistory.tblTitleDateAssigned') }}
                    </th>
                    <th :scope="$t('projectHistory.tblActionTakenBy')">
                      {{ $t('projectHistory.tblActionTakenBy') }}
                    </th>
                    <th :scope="$t('projectHistory.tblActionRole')">
                      {{ $t('projectHistory.tblActionRole') }}
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="history in projectHistoryData"
                    :key="history.id"
                    @click="redirectToProject(project)"
                    style="cursor: pointer"
                  >
                    <td>
                      {{
                        $t(
                          `projectStatus.status${
                            projectStatusList[history.status]
                          }`
                        )
                      }}
                    </td>
                    <td>{{ history.created }}</td>
                    <td>{{ history.name }}</td>
                    <td>
                      {{
                        $t(
                          history.role &&
                            `projectRoles.role${projectRolesList[history.role]}`
                        )
                      }}
                    </td>
                  </tr>
                </tbody>
              </template>
            </v-simple-table>
          </v-col>
          <v-col cols="12" md="12" v-else>
            <v-card flat class="text-left">
              <v-card-text>{{ $t('projectHistory.noData') }}</v-card-text>
            </v-card>
          </v-col>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import { projectStatus, projectRoles } from '@/constants/enums';
import VirtualCardCount from '@/components/Dashboard/VirtualCardCount.vue';
import Loading from '@/Atomic/Loading/Loading.vue';

import Button from '@/Atomic/Button/Button.vue';

const ProjectInfoModule = namespace('ProjectInfoModule');

@Component({
  components: {
    Button,
    VirtualCardCount,
    Loading,
  },
})
export default class ProjectHistory extends Vue {
  @Prop({ default: 0 })
  public id!: number;

  @ProjectInfoModule.Getter('getProjectHistory')
  public getProjectHistory!: any;
  @ProjectInfoModule.Action('loadProjectHistory')
  public loadProjectHistory!: any;

  private projectStatusList: any = projectStatus;
  private projectRolesList: any = projectRoles;
  private isLoading: boolean = true;
  private projectHistoryData: any = [];

  @Watch('getProjectHistory')
  private ongetProjectHistoryChanged(val: any) {
    this.isLoading = false;
    this.projectHistoryData = val;
  }

  private mounted() {
    this.loadProjectHistory(this.id);
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

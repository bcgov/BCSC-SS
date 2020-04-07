/** * Dashboard of app */

<template>
  <v-container>
    <v-row class="ma-5">
      <v-col cols="12" v-if="isLoading">
        <Loading />
      </v-col>
      <v-col cols="12" v-else>
        <h2 class="text-left tab-headline">
          {{ $t('TeamRoles.pagetitle') }}
        </h2>
        <h4 class="text-left tab-headline font-weight-medium">
          {{ $t('TeamRoles.pageInfo') }}
        </h4>

        <v-simple-table class="mt-5">
          <template v-slot:default>
            <thead class="tbl-head">
              <tr class="text-left">
                <th class="text-left">{{ $t('TeamRoles.tblHeadName') }}</th>
                <th class="text-left">{{ $t('TeamRoles.tblHeadMyRole') }}</th>
                <th class="text-left">{{ $t('TeamRoles.tblHeadEmail') }}</th>
                <th class="text-left">{{ $t('TeamRoles.tblHeadPhone') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="team in teamList" :key="team.id" class="text-left">
                <td>{{ team.firstName }} {{ team.lastName }}</td>
                <td>
                  {{ $t(`TeamRoles.labelRole${getRoleName(team.role)}`) }}
                </td>
                <td>{{ team.email }}</td>
                <td>{{ team.phone }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';

import Loading from '@/Atomic/Loading/Loading.vue';
import { projectRolesList } from '@/constants/enums';

const TeamRolesModule = namespace('TeamRolesModule');

@Component({
  components: {
    Loading
  }
})
export default class TeamRoles extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  @TeamRolesModule.Getter('getTeamList')
  public teamList!: any;
  @TeamRolesModule.Action('loadTeam')
  public loadTeam!: any;

  private isLoading: boolean = false;
  // private selectedTab: number = 0;
  private rolesList: any = projectRolesList;

  @Watch('teamList')
  private ongetroleListChanged(val: any) {
    this.isLoading = false;
  }

  private getRoleName(roles: any) {
    return this.rolesList[roles] || 'developer';
  }

  private mounted() {
    this.isLoading = true;
    this.loadTeam(this.id);
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.tbl-head {
  background-color: $BCgovBlue10;
  color: $BCgovFontColorInverted !important;
  & th {
    color: $BCgovFontColorInverted !important;
  }
}
</style>

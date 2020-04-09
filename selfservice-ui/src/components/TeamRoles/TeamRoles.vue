/** * Dashboard of app */

<template>
  <v-container>
    <v-row class="ma-5" v-if="isLoading">
      <v-col cols="12">
        <Loading />
      </v-col>
    </v-row>

    <v-row class="ma-5" v-else>
      <v-col cols="12">
        <v-card flat="">
          <h2 class="text-left tab-headline">
            {{ $t('teamRoles.pagetitle') }}
          </h2>
          <h4 class="text-left tab-headline font-weight-medium">
            {{ $t('teamRoles.pageInfo') }}
          </h4>

          <v-simple-table class="mt-5" v-if="teamList.length > 0">
            <template v-slot:default>
              <thead class="tbl-head">
                <tr class="text-left">
                  <th class="text-left">{{ $t('teamRoles.tblHeadName') }}</th>
                  <th class="text-left">{{ $t('teamRoles.tblHeadMyRole') }}</th>
                  <th class="text-left">{{ $t('teamRoles.tblHeadEmail') }}</th>
                  <th class="text-left">{{ $t('teamRoles.tblHeadPhone') }}</th>
                  <th class="text-left" v-if="isAdmin"></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="team in teamList" :key="team.id" class="text-left">
                  <td>{{ team.firstName }} {{ team.lastName }}</td>
                  <td>
                    {{ $t(`teamRoles.labelRole${rolesList[team.role]}`) }}
                    <v-icon
                      @click="toggleAddMember(true, team.id)"
                      class="ml-2"
                      small
                      v-if="team.isCurrentUser"
                      >mdi-pencil</v-icon
                    >
                  </td>
                  <td>{{ team.email }}</td>
                  <td>{{ team.phone }}</td>
                  <td v-if="isAdmin">
                    <v-icon
                      @click="toggleAddMember(true, team.id)"
                      class="ml-2"
                      small
                      >mdi-pencil</v-icon
                    >
                  </td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
          <v-card-actions class="mt-5">
            <v-spacer></v-spacer>
            <Button
              @click="toggleAddMember(true)"
              :aria-label="$t('teamRoles.btnAddTeamMember')"
              :disabled="teamList.length >= 3"
              >{{ $t('teamRoles.btnAddTeamMember') }}</Button
            >
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col>
        <div class="text-center">
          <v-dialog v-model="dialog" width="71%" class="text-left">
            <v-card>
              <AddTeamMember
                :id="id"
                @toggleAddMember="toggleAddMember"
                :memberId="memberId"
              />
            </v-card>
          </v-dialog>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';

import Loading from '@/Atomic/Loading/Loading.vue';
import Button from '@/Atomic/Button/Button.vue';
import AddTeamMember from '@/components/TeamRoles/AddTeamMember.vue';

import { projectRolesList } from '@/constants/enums';

const TeamRolesModule = namespace('TeamRolesModule');
const KeyCloakModule = namespace('KeyCloakModule');

@Component({
  components: {
    Loading,
    Button,
    AddTeamMember
  }
})
export default class TeamRoles extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  @TeamRolesModule.Getter('getTeamList')
  public teamList!: any;
  @TeamRolesModule.Action('loadTeam')
  public loadTeam!: any;
  @KeyCloakModule.Getter('isAdmin')
  private isAdmin!: any;

  private isLoading: boolean = false;
  // private selectedTab: number = 0;
  private rolesList: any = projectRolesList;
  private dialog: boolean = false;
  private memberId: number = 0;

  @Watch('teamList')
  private ongetroleListChanged(val: any) {
    this.isLoading = false;
  }

  private toggleAddMember(status: boolean = false, memberId: number = 0) {
    this.memberId = memberId;
    this.dialog = status;
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

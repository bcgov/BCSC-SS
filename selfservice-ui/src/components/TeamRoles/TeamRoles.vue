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
        <v-card flat>
          <h2 class="text-left tab-headline page-title-h2">
            {{ $t('teamRoles.pagetitle') }}
          </h2>
          <p class="text-left  pageinfo">{{ $t('teamRoles.pageInfo') }}</p>
          <v-simple-table class="mt-5" v-if="teamList.length > 0">
            <template v-slot:default>
              <thead class="tbl-head">
                <tr class="text-left">
                  <th :scope="$t('teamRoles.tblHeadName')" class="text-left">
                    {{ $t('teamRoles.tblHeadName') }}
                  </th>
                  <th :scope="$t('teamRoles.tblHeadMyRole')" class="text-left">
                    {{ $t('teamRoles.tblHeadMyRole') }}
                  </th>
                  <th :scope="$t('teamRoles.tblHeadEmail')" class="text-left">
                    {{ $t('teamRoles.tblHeadEmail') }}
                  </th>
                  <th :scope="$t('teamRoles.tblHeadPhone')" class="text-left">
                    {{ $t('teamRoles.tblHeadPhone') }}
                  </th>
                  <th scope="actions" class="text-left" v-if="isAdmin"></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="team in teamList" :key="team.id" class="text-left">
                  <td>{{ team.firstName }} {{ team.lastName }}</td>
                  <td>
                    {{ $t(`teamRoles.labelRole${rolesList[team.role]}`) }}
                    <span
                      @click="
                        toggleAddMember(true, team.id, team.isCurrentUser)
                      "
                      @keyup.enter="
                        toggleAddMember(true, team.id, team.isCurrentUser)
                      "
                      v-if="team.isCurrentUser && teamList.length == 1"
                      class="edit-wrapper"
                      tabindex="0"
                      :aria-label="$t('global.edit')"
                      role="link"
                    >
                      <v-icon class="ml-2" small>mdi-pencil</v-icon>
                    </span>
                  </td>
                  <td>
                    <a :href="`mailto:${team.email}`">{{ team.email }}</a>
                  </td>
                  <td>{{ team.phone }}</td>
                  <td v-if="isAdmin">
                    <v-icon
                      @click="toggleAddMember(true, team.id)"
                      @keyup.enter="toggleAddMember(true, team.id)"
                      class="ml-2"
                      small
                      >mdi-pencil</v-icon
                    >
                    <v-icon
                      @click="deleteMemberDialog(team.id)"
                      @keyup.enter="deleteMemberDialog(true, team.id)"
                      class="ml-2 delete-member"
                      small
                      >mdi-delete</v-icon
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
              @keyup.enter="toggleAddMember(true)"
              :aria-label="$t('teamRoles.btnAddTeamMember')"
              :disabled="teamList.length >= 3"
              class="team-roles"
              data-test-id="btn-add-new-team"
              >{{ $t('teamRoles.btnAddTeamMember') }}</Button
            >
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col>
        <div class="text-center">
          <v-dialog v-model="dialog" width="85%" class="text-left">
            <v-card>
              <AddTeamMember
                :id="id"
                @toggleAddMember="toggleAddMember"
                :memberId="memberId"
                :isCurrentUser="isCurrentUser"
              />
            </v-card>
          </v-dialog>
        </div>
      </v-col>
      <v-col>
        <v-dialog v-model="dialogDelete" persistent max-width="400">
          <v-card>
            <v-card-text
              class="text-left"
              v-html="$t('teamRoles.deleteWarning')"
            ></v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <Button
                secondary
                text
                @click="deleteMember(true)"
                @keyup.enter="deleteMember(true)"
                >Cancel</Button
              >
              <Button
                text
                @click="deleteMember()"
                @keyup.enter="deleteMember(true)"
                >Delete</Button
              >
            </v-card-actions>
          </v-card>
        </v-dialog>
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

import { projectRoles } from '@/constants/enums';

const TeamRolesModule = namespace('TeamRolesModule');
const KeyCloakModule = namespace('KeyCloakModule');

@Component({
  components: {
    Loading,
    Button,
    AddTeamMember,
  },
})
export default class TeamRoles extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  @TeamRolesModule.Getter('getTeamList')
  public teamList!: any;
  @TeamRolesModule.Action('loadTeam')
  public loadTeam!: any;
  @TeamRolesModule.Action('deleteTeamMember')
  public deleteTeamMember!: any;
  @KeyCloakModule.Getter('isAdmin')
  private isAdmin!: any;

  private isLoading: boolean = false;
  // private selectedTab: number = 0;
  private rolesList: any = projectRoles;
  private dialog: boolean = false;
  private dialogDelete: boolean = false;
  private memberId: number = 0;
  private isCurrentUser: boolean = false;

  @Watch('teamList')
  private ongetroleListChanged(val: any) {
    this.isLoading = false;
  }

  private toggleAddMember(
    status: boolean = false,
    memberId: number = 0,
    isCurrentUser: boolean = false
  ) {
    this.memberId = memberId;
    this.isCurrentUser = isCurrentUser;
    this.dialog = status;
  }

  private deleteMemberDialog(teamMemberId: number) {
    this.dialogDelete = true;
    this.memberId = teamMemberId;
  }

  private deleteMember(cancel: boolean = false) {
    if (!cancel) {
      this.isLoading = true;
      this.deleteTeamMember({
        projectId: this.id,
        memberId: this.memberId,
      });
    }
    this.memberId = 0;
    this.dialogDelete = false;
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

/** * Add team member of app */

<template>
  <v-container>
    <v-row class="text-left">
      <v-col v-if="userDetails">
        <v-card class="v-form ma-3" flat>
          <v-form ref="form" v-model="form">
            <v-card class="v-form px-6 ma-3">
              <v-alert type="error" dense outlined class="text-left" v-if="memberErrorStatus">
                <div>{{ $t('addTeamMember.errorTitle') }}</div>
                <ul>
                  <li
                    v-for="(errors, idx) in errorList"
                    :key="idx"
                    v-html="$t(`addTeamMember.${errors}`)"
                  ></li>
                </ul>
              </v-alert>

              <v-row>
                <v-col cols="12">
                  <div class="display-1">
                    {{
                    $t(
                    !editMode
                    ? 'addTeamMember.pagetitle'
                    : 'addTeamMember.pagetitleUpdate'
                    )
                    }}
                  </div>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-card-subtitle class="headline bc-padding-left-0">
                    {{
                    $t('addTeamMember.contactInfo')
                    }}
                  </v-card-subtitle>
                  <Input
                    v-model="userDetails.firstName"
                    :label="$t('addTeamMember.labelFirstName')"
                    :rules="[
                      rules.required,
                      rules.length(1),
                      rules.maxLength(250)
                    ]"
                    type="text"
                    :disabled="disabled()"
                  />
                  <Input
                    v-model="userDetails.lastName"
                    :label="$t('addTeamMember.labelLastName')"
                    :rules="[
                      rules.required,
                      rules.length(1),
                      rules.maxLength(250)
                    ]"
                    type="text"
                    :disabled="disabled()"
                  />
                  <Input
                    v-model="userDetails.email"
                    :label="$t('addTeamMember.labelWorkEmail')"
                    :rules="[rules.required, rules.email, rules.maxLength(250)]"
                    type="text"
                    :disabled="disabled()"
                  />

                  <Input
                    v-model="userDetails.phone"
                    :label="$t('addTeamMember.labelPhone')"
                    type="text"
                    :disabled="disabled()"
                    :optional="true"
                  />
                </v-col>
                <v-col>
                  <v-divider class="mx-4" :inset="inset" vertical></v-divider>
                </v-col>
                <v-col cols="12" sm="5">
                  <v-card-subtitle class="headline bc-padding-left-0">
                    {{
                    $t('addTeamMember.roleTitle')
                    }}
                  </v-card-subtitle>

                  <v-radio-group v-model="userDetails.role" :mandatory="false">
                    <v-radio
                      :label="$t(`addTeamMember.labelRole${rolesList[1]}`)"
                      :value="projectRoles.developer"
                      class="my-2"
                    ></v-radio>
                    <v-radio
                      :label="$t(`addTeamMember.labelRole${rolesList[2]}`)"
                      :value="projectRoles.manager"
                      class="my-2"
                    ></v-radio>
                    <v-radio
                      :label="$t(`addTeamMember.labelRole${rolesList[3]}`)"
                      :value="projectRoles.cto"
                      class="my-2"
                    ></v-radio>
                  </v-radio-group>

                  <v-card-actions class="btn-bottom">
                    <v-spacer></v-spacer>
                    <Button
                      @click="$emit('toggleAddMember', false)"
                      aria-label="Back Button"
                      secondary
                    >{{ $t('addTeamMember.btnCancel') }}</Button>
                    <Button
                      :disabled="!form"
                      class="white--text submit-package ml-6"
                      @click="submitTeamMember"
                    >{{ $t('addTeamMember.btnSumbmit') }}</Button>
                  </v-card-actions>
                </v-col>
              </v-row>
            </v-card>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
// import { ProjectUserModel, ProjectInfoModel } from '@/models/ProjectInfoModel';
import Input from '@/Atomic/Input/Input.vue';
import Button from '@/Atomic/Button/Button.vue';

import validationRules from '@/config/validationRules';
import { projectRoles, projectRolesList } from '@/constants/enums';
import { TeamRoleModel } from '@/models/TeamRoleModel';
import { memberDetails } from '@/store/modules/TeamRoles/defaults';

const TeamRolesModule = namespace('TeamRolesModule');
const KeyCloakModule = namespace('KeyCloakModule');

@Component({
  components: {
    Input,
    Button
  }
})
export default class AddTeamMember extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  @Prop()
  public toggleAddMember: any;
  @Prop({ default: 0 })
  public memberId!: number;

  @TeamRolesModule.Getter('getTeamList')
  public teamList!: any;
  @TeamRolesModule.Action('addTeamMember')
  public addTeamMember!: any;
  @TeamRolesModule.Action('updateTeamMember')
  public updateTeamMember!: any;
  @TeamRolesModule.Action('getTeamMember')
  public getTeamMember!: any;
  @TeamRolesModule.Getter('memberErrorStatus')
  public memberErrorStatus!: any;
  @TeamRolesModule.Getter('getMemberErrorList')
  public getMemberErrorList!: any;
  @TeamRolesModule.Getter('getMemberDetails')
  public memberDetails!: any;
  @TeamRolesModule.Getter('memberSucessStatus')
  public memberSucessStatus!: any;
  @TeamRolesModule.Action('clearMemberData')
  public clearMemberData!: any;

  public errorList: any = {};

  public userDetails: TeamRoleModel;

  @KeyCloakModule.Getter('isAdmin')
  private isAdmin!: any;

  private rules: any = validationRules;
  private projectRoles: any = projectRoles;
  private selectedRole: any = 1;
  private rolesList: any = projectRolesList;
  private form: boolean = false;
  private editMode: boolean = false;

  public constructor() {
    super();
    this.userDetails = memberDetails;
  }

  @Watch('getMemberErrorList')
  private ongetMemberErrorListChanged(val: any) {
    this.errorList = val;
  }

  @Watch('memberDetails')
  private ongetmemberDetailsChanged(val: any) {
    this.userDetails = val;
  }

  @Watch('memberId')
  private onmemberIdChanged(val: any) {
    this.memberId = val;
    this.getMemberDetails();
  }
  @Watch('memberSucessStatus')
  private onmemberSucessStatusChanged(val: boolean) {
    if (val) {
      this.$emit('toggleAddMember', false);
    }
  }

  private submitTeamMember() {
    if (this.editMode) {
      this.updateTeamMember({
        userDetails: this.userDetails,
        projectId: this.id,
        memberId: this.memberId
      });
    } else {
      this.addTeamMember({
        userDetails: this.userDetails,
        projectId: this.id
      });
    }
  }
  private getMemberDetails() {
    if (this.memberId !== 0) {
      this.editMode = true;
      this.getTeamMember({ memberId: this.memberId, projectId: this.id });
    } else {
      this.editMode = false;
      this.clearMemberData();
    }
  }
  private disabled() {
    if (this.editMode && !this.isAdmin) {
      return true;
    }
    return false;
  }

  private mounted() {
    this.getMemberDetails();
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.v-text-field input {
  padding: 3px 0 3px 0;
}
.btn-bottom {
  bottom: 32px;
  position: absolute;
}
</style>

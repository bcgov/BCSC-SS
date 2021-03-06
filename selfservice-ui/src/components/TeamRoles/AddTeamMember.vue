/** * Add team member of app */

<template>
  <v-container>
    <v-row class="text-left" ref="addmember">
      <v-col v-if="userDetails">
        <v-card class="v-form ma-3" flat>
          <v-form ref="form" v-model="valid">
            <v-card class="v-form px-6 pt-2 ma-3">
              <Alert
                type="error"
                class="text-left mt-2"
                v-if="memberErrorStatus"
              >
                <div>
                  <div>{{ $t('addTeamMember.errorTitle') }}</div>
                  <ul>
                    <li
                      v-for="(errors, idx) in errorList"
                      :key="idx"
                      v-html="$t(`addTeamMember.${errors}`)"
                    ></li>
                  </ul>
                </div>
              </Alert>

              <v-row>
                <v-col cols="12">
                  <div class="display-1" v-if="isCurrentUser">
                    {{ $t('addTeamMember.pageTitleEditRole') }}
                  </div>
                  <div class="display-1" v-else>
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
                  <v-card-subtitle class="headline bc-padding-left-0">{{
                    $t('addTeamMember.contactInfo')
                  }}</v-card-subtitle>
                  <Input
                    v-model="userDetails.firstName"
                    :label="$t('addTeamMember.labelFirstName')"
                    :rules="[
                      rules.required,
                      rules.length(1),
                      rules.maxLength(250),
                    ]"
                    type="text"
                    :disabled="disabled()"
                    data-test-id="input-team-first-name"
                    id="input-team-first-name"
                  />
                  <Input
                    v-model="userDetails.lastName"
                    :label="$t('addTeamMember.labelLastName')"
                    :rules="[
                      rules.required,
                      rules.length(1),
                      rules.maxLength(250),
                    ]"
                    type="text"
                    :disabled="disabled()"
                    data-test-id="input-team-last-name"
                    id="input-team-last-name"
                  />
                  <Input
                    v-model="userDetails.email"
                    :label="$t('addTeamMember.labelWorkEmail')"
                    :rules="[rules.required, rules.email, rules.maxLength(250)]"
                    type="text"
                    :disabled="disabled()"
                    data-test-id="input-team-email"
                    id="input-team-email"
                  />

                  <Input
                    v-model="userDetails.phone"
                    :label="$t('addTeamMember.labelPhone')"
                    type="text"
                    :disabled="disabled()"
                    :optional="true"
                    data-test-id="input-team-phone"
                    id="input-team-phone"
                  />
                </v-col>
                <v-col cols="1">
                  <v-divider class="mx-4 d-none d-sm-flex" vertical></v-divider>
                </v-col>
                <v-col cols="12" sm="5" class="p-relative">
                  <v-card-subtitle class="headline bc-padding-left-0">{{
                    $t('addTeamMember.roleTitle')
                  }}</v-card-subtitle>

                  <v-radio-group
                    v-model="userDetails.role"
                    :mandatory="false"
                    data-test-id="radio-team-role"
                  >
                    <v-radio
                      :label="$t(`addTeamMember.labelRoledeveloper`)"
                      :value="projectRoles.developer"
                      class="my-2"
                    ></v-radio>

                    <v-radio
                      :label="$t(`addTeamMember.labelRolemanager`)"
                      :value="projectRoles.manager"
                      class="my-2"
                    ></v-radio>

                    <v-radio
                      :label="$t(`addTeamMember.labelRolecto`)"
                      :value="projectRoles.cto"
                      class="my-2"
                    ></v-radio>
                  </v-radio-group>

                  <div>
                    {{
                      $t(
                        `addTeamMember.labelRoleInfo${
                          projectRoles[userDetails.role]
                        }`
                      )
                    }}
                  </div>
                  <v-card-actions class="btn-bottom">
                    <v-spacer></v-spacer>
                    <Button
                      @click="cancel"
                      @keyup.enter="cancel"
                      aria-label="Back Button"
                      secondary
                      data-test-id="btn-cancel-add-team"
                      >{{ $t('addTeamMember.btnCancel') }}</Button
                    >
                    <Button
                      :disabled="!valid"
                      class="white--text submit-package"
                      @click="submitTeamMember"
                      @keyup.enter="submitTeamMember"
                      data-test-id="btn-submit-add-team"
                    >
                      {{
                        $t(
                          !editMode
                            ? 'addTeamMember.btnSumbmit'
                            : 'addTeamMember.btnSumbmitSave'
                        )
                      }}
                    </Button>
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
import Input from '@/Atomic/Input/Input.vue';
import Button from '@/Atomic/Button/Button.vue';
import Alert from '@/Atomic/Alert/Alert.vue';

import validationRules from '@/config/validationRules';
import { projectRoles } from '@/constants/enums';
import { TeamRoleModel } from '@/models/TeamRoleModel';
import { memberDetails } from '@/store/modules/TeamRoles/defaults';

const TeamRolesModule = namespace('TeamRolesModule');
const KeyCloakModule = namespace('KeyCloakModule');

@Component({
  components: {
    Input,
    Button,
    Alert,
  },
})
export default class AddTeamMember extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  @Prop()
  public toggleAddMember: any;
  @Prop({ default: 0 })
  public memberId!: number;
  @Prop({ default: false })
  public isCurrentUser!: boolean;

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
  @TeamRolesModule.Action('clearErrors')
  public clearErrors!: any;

  public errorList: any = {};

  public userDetails: TeamRoleModel;

  @KeyCloakModule.Getter('isAdmin')
  private isAdmin!: any;

  private rules: any = validationRules;
  private projectRoles: any = projectRoles;
  private selectedRole: any = 1;
  private valid: boolean = false;
  private editMode: boolean = false;

  public constructor() {
    super();
    this.userDetails = memberDetails();
  }

  @Watch('getMemberErrorList')
  private ongetMemberErrorListChanged(val: any) {
    this.errorList = val;

    (this.$refs.addmember as Vue & {
      scrollIntoView: ({}) => any;
    }).scrollIntoView({
      behavior: 'smooth',
    });
  }

  @Watch('memberDetails')
  private ongetmemberDetailsChanged(val: any) {
    this.userDetails = { ...val };
    this.resetValidation();
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
        memberId: this.memberId,
      });
    } else {
      this.addTeamMember({
        userDetails: this.userDetails,
        projectId: this.id,
      });
    }
    this.resetValidation();
  }
  private getMemberDetails() {
    if (this.memberId !== 0) {
      this.editMode = true;
      this.getTeamMember({ memberId: this.memberId, projectId: this.id });
    } else {
      this.editMode = false;
      this.clearMemberData();
    }
    this.resetValidation();
  }
  private resetValidation() {
    // to fix typescript error
    (this.$refs.form as Vue & {
      resetValidation: () => any;
    }).resetValidation();
  }
  private disabled() {
    if (this.editMode && !this.isAdmin) {
      return true;
    }
    return false;
  }
  private cancel() {
    this.resetValidation();
    this.clearErrors();
    this.userDetails = memberDetails();
    this.$emit('toggleAddMember', false);
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
  flex-direction: column;
  width: 100%;

  @include sm {
    bottom: 32px;
    position: absolute;
  }
  & .btn {
    width: 100%;
    margin-top: 12px;
    margin-left: 0px !important;
  }
  @include rwd('1260') {
    bottom: 32px;
    position: absolute;
    flex-direction: row;
    width: auto;
    & .btn {
      width: auto;
      margin-top: 0;
      margin-left: 8px !important;
    }
  }
}
.p-relative {
  position: relative;
}
</style>

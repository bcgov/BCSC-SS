/** * Project information */
<template>
  <v-card class="mx-auto outer-card">
    <v-card class="mx-auto">
      <v-app-bar dark class="bc-subtitle">
        <v-btn icon @click="$router.push('/dashboard/')" aria-label="Back Button">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
        <v-toolbar-title>
          {{
          $t('projectInfo.ProjectInfoTitle')
          }}
        </v-toolbar-title>
        <v-spacer></v-spacer>
      </v-app-bar>
      <v-form ref="form" v-model="form">
        <v-container>
          <v-row dense>
            <v-col cols="12" md="12">
              <v-card class="pa-8 pt-6 ma-3">
                <v-card-title class="headline bc-padding-left-0">
                  {{
                  $t('projectInfo.ProjectInfoTitle')
                  }}
                </v-card-title>
                <v-card-subtitle
                  class="text-left bc-padding-left-0"
                  v-html="$t('projectInfo.ProjectInfoTitleInfo')"
                ></v-card-subtitle>
                <v-card-subtitle
                  class="font-weight-bold text-left bc-padding-left-0"
                >{{ $t('projectInfo.ProjectOrgTitle') }}</v-card-subtitle>

                <Input
                  v-model="organizationName"
                  :label="$t('projectInfo.OrganizationName')"
                  type="text"
                  :rules="[
                    rules.required,
                    rules.length(2),
                    rules.maxLength(100)
                  ]"
                  :helpText="$t('projectInfo.OrganizationNameHint')"
                />

                <Input
                  v-model="projectName"
                  :label="$t('projectInfo.projectName')"
                  type="text"
                  :rules="[
                    rules.required,
                    rules.length(2),
                    rules.maxLength(100)
                  ]"
                  :helpText="$t('projectInfo.projectNameHint')"
                />

                <TextArea
                  v-model="description"
                  :label="$t('projectInfo.Description')"
                  type="text"
                  :rules="[rules.required]"
                  outlined
                  :helpText="$t('projectInfo.DescriptionHint')"
                />
              </v-card>
            </v-col>

            <v-col cols="12">
              <v-card class="pa-8 pt-6 ma-3">
                <v-card-title class="headline bc-padding-left-0">
                  {{
                  $t('projectInfo.ProjectRoles')
                  }}
                </v-card-title>
                <v-card-subtitle class="text-left bc-padding-left-0">
                  {{
                  $t('projectInfo.RolesTitleInfo')
                  }}
                </v-card-subtitle>
                <v-radio-group v-model.number="myRole" row color="black">
                  <span class="mr-2">{{ $t('projectInfo.myRole') }}</span>
                  <v-radio class="black-color" v-bind:value="projectRoles.developer">
                    <template v-slot:label>
                      <span class="black-color">
                        {{
                        $t('projectInfo.DeveloperRole')
                        }}
                      </span>
                    </template>
                  </v-radio>
                  <v-radio label="Manager" v-bind:value="projectRoles.manager">
                    <template v-slot:label>
                      <span class="black-color">
                        {{
                        $t('projectInfo.ManagerRole')
                        }}
                      </span>
                    </template>
                  </v-radio>
                  <v-radio v-bind:value="projectRoles.cto">
                    <template v-slot:label>
                      <span class="black-color">
                        {{
                        $t('projectInfo.CTORole')
                        }}
                      </span>
                    </template>
                  </v-radio>
                </v-radio-group>
              </v-card>
            </v-col>

            <v-col cols="12" sm="6" v-if="myRole !== projectRoles.manager">
              <ProjectUsers
                :userDetails="getUserDetailsByRole(users, projectRoles.manager)"
                :rules="rules"
                :title="$t('projectInfo.ManagerRole')"
                :hint="$t('projectInfo.managerHint')"
              />
            </v-col>
            <v-col cols="12" sm="6" v-if="myRole !== projectRoles.cto">
              <ProjectUsers
                :userDetails="getUserDetailsByRole(users, projectRoles.cto)"
                :rules="rules"
                :title="$t('projectInfo.CTORole')"
                :hint="$t('projectInfo.ctoHint')"
              />
            </v-col>
            <v-col cols="12" sm="6" v-if="myRole !== projectRoles.developer">
              <ProjectUsers
                :userDetails="
                  getUserDetailsByRole(users, projectRoles.developer)
                "
                :rules="rules"
                :title="$t('projectInfo.DeveloperRole')"
                :hint="$t('projectInfo.developerHint')"
              />
            </v-col>

            <v-col cols="12">
              <v-card flat>
                <v-divider></v-divider>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <Button
                    @click="$router.push(`/project/${id}/summary/`)"
                    aria-label="Back Button"
                    secondary
                    v-if="!showWizardExperience()"
                  >{{ $t('projectInfo.btnCancel') }}</Button>
                  <Button
                    :disabled="!form"
                    :loading="isLoading"
                    class="white--text submit-project"
                    depressed
                    @click="submitProjectInfo"
                    @keyup.enter="submitProjectInfo"
                  >
                    {{
                    $t(
                    showWizardExperience()
                    ? 'projectInfo.btnNext'
                    : 'projectInfo.btnSaveChanges'
                    )
                    }}
                  </Button>
                </v-card-actions>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </v-card>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Watch, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import { ProjectUserModel, ProjectInfoModel } from '@/models/ProjectInfoModel';
import Input from '@/Atomic/Input/Input.vue';
import TextArea from '@/Atomic/TextArea/TextArea.vue';
import Button from '@/Atomic/Button/Button.vue';
import ProjectUsers from './ProjectUsers.vue';
import validationRules from '@/config/validationRules';
import { projectRoles } from '@/constants/enums';

const ProjectInfoModule = namespace('ProjectInfoModule');
const SharedModule = namespace('SharedModule');

@Component({ components: { Input, TextArea, Button, ProjectUsers } })
export default class AddProjectInfo extends Vue {
  @Prop({ default: '' })
  public id!: string;
  @Prop({ default: '' })
  public action!: string;

  @ProjectInfoModule.Getter('successStatus') public successStatus!: boolean;
  @ProjectInfoModule.Getter('errorStatus') public errorStatus!: boolean;
  @ProjectInfoModule.Action('addProjectInfo') public addProjectInfoStore!: any;
  @ProjectInfoModule.Action('loadProjectInfo')
  public loadProjectInfo!: any;
  @ProjectInfoModule.Getter('getSingleProjectInfo')
  public getSingleProjectInfo!: any;
  @ProjectInfoModule.Action('updateProjectInfo')
  public updateProjectInfoStore!: any;
  @ProjectInfoModule.Action('loadSingleProjectInfo')
  public loadSingleProjectInfo!: any;

  @SharedModule.Getter('isRedirectFromSummaryPage')
  public isRedirectFromSummaryPage!: boolean;
  @SharedModule.Action('redirectFromSummaryPage')
  public redirectFromSummaryPage!: any;

  public form: boolean = false;
  private isLoading: boolean = false;
  private organizationName: string = '';
  private projectName: string = '';
  private description: string = '';
  private myRole: number = 1;
  private users: ProjectUserModel[] = [
    {
      email: '',
      phone: '',
      firstName: '',
      lastName: '',
      role: projectRoles.developer
    },
    {
      email: '',
      phone: '',
      firstName: '',
      lastName: '',
      role: projectRoles.manager
    },
    {
      email: '',
      phone: '',
      firstName: '',
      lastName: '',
      role: projectRoles.cto
    }
  ];
  private projectRoles: any = projectRoles;
  private isEditMode: boolean = false;
  /* istanbul ignore next */
  private rules = validationRules;

  @Watch('getSingleProjectInfo')
  private ongetSingleProjectInfoChanged(val: any) {
    this.updteEdit(val);
  }

  private submitProjectInfo() {
    // to fix change below line
    const selectedUserIdx = this.users.filter(user => {
      return user.role !== this.myRole;
    });

    const data: ProjectInfoModel = {
      organizationName: this.organizationName,
      projectName: this.projectName,
      description: this.description,
      myRole: this.myRole,
      users: selectedUserIdx
    };

    if (this.isEditMode) {
      data.id = this.id;
      this.updateProjectInfoStore(data);
      if (!this.showWizardExperience()) {
        this.redirectFromSummaryPage(true);
      }
    } else {
      this.addProjectInfoStore(data);
      this.redirectFromSummaryPage(false);
    }
  }

  private getUserDetailsByRole(users: any, selectedRole: number) {
    return users.find((userData: any) => userData.role === selectedRole);
  }

  private updteEdit(val: any) {
    this.organizationName = val.organizationName;
    this.projectName = val.projectName;
    this.description = val.description;
    this.myRole = val.myRole;
    this.users = val.users;
    // this.id = val.id;
    this.isEditMode = true;
  }

  private mounted() {
    this.isEditMode = false;
    if (this.id !== '') {
      this.isEditMode = true;
      this.loadSingleProjectInfo(this.id);
    }
  }

  private showWizardExperience() {
    if (this.isEditMode && this.isRedirectFromSummaryPage) {
      return false;
    }
    return true;
  }
}
</script>

<style lang="scss" scoped>
.black-color {
  color: #000 !important;
}
</style>

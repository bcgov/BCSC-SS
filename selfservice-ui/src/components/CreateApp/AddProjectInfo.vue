/** * Project information */
<template>
  <v-card class="mx-auto" style="max-width: 80%;">
    <v-card class="mx-auto">
      <v-app-bar dark class="bc-subtitle">
        <v-btn icon @click="$router.push('/project/')" aria-label="Back Button">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
        <v-toolbar-title>Project information</v-toolbar-title>
        <v-spacer></v-spacer>
      </v-app-bar>
      <v-form ref="form" v-model="form">
        <v-container>
          <v-row dense>
            <v-col cols="12" md="12">
              <v-card class="pa-4 pt-6">
                <v-card-title class="headline">Project information</v-card-title>
                <v-card-subtitle class="text-left">Tell us about your Project</v-card-subtitle>
                <Input
                  v-model="organizationName"
                  counter="100"
                  label="Organization name"
                  type="text"
                  :rules="[
                    rules.required,
                    rules.length(2),
                    rules.maxLength(100)
                  ]"
                />
                <Input
                  v-model="projectName"
                  counter="100"
                  label="Project name"
                  type="text"
                  :rules="[
                    rules.required,
                    rules.length(2),
                    rules.maxLength(100)
                  ]"
                />
                <TextArea
                  v-model="description"
                  label="Description"
                  type="text"
                  :rules="[rules.required]"
                />
              </v-card>
            </v-col>

            <v-col cols="12">
              <v-card class="pa-4 pt-6">
                <v-card-title class="headline">Project Roles</v-card-title>
                <v-card-subtitle class="text-left">Tell us about your role in this project</v-card-subtitle>
                <v-radio-group v-model.number="myRole" row>
                  I am
                  <v-radio label="Developer" v-bind:value="1"></v-radio>
                  <v-radio label="Manager" v-bind:value="2"></v-radio>
                  <v-radio label="CTO" v-bind:value="3"></v-radio>For this project
                </v-radio-group>
              </v-card>
            </v-col>

            <!-- <v-form ref="form" v-model="form" class="pa-4 pt-6"> -->
            <v-col cols="12" sm="6" v-if="myRole !== 2">
              <ProjectUsers :userDetails="users[1]" :rules="rules" title="Manager" />
            </v-col>
            <v-col cols="12" sm="6" v-if="myRole !== 3">
              <ProjectUsers :userDetails="users[2]" :rules="rules" title="CTO" />
            </v-col>
            <v-col cols="12" sm="6" v-if="myRole !== 1">
              <ProjectUsers :userDetails="users[0]" :rules="rules" title="Developer" />
            </v-col>

            <v-col cols="12">
              <v-card flat>
                <v-divider></v-divider>
                <v-card-actions>
                  <!-- <v-btn text @click="$refs.form.reset()">Clear</v-btn> -->
                  <v-spacer></v-spacer>
                  <Button
                    :disabled="!form"
                    :loading="isLoading"
                    class="white--text"
                    color="indigo accent-4"
                    depressed
                    @click="addProjectInfo"
                  >Next</Button>
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

const ProjectInfoModule = namespace('ProjectInfoModule');

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
      role: 1
    },
    {
      email: '',
      phone: '',
      firstName: '',
      lastName: '',
      role: 2
    },
    {
      email: '',
      phone: '',
      firstName: '',
      lastName: '',
      role: 3
    }
  ];

  private isEditmode: boolean = false;
  /* istanbul ignore next */
  private rules = validationRules;

  @Watch('getSingleProjectInfo')
  private ongetSingleProjectInfoChanged(val: any) {
    this.updteEdit(val);
  }

  private addProjectInfo() {
    // to fix change below line
    const selectedUserIdx = this.users.filter(user => {
      return user.role !== this.myRole;
    });

    // const usersList = this.users.splice(1, 2);
    // console.log('usersList', usersList);
    const data: ProjectInfoModel = {
      organizationName: this.organizationName,
      projectName: this.projectName,
      description: this.description,
      myRole: this.myRole,
      users: selectedUserIdx
    };

    if (this.isEditmode) {
      data.id = this.id;
      this.updateProjectInfoStore(data);
    } else {
      this.addProjectInfoStore(data);
    }
    // (this.$refs.form as HTMLFormElement).reset();
    // this.$router.push('/project/technical/');
  }

  private updteEdit(val: any) {
    this.organizationName = val.organizationName;
    this.projectName = val.projectName;
    this.description = val.description;
    this.myRole = val.myRole;
    this.users = this.users;
    // this.id = val.id;
    this.isEditmode = true;
  }

  private mounted() {
    this.isEditmode = false;
    if (this.id !== '') {
      this.isEditmode = true;
      this.loadSingleProjectInfo(this.id);
    }
  }
  private input(value: string) {
    // console.log('value', value);
  }
}
</script>

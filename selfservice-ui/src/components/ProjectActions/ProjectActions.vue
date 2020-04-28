/** * Dashboard of app */

<template>
  <div>
    <v-col
      cols="12"
      class="d-flex justify-end"
      v-if="projectStatus === projectStatusList.development"
      no-gutters
    >
      <v-card flat>
        <Button
          @click="toggleWarning()"
          :aria-label="$t('projectActions.btnRequestLiveAccess')"
          class="btn-req"
          secondary
        >{{ $t('projectActions.btnRequestLiveAccess') }}</Button>
      </v-card>
    </v-col>

    <v-col
      class="d-flex justify-end btn-delete pad-0"
      @click="toggleDelete()"
      v-if="isAdmin || projectStatus < projectStatusList.developmentComplete"
      no-gutters
    >
      <v-icon class="ml-2 icon-delete" small>mdi-delete</v-icon>
      {{ $t('projectActions.labelDelete') }}
    </v-col>

    <v-col v-if="requestDialog || deleteDialog">
      <v-dialog v-model="requestDialog" persistent max-width="70%">
        <v-card>
          <v-toolbar flat class="bc-subtitle" dark>
            <v-toolbar-title>
              {{
              $t('projectActions.requestLiveAccessDialogTitle')
              }}
            </v-toolbar-title>
          </v-toolbar>
          <v-card-text
            class="text-left ma-8"
            v-html="$t('projectActions.requestLiveAccessDialogInfo')"
          ></v-card-text>
          <v-card-actions class="pb-10">
            <v-spacer></v-spacer>
            <Button secondary text @click="toggleWarning()">
              {{
              $t('projectActions.btnCancel')
              }}
            </Button>
            <Button text class="btn-live" @click="confirmLiveAccess()">
              {{
              $t('projectActions.btnConfirm')
              }}
            </Button>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <v-dialog v-model="deleteDialog" persistent max-width="70%">
        <v-card>
          <v-toolbar flat class="bc-subtitle" dark>
            <v-toolbar-title>
              <v-icon class="ml-2" medium>mdi-delete</v-icon>
              {{ $t('projectActions.deleteDialogTitle') }}
            </v-toolbar-title>
          </v-toolbar>
          <v-card-text class="text-left ma-8" v-html="$t('projectActions.deleteDialogInfo')"></v-card-text>
          <v-card-actions class="pb-10">
            <v-spacer></v-spacer>
            <Button secondary text @click="toggleDelete()">
              {{
              $t('projectActions.btnDeleteCancel')
              }}
            </Button>
            <Button
              text
              class="dialog-delete"
              @click="confirmDeleteProject()"
            >{{ $t('projectActions.btnDeleteConfirm') }}</Button>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-col>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';

import Button from '@/Atomic/Button/Button.vue';
import { projectStatus } from '@/constants/enums';

const ProjectInfoModule = namespace('ProjectInfoModule');
const KeyCloakModule = namespace('KeyCloakModule');

@Component({
  components: {
    Button
  }
})
export default class ProjectActions extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  @ProjectInfoModule.Getter('getChangeStatus')
  public getChangeStatus!: any;
  @ProjectInfoModule.Action('updateProjectStatus')
  public updateProjectStatus!: any;

  @ProjectInfoModule.Getter('getDeleteProjectReturn')
  public getDeleteProjectReturn!: any;
  @ProjectInfoModule.Action('deleteProject')
  public deleteProject!: any;

  @ProjectInfoModule.Getter('getSingleProjectInfo')
  public getSingleProjectInfo!: any;

  @KeyCloakModule.Getter('isAdmin')
  private isAdmin!: any;

  private requestDialog: boolean = false;
  private deleteDialog: boolean = false;

  private showProjectActions: boolean = false;
  private projectStatus: number = 1;
  private projectStatusList: any = projectStatus;

  @Watch('getChangeStatus')
  private ongetChangeStatusChanged(val: any) {
    const { statusChangeError, statusChangeSuccess } = val;
    this.toggleWarning();
    if (statusChangeSuccess === true) {
      this.$router.push(`/project-container/${this.id}`);
    }
  }
  @Watch('getDeleteProjectReturn')
  private ongetgetDeleteProjectReturnChanged(val: any) {
    const { deleteProjectError, deleteProjectSuccess } = val;

    if (deleteProjectSuccess === true) {
      this.$router.push('/dashboard');
    }
  }

  /** this watch will get called on load of projectinfo summary page which loads as child */
  @Watch('getSingleProjectInfo')
  private ongetSingleProjectInfoChanged(val: any) {
    if (val && val.statusId > 1) {
      this.showProjectActions = true;
      this.projectStatus = val.statusId;
    }
  }

  private toggleWarning() {
    this.requestDialog = !this.requestDialog;
  }

  private toggleDelete() {
    this.deleteDialog = !this.deleteDialog;
  }

  private confirmLiveAccess() {
    this.updateProjectStatus({
      projectId: this.id,
      statusId: projectStatus.developmentComplete
    });
  }
  private confirmDeleteProject() {
    this.deleteProject({ projectId: this.id });
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';

.btn-delete {
  color: $BCgovBlue10;
  cursor: pointer;
  & .icon-delete {
    color: $BCgovBlue10;
  }
}
.pad-0 {
  padding: 0 12px;
}
</style>

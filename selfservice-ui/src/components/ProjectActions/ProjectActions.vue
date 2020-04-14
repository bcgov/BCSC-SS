/** * Dashboard of app */

<template>
  <div class="right-side">
    <v-col cols="12" class="d-flex justify-end">
      <v-card flat>
        <Button
          @click="toggleWarning()"
          :aria-label="$t('projectActions.btnRequestLiveAccess')"
          class="team-roles"
          secondary
          >{{ $t('projectActions.btnRequestLiveAccess') }}</Button
        >
      </v-card>
    </v-col>
    <v-col class="d-flex justify-end btn-delete">
      <!-- <div> -->
      <v-icon
        @click="deleteMemberDialog(team.id)"
        class="ml-2 btn-delete "
        small
        >mdi-delete</v-icon
      >{{ $t('projectActions.labelDelete') }}
      <!-- </div> -->
    </v-col>

    <v-col>
      <v-dialog v-model="requestDialog" persistent max-width="70%">
        <v-card>
          <v-toolbar flat class="bc-subtitle" dark>
            <v-toolbar-title>{{
              $t('projectActions.requestLiveAccessDialogTitle')
            }}</v-toolbar-title>
          </v-toolbar>
          <v-card-text
            class="text-left"
            v-html="$t('projectActions.requestLiveAccessDialogInfo')"
          ></v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <Button secondary text @click="toggleWarning()">{{
              $t('projectActions.btnCancel')
            }}</Button>
            <Button text @click="confirmLiveAccess()">{{
              $t('projectActions.btnConfirm')
            }}</Button>
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

import { projectRolesList } from '@/constants/enums';

const ProjectInfoModule = namespace('ProjectInfoModule');
// const KeyCloakModule = namespace('KeyCloakModule');

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

  private requestDialog: boolean = false;

  @Watch('getChangeStatus')
  private ongetChangeStatusChanged(val: any) {
    const { statusChangeError, statusChangeSuccess } = val;
    this.toggleWarning();
  }

  private toggleWarning() {
    this.requestDialog = !this.requestDialog;
  }

  private confirmLiveAccess() {
    this.updateProjectStatus({
      projectId: this.id,
      statusId: projectStatus.developmentComplete
    });
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.right-side {
  margin-right: -25px;
}
.btn-delete {
  color: $BCgovBlue10;
  cursor: pointer;
}
</style>

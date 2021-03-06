/** * Dashboard of app */

<template>
  <v-card class="mx-auto outer-card">
    <v-container>
      <v-row class="ma-5">
        <v-col cols="12" v-if="isLoading">
          <Loading />
        </v-col>
        <v-col cols="8" v-else>
          <h1 class="text-left tab-headline">{{ projectInfo && projectInfo.projectName }}</h1>
          <div
            class="text-left tab-headline font-weight-medium my-2"
          >{{ projectInfo && projectInfo.organizationName }}</div>
        </v-col>
        <v-col cols="4" class="d-flex align-end flex-column-reverse mb-2" v-show="!isLoading">
          <ProjectActions :id="id" />
        </v-col>

        <v-col cols="12">
          <v-tabs slider-color="d-none" v-model="selectedTab">
            <v-tab class="font-weight-bold">
              {{
              $t('projectContainer.titleDevSummary')
              }}
            </v-tab>
            <v-tab class="font-weight-bold">
              {{
              $t('projectContainer.titleTeamRoles')
              }}
            </v-tab>
            <v-tab class="font-weight-bold">
              {{
              $t('projectContainer.titleCompliance')
              }}
            </v-tab>
            <v-tab class="font-weight-bold">
              {{
              $t('projectContainer.titleHistory')
              }}
            </v-tab>
            <v-tab-item class="custom-tabs-items" tabindex="0">
              <v-card flat>
                <v-card-text>
                  <ProjectSummary :id="id" />
                </v-card-text>
              </v-card>
            </v-tab-item>
            <v-tab-item class="custom-tabs-items" tabindex="0">
              <v-card flat>
                <v-card-text>
                  <TeamRoles :id="id" />
                </v-card-text>
              </v-card>
            </v-tab-item>

            <v-tab-item class="custom-tabs-items" tabindex="0">
              <v-card flat>
                <v-card-text>
                  <ProjectCompliance />
                </v-card-text>
              </v-card>
            </v-tab-item>
            <v-tab-item class="custom-tabs-items" tabindex="0">
              <v-card flat>
                <v-card-text>
                  <p>
                    <ProjectHistory :id="id" />
                  </p>
                </v-card-text>
              </v-card>
            </v-tab-item>
          </v-tabs>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import ProjectSummary from '@/components/CreateApp/ProjectSummary.vue';
import Loading from '@/Atomic/Loading/Loading.vue';

import TeamRoles from '@/components/TeamRoles/TeamRoles.vue';
import ProjectActions from '@/components/ProjectActions/ProjectActions.vue';
import ProjectHistory from '@/components/ProjectContainer/ProjectHistory.vue';
import ProjectCompliance from '@/components/ProjectContainer/ProjectCompliance.vue';

const ProjectInfoModule = namespace('ProjectInfoModule');

@Component({
  components: {
    ProjectSummary,
    Loading,
    TeamRoles,
    ProjectActions,
    ProjectHistory,
    ProjectCompliance
  }
})
export default class ProjectContainer extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  @ProjectInfoModule.Getter('getSingleProjectInfo')
  public projectInfo!: any;
  @ProjectInfoModule.Action('loadSingleProjectInfo')
  public loadSingleProjectInfo!: any;

  private isLoading: boolean = true;
  private selectedTab: number = 0;

  @Watch('projectInfo')
  private ongetprojectInfoChanged(val: any) {
    this.isLoading = false;
  }

  private mounted() {
    this.isLoading = true;

    if (this.id === 0) {
      this.$router.push('/unauthorized');
    }
    if (this.projectInfo && this.projectInfo.id !== this.id) {
      this.loadSingleProjectInfo(this.id);
    }
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.custom-tabs-items {
  border: 1px solid $gray5;
  min-height: 300px; // temp fix
}
.v-tab {
  color: $BCgovFontColorInvertedDark !important;
}
.v-tab--active {
  border: 1px solid $gray5;
  background-color: $BCgovGold5;
  color: $BCgovWhite !important;
}
.tab-headline {
  color: $BCgovFontColorInvertedDark;
}
</style>

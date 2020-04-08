/* AddTeam component */
<template>
  <v-card class="mx-auto outer-card">
    <v-toolbar flat class="bc-subtitle" dark>
      <v-btn icon @click="goBack()" :aria-label="$t('team.btnBack')">
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <v-toolbar-title>{{ $t('team.pageTitle') }}</v-toolbar-title>
      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-divider></v-divider>
    <v-col cols="12">
      <TeamRoles :id="id" />
    </v-col>
    <v-col cols="12">
      <v-card flat class="ma-5">
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <Button @click="goBack" :aria-label="$t('team.btnBack')" secondary class="back-btn">
            {{
            $t(
            showWizardExperience()
            ? 'team.btnBack'
            : 'team.btnCancel'
            )
            }}
          </Button>
          <Button class="white--text ml-6" depressed @click="nextRedirect">
            {{
            $t(
            showWizardExperience()
            ? 'team.btnNext'
            : 'team.btnSaveChanges'
            )
            }}
          </Button>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Watch, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import Button from '@/Atomic/Button/Button.vue';
import TeamRoles from '@/components/TeamRoles/TeamRoles.vue';
const SharedModule = namespace('SharedModule');

@Component({
  components: {
    Button,
    TeamRoles
  }
})
export default class AddTeam extends Vue {
  @Prop({ default: 0 })
  public id!: number;

  @SharedModule.Action('redirectFromSummaryPage')
  public redirectFromSummaryPage!: any;
  @SharedModule.Getter('isRedirectFromSummaryPage')
  public isRedirectFromSummaryPage!: boolean;

  private projectId: number = this.id || 0;

  private goBack() {
    const redirectPage = this.showWizardExperience() ? 'info' : 'summary';
    this.redirectFromSummaryPage(false);
    this.$router.push(`/project/${this.projectId}/${redirectPage}/`);
  }
  private showWizardExperience() {
    if (this.isRedirectFromSummaryPage) {
      return false;
    }
    return true;
  }

  private nextRedirect() {
    const redirectPage = this.showWizardExperience() ? 'technical' : 'summary';
    this.$router.push(`/project/${this.projectId}/${redirectPage}/`);
  }
}
</script>

<style lang="scss" scoped>
</style>

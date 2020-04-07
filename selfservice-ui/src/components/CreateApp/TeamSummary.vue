/** * TeamSummary component */

<template>
  <v-card>
    <Loading v-if="isLoading" />
    <v-toolbar dense class="bc-subtitle-2" dark v-else>
      <v-card-title>
        {{ $t('summaryPage.teamTitle') }}
        <v-spacer></v-spacer>
        <v-icon small class="ml-3" @click="$router.push(`/project/${id}/team`)">mdi-pencil</v-icon>
      </v-card-title>
    </v-toolbar>

    <v-list dense class="px-5" v-if="!isLoading">
      <template v-for="(member, index) in team">
        <v-list-item :key="member.id">
          <v-list-item-content class="align-self-start pr-30">
            {{
            $t(`summaryPage.${rolesList[member.role]}`)
            }}
            <span
              class="small-hint pad-50"
              v-html="$t(`summaryPage.${rolesList[member.role]}Hint`)"
            ></span>
          </v-list-item-content>
          <v-list-item-content class="align-end">
            <div>
              <v-icon small class="mr-1">mdi-account</v-icon>
              {{ member.firstName }}
              {{ member.lastName }}
            </div>
            <div v-if="member.phone !== ''" class="ml-6">{{ member.phone }}</div>
            <div v-if="member.email !== ''" class="ml-6">{{ member.email }}</div>
          </v-list-item-content>
        </v-list-item>
        <v-divider :key="`divider-${member.id}`" v-if="index < team.length - 1"></v-divider>
      </template>
    </v-list>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import { projectRolesList } from '@/constants/enums';
import Loading from '@/Atomic/Loading/Loading.vue';

const TeamModule = namespace('TeamRolesModule');

@Component({
  components: { Loading }
})
export default class TeamSummary extends Vue {
  @Prop({ default: 0 })
  public id!: number;

  @TeamModule.Getter('getTeamList')
  public team!: any;
  @TeamModule.Action('loadTeam')
  public loadTeam!: any;

  private isLoading: boolean = true;
  private rolesList: any = projectRolesList;

  @Watch('team')
  private onTeamChanged(val: any) {
    this.isLoading = false;
  }

  private mounted() {
    this.isLoading = true;
    this.loadTeam(this.id);
  }
}
</script>

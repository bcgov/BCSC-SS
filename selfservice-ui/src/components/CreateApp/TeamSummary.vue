/** * TeamSummary component */

<template>
  <v-card class="mt-5" :class="!isTeamAvailable ? 'red-border' : ''">
    <v-toolbar dense class="bc-subtitle-2" dark>
      <v-card-title>
        {{ $t('summaryPage.teamTitle') }}
        <v-spacer></v-spacer>

        <span
          @click="$router.push(`/project/${id}/team`)"
          @keyup.enter="$router.push(`/project/${id}/team`)"
          class="edit-wrapper"
          :aria-label="$t('global.edit')"
          tabindex="0"
          role="link"
        >
          <v-icon small class="ml-3">mdi-pencil</v-icon>
        </span>
      </v-card-title>
    </v-toolbar>

    <v-list dense class="px-5">
      <template v-for="(member, index) in team">
        <v-list-item :key="member.id">
          <v-list-item-content class="align-self-start pr-30">
            {{ $t(`summaryPage.${rolesList[member.role]}`) }}
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
import { projectRoles } from '@/constants/enums';

@Component
export default class TeamSummary extends Vue {
  @Prop({ default: 0 })
  public id!: number;

  @Prop({ default: [] })
  public team!: any;

  @Prop({ default: false })
  public isTeamAvailable!: boolean;

  private rolesList: any = projectRoles;
}
</script>

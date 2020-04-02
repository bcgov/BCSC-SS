/** * ClientID component */

<template>
  <v-card class="mx-auto mb-5" v-if="technicalReq">
    <v-toolbar dense class="bc-subtitle-2" dark>
      <v-card-title>
        {{ $t('summaryPage.labelTestAccountsTitle') }}
        <v-icon
          small
          class="ml-3"
          @click="$router.push(`/project/${projectId}/test-account`)"
        >mdi-pencil</v-icon>
      </v-card-title>
    </v-toolbar>
    <v-list dense class="px-5">
      <v-list-item>
        <v-list-item-content class="pr-30">
          {{
          $t('summaryPage.labelTestAccounts')
          }}
        </v-list-item-content>

        <v-list-item-content class="align-end">
          <div v-if="technicalReq.noOfTestAccount">
            <span class="font-weight-bold">{{ technicalReq.noOfTestAccount }}</span>
            {{$t('summaryPage.labelTestAccountNumber')}}
          </div>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
const ClientIdModule = namespace('ClientIdModule');

@Component({
  components: {}
})
export default class ClientIDDetails extends Vue {
  @Prop({ default: 0 })
  public projectId!: number;
  @Prop({ default: {} })
  public technicalReq!: any;
}
</script>


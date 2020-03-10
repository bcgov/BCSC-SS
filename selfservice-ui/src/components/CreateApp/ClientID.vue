/** * ClientID component */

<template>
  <v-card class="mx-auto mb-5" v-if="getApiData.oidcConfig && getApiData.oidcConfig.clientSecret">
    <v-snackbar v-model="snackbar" :timeout="timeout">
      {{ text }}
      <v-btn color="blue" text @click="snackbar = false">{{ $t('ClientID.labelSnackbarClose') }}</v-btn>
    </v-snackbar>
    <Loading v-if="isLoading && getApiData === 0" />
    <v-toolbar dense class="bc-subtitle-gold-1" dark>
      <v-card-title>{{ $t('ClientID.pagetitle') }}</v-card-title>
    </v-toolbar>
    <v-list dense class="px-5">
      <v-list-item>
        <v-list-item-content>
          {{
          $t('ClientID.titleApiKey')
          }}
          <span
            class="small-hint pad-50"
            v-html="$t('ClientID.titleApiKeyInfo')"
          ></span>
        </v-list-item-content>
        <v-list-item-content
          class="align-end pointer font-weight-bold client-id-copy"
          @click="
                  docopy(
                    getApiData.oidcConfig && getApiData.oidcConfig.clientId
                  )
                "
        >
          <div>
            <v-icon small class="mr-1">mdi-content-copy</v-icon>
            {{ getApiData.oidcConfig && getApiData.oidcConfig.clientId }}
          </div>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>

      <v-list-item>
        <v-list-item-content>
          {{
          $t('ClientID.titleClientSecret')
          }}
          <span
            class="small-hint pad-50"
            v-html="$t('ClientID.titleClientSecretInfo')"
          ></span>
        </v-list-item-content>
        <v-list-item-content
          class="align-end pointer font-weight-bold d-block"
          @click="
                  docopy(
                    getApiData.oidcConfig && getApiData.oidcConfig.clientSecret
                  )
                "
        >
          <div class="float-left">
            <v-icon small class="mr-2">mdi-content-copy</v-icon>
          </div>
          <div>
            <span>{{ getApiData.oidcConfig && getApiData.oidcConfig.clientSecret }}</span>
          </div>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>
      <v-list-item>
        <v-list-item-content class="align-self-start">
          {{
          $t('ClientID.titleTestAccount')
          }}
          <span
            class="small-hint pad-50"
            v-html="$t('ClientID.titleTestAccountInfo')"
          ></span>
        </v-list-item-content>
        <v-list-item-content class="align-self-start">
          <v-simple-table dense>
            <template v-slot:default>
              <thead>
                <tr>
                  <th
                    :scope="$t('ClientID.tblCardNo')"
                    class="text-left"
                  >{{$t('ClientID.tblCardNo')}}</th>
                  <th
                    :scope="$t('ClientID.tblPassCode')"
                    class="text-left"
                  >{{$t('ClientID.tblPassCode')}}</th>
                  <th
                    :scope="$t('ClientID.tblGivenName')"
                    class="text-left"
                  >{{$t('ClientID.tblGivenName')}}</th>
                  <th
                    :scope="$t('ClientID.tblSurName')"
                    class="text-left"
                  >{{$t('ClientID.tblSurName')}}</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(account) in getApiData.testAccount" :key="account.cardNumber">
                  <td>{{ account.cardNumber }}</td>
                  <td>{{ account.passcode }}</td>
                  <td>{{ account.attributes.givenname }}</td>
                  <td>{{ account.attributes.surname }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import Loading from '@/Atomic/Loading/Loading.vue';
const ClientIdModule = namespace('ClientIdModule');

@Component({
  components: {
    Loading
  }
})
export default class ClientIDDetails extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  @ClientIdModule.Getter('errorStatus') public errorStatus!: boolean;
  @ClientIdModule.Action('getClientIdDetails')
  public getClientIdDetails!: any;
  @ClientIdModule.Getter('getApiData') public getApiData!: [];
  @ClientIdModule.Getter('isLoading') public isLoading!: boolean;

  private projectId: number = this.id || 0;
  private snackbar: boolean = false;
  private text: string = 'Copied';
  private timeout: number = 2000;

  public docopy(message: any) {
    this.$copyText(message);
    this.snackbar = true;
  }

  private mounted() {
    this.getClientIdDetails(this.projectId);
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.active-bg {
  background-color: $BCgovActiveBg;
}
.pad-50 {
  padding-right: 50px;
}
</style>

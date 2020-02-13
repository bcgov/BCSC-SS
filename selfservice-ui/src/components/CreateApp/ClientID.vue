/** * ClientID component */

<template>
  <v-card class="mx-auto" style="max-width: 80%;">
    <v-toolbar flat class="bc-subtitle" dark>
      <v-btn
        icon
        @click="$router.push(`/project/${projectId}/summary/`)"
        :aria-label="$t('ClientID.Back')"
      >
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <v-toolbar-title>{{ $t('ClientID.pagetitle') }}</v-toolbar-title>
      <div class="flex-grow-1"></div>
      <v-col class="col-lg-4 col-md-5 col-8">
        <v-alert type="error" v-if="errorStatus" class="alert-top"
          >Something went wrong...</v-alert
        >
      </v-col>
      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-divider></v-divider>
    <v-item-group>
      <v-container>
        <v-row class="ma-5">
          <v-snackbar v-model="snackbar" :timeout="timeout">
            {{ text }}
            <v-btn color="blue" text @click="snackbar = false">
              {{ $t('ClientID.labelSnackbarClose') }}</v-btn
            >
          </v-snackbar>

          <v-col cols="12" md="12">
            <v-card flat>
              <v-list-item-content class="headline">{{
                $t('ClientID.titleApiKey')
              }}</v-list-item-content>
              <v-list-item-content
                v-html="$t('ClientID.titleApiKeyInfo')"
              ></v-list-item-content>
            </v-card>
            <v-item class="client-id" :value="getApiData.clientId">
              <v-card
                class="d-flex align-center px-5 client-id v-card--link"
                @click="docopy(getApiData.clientId)"
              >
                <v-list-item two-line>
                  <v-list-item-action>
                    <v-list-item-title class="title mb-1">
                      {{ getApiData.clientId }}
                    </v-list-item-title>
                  </v-list-item-action>
                </v-list-item>
                <v-spacer></v-spacer>

                <div class="display-3 flex-grow-1 text-center mr-5">
                  <v-icon color="#eae9e9" large>mdi-content-copy</v-icon>
                </div>
              </v-card>
            </v-item>
          </v-col>

          <v-col cols="12" md="12">
            <v-card flat>
              <v-list-item-content class="headline">{{
                $t('ClientID.titleClientSecret')
              }}</v-list-item-content>
              <v-list-item-content
                v-html="$t('ClientID.titleClientSecretInfo')"
              ></v-list-item-content>
            </v-card>
            <v-item class="client-id" :value="getApiData.clientSecret">
              <v-card
                class="d-flex align-center px-4 client-id v-card--link"
                @click="docopy(getApiData.clientSecret)"
              >
                <v-list-item two-line>
                  <v-list-item-content>
                    <v-list-item-title class="title mb-1">
                      {{ getApiData.clientSecret }}
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-spacer></v-spacer>

                <div class="display-3 flex-grow-1 text-center mr-5">
                  <v-icon color="#eae9e9" large>mdi-content-copy</v-icon>
                </div>
              </v-card>
            </v-item>
          </v-col>
          <v-col cols="12" md="12">
            <v-card flat>
              <v-list-item-content class="headline">{{
                $t('ClientID.titleTestAccount')
              }}</v-list-item-content>
              <v-list-item-content
                v-html="$t('ClientID.titleTestAccountInfo')"
              ></v-list-item-content>
            </v-card>
            <v-item class="client-id" :value="getApiData.clientSecret">
              <v-card class="d-flex align-center pa-4 client-id v-card--link">
                <v-list-item two-line>
                  <v-list-item-content>
                    <v-list-item-title
                      class="subtitle-1	 mb-1"
                      v-for="account in getApiData.testUserAccounts"
                    >
                      {{ account.userName }} , {{ account.idKey }}
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-spacer></v-spacer>
              </v-card>
            </v-item>
          </v-col>
        </v-row>
      </v-container>
    </v-item-group>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
const ClientIdModule = namespace('ClientIdModule');

@Component
export default class ClientIDDetails extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  @ClientIdModule.Getter('errorStatus') public errorStatus!: boolean;
  @ClientIdModule.Action('getClientIdDetails')
  public getClientIdDetails!: any;
  @ClientIdModule.Getter('getApiData') public getApiData!: [];

  private isLoading: boolean = false;
  private projectId: number = this.id || 0;
  private snackbar: boolean = false;
  private text: string = 'Copied';
  private timeout: number = 2000;

  public docopy(message: any) {
    this.$copyText(message);
    this.snackbar = true;
  }

  private mounted() {
    this.getClientIdDetails();
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.active-bg {
  background-color: $BCgovActiveBg;
}
</style>

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
          class="align-end pointer font-weight-bold"
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
                  <th class="text-left">Card Number</th>
                  <th class="text-left">Passcode</th>
                  <th class="text-left">Given Name</th>
                  <th class="text-left">Surname</th>
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
          <!-- <span class="pl-5">cardNumber ,passcode</span>
          <div v-for="(account, idx) in getApiData.testAccount" :key="account">
            <v-icon small class="mr-1" v-if="idx === 0">mdi-account</v-icon>
            <span :class="idx ===0 ? '' :'pl-5'">{{ account.cardNumber }} , {{ account.passcode }}</span>
          </div>-->
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <!-- <v-toolbar flat color="#38598a" dark>
      <v-card-title>{{ $t('ClientID.pagetitle') }}</v-card-title>
      <div class="flex-grow-1"></div>
      <v-col class="col-lg-4 col-md-5 col-8">
        <v-alert type="error" v-if="errorStatus" class="alert-top">Something went wrong...</v-alert>
      </v-col>
      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-divider></v-divider>-->

    <!-- <v-item-group>
      <v-container>
        <Loading v-if="isLoading && getApiData === 0" />
        <v-row class="ma-5" v-else>
          <v-snackbar v-model="snackbar" :timeout="timeout">
            {{ text }}
            <v-btn
              color="blue"
              text
              @click="snackbar = false"
            >{{ $t('ClientID.labelSnackbarClose') }}</v-btn>
          </v-snackbar>

          <v-col cols="12" md="12">
            <v-card flat>
              <v-list-item-content class="headline">
                {{
                $t('ClientID.titleApiKey')
                }}
              </v-list-item-content>
              <v-list-item-content v-html="$t('ClientID.titleApiKeyInfo')"></v-list-item-content>
            </v-card>
            <v-item
              class="client-id"
              :value="getApiData.oidcConfig && getApiData.oidcConfig.clientId"
            >
              <v-card
                class="d-flex align-center px-5 client-id-copy v-card--link"
                @click="
                  docopy(
                    getApiData.oidcConfig && getApiData.oidcConfig.clientId
                  )
                "
              >
                <v-list-item two-line>
                  <v-list-item-action>
                    <v-list-item-title class="title mb-1">
                      {{
                      getApiData.oidcConfig && getApiData.oidcConfig.clientId
                      }}
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
              <v-list-item-content class="headline">
                {{
                $t('ClientID.titleClientSecret')
                }}
              </v-list-item-content>
              <v-list-item-content v-html="$t('ClientID.titleClientSecretInfo')"></v-list-item-content>
            </v-card>
            <v-item
              class="client-id"
              :value="
                getApiData.oidcConfig && getApiData.oidcConfig.clientSecret
              "
            >
              <v-card
                class="d-flex align-center px-4 client-id v-card--link"
                @click="
                  docopy(
                    getApiData.oidcConfig && getApiData.oidcConfig.clientSecret
                  )
                "
              >
                <v-list-item two-line>
                  <v-list-item-content>
                    <v-list-item-content class="title mb-1">
                      {{
                      getApiData.oidcConfig &&
                      getApiData.oidcConfig.clientSecret
                      }}
                    </v-list-item-content>
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
              <v-list-item-content class="headline">
                {{
                $t('ClientID.titleTestAccount')
                }}
              </v-list-item-content>
              <v-list-item-content v-html="$t('ClientID.titleTestAccountInfo')"></v-list-item-content>
            </v-card>
            <v-item class="client-id">
              <v-card class="d-flex align-center pa-4 client-id v-card--link">
                <v-list-item two-line>
                  <v-list-item-content v-if="getApiData && getApiData.testAccount">
                    <v-list-item-title
                      class="subtitle-1 mb-1"
                      v-for="account in getApiData.testAccount"
                    >{{ account.cardNumber }} , {{ account.passcode }}</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-spacer></v-spacer>
              </v-card>
            </v-item>
          </v-col>
        </v-row>
      </v-container>
    </v-item-group>-->
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

/** * ClientID component */

<template>
  <v-card class="mx-auto" style="max-width: 80%;">
    <v-toolbar flat class="bc-subtitle" dark>
      <v-btn
        icon
        @click="$router.push(`/project/${projectId}/summary/`)"
        aria-label="Back Button"
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
    <v-item-group mandatory :value="slectedPackage">
      <v-container>
        <v-row class="ma-5">
          <v-snackbar v-model="snackbar" :timeout="timeout">
            {{ text }}
            <v-btn color="blue" text @click="snackbar = false">Close</v-btn>
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
              <!-- v-slot:default="{ active }" -->
              <!-- :value="packageData.id" -->
              <v-card class="d-flex align-center pa-4 client-id v-card--link">
                <v-list-item three-line>
                  <v-list-item-content>
                    <v-list-item-title
                      class="title mb-1"
                      @click="docopy(getApiData.clientId)"
                    >
                      {{ getApiData.clientId }}
                    </v-list-item-title>
                    <!-- <v-list-item-subtitle>
                      {{ packageData.description }}
                    </v-list-item-subtitle> -->
                    <!-- <v-list-item-subtitle
                      v-for="claimName in packageData.claimNames"
                      :key="claimName"
                    >
                      <v-icon color="#eae9e9" x-small>mdi-content-copy</v-icon>
                      {{ claimName }}
                    </v-list-item-subtitle> -->
                  </v-list-item-content>
                </v-list-item>
                <v-spacer></v-spacer>

                <div class="display-3 flex-grow-1 text-center mr-5">
                  <v-icon color="#eae9e9" x-large>mdi-content-copy</v-icon>
                </div>
                <!-- </v-scroll-y-transition> -->
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
              <!-- :value="packageData.id" -->
              <v-card class="d-flex align-center pa-4 client-id v-card--link">
                <v-list-item three-line>
                  <v-list-item-content>
                    <v-list-item-title
                      class="title mb-1"
                      @click="docopy(getApiData.clientSecret)"
                    >
                      {{ getApiData.clientSecret }}
                    </v-list-item-title>
                    <!-- <v-list-item-subtitle>
                      {{ packageData.description }}
                    </v-list-item-subtitle> -->
                    <!-- <v-list-item-subtitle
                      v-for="claimName in packageData.claimNames"
                      :key="claimName"
                    >
                      <v-icon color="#eae9e9" x-small>mdi-content-copy</v-icon>
                      {{ claimName }}
                    </v-list-item-subtitle> -->
                  </v-list-item-content>
                </v-list-item>
                <v-spacer></v-spacer>

                <div class="display-3 flex-grow-1 text-center mr-5">
                  <v-icon color="#eae9e9" x-large>mdi-content-copy</v-icon>
                </div>
                <!-- </v-scroll-y-transition> -->
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
              <!-- :value="packageData.id" -->
              <v-card class="d-flex align-center pa-4 client-id v-card--link">
                <v-list-item three-line>
                  <v-list-item-content>
                    <v-list-item-title
                      class="subtitle-1	 mb-1"
                      v-for="accounts in getApiData.testUserAccounts"
                    >
                      {{ accounts.userName }} , {{ accounts.idKey }}
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-spacer></v-spacer>

                <!-- <div class="display-3 flex-grow-1 text-center mr-5">
                  <v-icon color="#eae9e9" x-large>mdi-content-copy</v-icon>
                </div> -->
                <!-- </v-scroll-y-transition> -->
              </v-card>
            </v-item>
          </v-col>
        </v-row>
      </v-container>
    </v-item-group>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Watch, Prop } from 'vue-property-decorator';
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

  // @PackageAndTestModule.Action('addPackagetoProject')

  private slectedPackage: number = 1;
  private isLoading: boolean = false;
  private projectId: number = this.id || 0;
  private snackbar: boolean = false;
  private text: string = 'Copied';
  private timeout: number = 2000;

  private addPackagetoProject!: any;
  public docopy(message: any) {
    this.$copyText(message);
    this.snackbar = true;
    // alert('copied');
  }

  private mounted() {
    this.getClientIdDetails();
  }
  private selectedPackage(packageVal: number) {
    this.slectedPackage = packageVal;
  }
  private submitPackage() {
    // add package to project com ehere
    this.addPackagetoProject({
      slectedPackage: this.slectedPackage,
      projectId: this.projectId
    });
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.active-bg {
  background-color: $BCgovActiveBg;
}
</style>

/** * Add TechnicalReq */
<template>
  <v-card class="mx-auto outer-card">
    <!--  <v-alert type="success" v-if="successStatus">TechnicalReq {{isEditMode ? 'Updated' : 'Added'}} succesfully</v-alert>
    <v-alert type="error" v-if="errorStatus">Something went wrong...</v-alert>-->
    <v-card class="mx-auto">
      <v-app-bar dark class="bc-subtitle">
        <v-btn icon @click="goBack()" aria-label="Back Button">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
        <v-toolbar-title>
          {{
          $t('technicalRequirements.technicalTitle')
          }}
        </v-toolbar-title>
        <v-spacer></v-spacer>
      </v-app-bar>

      <v-form ref="form" v-model="form" class="pa-4 pt-6">
        <Loading v-if="isLoading" />
        <v-container v-else>
          <v-row dense>
            <v-col cols="12" md="12">
              <v-card class="pa-4 pt-6 mb-4">
                <v-card-title class="headline bc-padding-left-0 text-capitalize">
                  {{
                  getSingleProjectInfo && getSingleProjectInfo.projectName
                  }}
                </v-card-title>
                <v-card-subtitle class="text-left bc-padding-left-0">
                  {{
                  $t('technicalRequirements.technicalTitleInfo')
                  }}
                </v-card-subtitle>
              </v-card>
              <v-card class="pa-4 pt-6">
                <v-card-subtitle class="text-left bc-padding-left-0">
                  {{
                  $t('technicalRequirements.inputAppText')
                  }}
                </v-card-subtitle>
                <Input
                  v-model="clientUri"
                  :label="$t('technicalRequirements.labelApplicationUrl')"
                  type="text"
                  :rules="[rules.required, rules.url, rules.maxLength(500)]"
                />
                <!-- <div class="col-12"> -->
                <v-card-subtitle class="text-left bc-padding-left-0">
                  {{
                  $t('technicalRequirements.inputUrlText')
                  }}
                </v-card-subtitle>
                <!-- </div> -->
                <!-- <div
                  v-for="(redirectUri, index) in redirectUris"
                  v-bind:key="index"
                  class="row v-form px-4"
                >-->

                <v-text-field
                  v-model="redirectUris[0]"
                  :label="$t('technicalRequirements.labelRedirectUrl')"
                  type="text"
                  :rules="[rules.required, rules.url]"
                  class="addUri"
                  outlined
                ></v-text-field>
                <!-- :rules="[rules.required]" -->
                <!-- </div> -->
                <v-card-subtitle class="text-left bc-padding-left-0">
                  {{
                  $t('technicalRequirements.labelTestMethod')
                  }}
                </v-card-subtitle>
                <v-card-subtitle class="text-left bc-padding-left-0">
                  {{
                  $t('technicalRequirements.labelTestMethodHint')
                  }}
                </v-card-subtitle>

                <v-card-subtitle class="text-left bc-padding-left-0">
                  <v-radio-group v-model="signingEncryptionType" :mandatory="false">
                    <div class="small-hint">{{$t('technicalRequirements.SimpleJSONHint')}}</div>
                    <v-radio label="Simple JSON" :value="algorithamBase.SimpleJSON"></v-radio>
                    <div class="small-hint">{{$t('technicalRequirements.SignedJWTHint')}}</div>
                    <v-radio label="Signed JWT" :value="algorithamBase.SignedJWT">></v-radio>
                    <div
                      class="row pad-radio"
                      v-if="signingEncryptionType === algorithamBase.SignedJWT"
                    >
                      <div class="col-12 col-md-5">
                        <v-card-subtitle class="text-left bc-padding-left-0 pad-0">
                          {{
                          $t('technicalRequirements.labelSignedResponseAlgHint')
                          }}
                        </v-card-subtitle>
                      </div>
                      <div class="col-12 col-md-5">
                        <Select
                          v-model="signedResponseAlg"
                          :label="
                        $t(
                          'technicalRequirements.labelSignedResponseAlg'
                        )
                      "
                          :items="algorithm"
                          :rules="[rules.required]"
                          outlined
                        />
                      </div>
                    </div>
                    <div class="small-hint">{{$t('technicalRequirements.SecureJWTHint')}}</div>
                    <v-radio label="Secure JWT" :value="algorithamBase.SecureJWT">></v-radio>
                  </v-radio-group>
                </v-card-subtitle>
                <div v-if="signingEncryptionType === algorithamBase.SecureJWT" class="pad-radio">
                  <v-card-subtitle class="text-left bc-padding-left-0">
                    {{
                    $t('technicalRequirements.JWKSText')
                    }}
                  </v-card-subtitle>
                  <Input
                    v-model="jwksUri"
                    :label="$t('technicalRequirements.labelJWKSUrl')"
                    type="text"
                    :rules="[rules.required, rules.url, rules.maxLength(500)]"
                    class="pt-6"
                  />
                  <div class="row">
                    <div class="col-12 col-md-5">
                      <v-card-subtitle class="text-left bc-padding-left-0">
                        {{
                        $t('technicalRequirements.labelEncryptedResponseAlgHint')
                        }}
                      </v-card-subtitle>
                    </div>
                    <v-spacer />
                    <div class="col-12 col-md-5">
                      <v-card-subtitle class="text-left bc-padding-left-0">
                        {{
                        $t('technicalRequirements.labelSignedResponseAlgHint')
                        }}
                      </v-card-subtitle>
                    </div>
                    <div class="col-12 col-md-5">
                      <Select
                        v-model="encryptedResponseAlg"
                        :label="
                        $t(
                          'technicalRequirements.labelEncryptedResponseAlg'
                        )
                      "
                        :items="algorithm"
                        :rules="[rules.required]"
                        outlined
                      />
                    </div>
                    <v-spacer />
                    <div class="col-12 col-md-5">
                      <Select
                        v-model="signedResponseAlg"
                        :label="
                        $t(
                          'technicalRequirements.labelSignedResponseAlg'
                        )
                      "
                        :items="algorithm"
                        :rules="[rules.required]"
                        outlined
                        class="col-6"
                      />
                    </div>
                  </div>
                </div>
                <!-- </v-form> -->
                <v-divider></v-divider>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <Button @click="goBack()" aria-label="Back Button" secondary>
                    {{
                    $t(
                    showWizardExperience()
                    ? 'technicalRequirements.btnBack'
                    : 'technicalRequirements.btnCancel'
                    )
                    }}
                  </Button>
                  <Button
                    :disabled="!form"
                    :loading="isLoading"
                    class="white--text submit-req ml-6"
                    depressed
                    @click="addTechnicalReq()"
                  >
                    {{
                    $t(
                    showWizardExperience()
                    ? 'technicalRequirements.btnNext'
                    : 'technicalRequirements.btnSaveChanges'
                    )
                    }}
                  </Button>
                </v-card-actions>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </v-card>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Watch, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import Input from '@/Atomic/Input/Input.vue';
import Button from '@/Atomic/Button/Button.vue';
import Select from '@/Atomic/Select/Select.vue';
import validationRules from '@/config/validationRules';
import Loading from '@/Atomic/Loading/Loading.vue';
import { algorithamBase } from '@/constants/enums';

import { algorithm } from '@/constants/algorithm';
import { TechnicalReqModel } from '@/models/TechnicalReqModel';
const TechnicalReqModule = namespace('TechnicalReqModule');
const ProjectInfoModule = namespace('ProjectInfoModule');
const SharedModule = namespace('SharedModule');

@Component({
  components: { Input, Button, Select, Loading }
})
export default class AddTechnicalReq extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  @Prop({ default: '' })
  public action!: string;

  @TechnicalReqModule.Getter('successStatus') public successStatus!: boolean;
  @TechnicalReqModule.Getter('errorStatus') public errorStatus!: boolean;
  @TechnicalReqModule.Action('addTechnicalReq')
  public addTechnicalReqStore!: any;
  @TechnicalReqModule.Getter('getTechnicalReq')
  public getTechnicalReq!: any;
  @TechnicalReqModule.Action('updateTechnicalReq')
  public updateTechnicalReqStore!: any;
  @TechnicalReqModule.Action('loadTechnicalReqDetails')
  public loadTechnicalReqDetails!: any;
  @TechnicalReqModule.Getter('isLoading') public isLoading!: boolean;

  @ProjectInfoModule.Getter('getSingleProjectInfo')
  public getSingleProjectInfo!: any;
  @ProjectInfoModule.Action('loadSingleProjectInfo')
  public loadSingleProjectInfo!: any;
  @SharedModule.Action('redirectFromSummaryPage')
  public redirectFromSummaryPage!: any;
  @SharedModule.Getter('isRedirectFromSummaryPage')
  public isRedirectFromSummaryPage!: boolean;

  public form: boolean = false;
  private projectId: number = this.id || 0;
  private TechnicalReqId: number = 0;
  private clientUri: string = '';
  private redirectUris: any = [''];
  private jwksUri: string = '';
  private encryptedResponseAlg: string = 'RS256';
  private signedResponseAlg: string = 'RS256';
  private algorithm: any = algorithm;
  private blockRemoval = true;
  private signingEncryptionType: number = algorithamBase.SimpleJSON;
  private algorithamBase: any = algorithamBase;

  // private id: string = '';
  private isEditMode: boolean = false;
  /* istanbul ignore next */
  private rules = validationRules;

  @Watch('getTechnicalReq')
  private ongetTechnicalReqChanged(val: any) {
    this.updteEdit(val);
  }

  @Watch('getSingleProjectInfo')
  private ongetSingleProjectInfoChanged(val: any) {
    this.projectId = this.getSingleProjectInfo.id;
  }

  private addTechnicalReq() {
    const data: TechnicalReqModel = {
      projectId: this.projectId,
      clientUri: this.clientUri,
      redirectUris: this.redirectUris,
      signingEncryptionType: this.signingEncryptionType,
      jwksUri:
        this.signingEncryptionType === algorithamBase.SecureJWT
          ? this.jwksUri
          : '',
      encryptedResponseAlg:
        this.signingEncryptionType === algorithamBase.SecureJWT
          ? this.encryptedResponseAlg
          : null,
      signedResponseAlg:
        this.signingEncryptionType === algorithamBase.SimpleJSON
          ? null
          : this.signedResponseAlg
    };

    if (this.isEditMode && this.TechnicalReqId !== 0) {
      data.id = this.TechnicalReqId;
      this.updateTechnicalReqStore(data);
    } else {
      this.addTechnicalReqStore(data);
    }
  }

  private updteEdit(val: any) {
    this.projectId = val.projectId || this.projectId;
    this.clientUri = val.clientUri;
    this.redirectUris = val.redirectUris || this.redirectUris;
    this.jwksUri = val.jwksUri;
    this.encryptedResponseAlg =
      val.encryptedResponseAlg || this.encryptedResponseAlg;
    this.signedResponseAlg = val.signedResponseAlg || this.signedResponseAlg;
    this.TechnicalReqId = val.id || 0;
    this.isEditMode = true;
    this.signingEncryptionType =
      val.signingEncryptionType || this.signingEncryptionType;
  }

  private mounted() {
    this.isEditMode = false;

    if (this.id !== 0) {
      this.isEditMode = true;
      this.loadTechnicalReqDetails(this.id);
    }
    if (this.getSingleProjectInfo && this.getSingleProjectInfo.id) {
      this.projectId = this.getSingleProjectInfo.id;
    } else {
      this.loadSingleProjectInfo(this.id);
    }
  }
  private goBack() {
    const redirectPage = this.showWizardExperience() ? 'info' : 'summary';
    this.redirectFromSummaryPage(false);
    this.$router.push(`/project/${this.projectId}/${redirectPage}/`);
  }
  private showWizardExperience() {
    if (this.isEditMode && this.isRedirectFromSummaryPage) {
      return false;
    }
    return true;
  }

  // commented out now only one redirect URL
  // private addUri() {
  //   const checkEmptyLines = this.redirectUris.filter((uri: any) => uri === '');
  //   if (checkEmptyLines.length >= 1 && this.redirectUris.length > 0) {
  //     return;
  //   }
  //   this.redirectUris.push('');
  // }
  // private clearUri(uriId: number) {
  //   this.blockRemoval = this.redirectUris.length <= 1;
  //   if (!this.blockRemoval) {
  //     this.redirectUris.splice(uriId, 1);
  //   }
  // }
}
</script>
<style lang="scss" scoped>
.pad-radio {
  padding-left: 33px;
}
.pad-0 {
  padding: 0;
}
</style>

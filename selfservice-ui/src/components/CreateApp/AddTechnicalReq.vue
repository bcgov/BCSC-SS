/** * Add TechnicalReq */
<template>
  <v-card class="mx-auto" style="max-width: 80%;">
    <!--  <v-alert type="success" v-if="successStatus">TechnicalReq {{isEditmode ? 'Updated' : 'Added'}} succesfully</v-alert>
    <v-alert type="error" v-if="errorStatus">Something went wrong...</v-alert>-->
    <v-card class="mx-auto">
      <v-app-bar dark class="bc-subtitle">
        <v-btn icon @click="$router.push(`/project/${projectId}/info/`)" aria-label="Back Button">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
        <v-toolbar-title>{{$t('technicalRequirements.technicalTitle')}}</v-toolbar-title>
        <v-spacer></v-spacer>
      </v-app-bar>

      <v-form ref="form" v-model="form" class="pa-4 pt-6">
        <v-container>
          <v-row dense>
            <v-col cols="12" md="12">
              <v-card class="pa-4 pt-6">
                <!-- <v-card-title class="headline"
                  >Technical information</v-card-title
                >-->
                <!-- <v-card-subtitle class="text-left"
                  >Tell us about your Project</v-card-subtitle
                >-->
                <v-card-title
                  class="headline padding-0 text-capitalize"
                >{{$t('technicalRequirements.projectName')}}{{ getSingleProjectInfo && getSingleProjectInfo.projectName }}</v-card-title>

                <Input
                  v-model="clientUri"
                  counter="500"
                  :label="$t('technicalRequirements.labelApplicationUrl')"
                  type="text"
                  :rules="[rules.required, rules.url, rules.maxLength(500)]"
                />
                <!-- <div class="col-12"> -->
                <v-card-subtitle
                  class="text-left padding-0"
                >{{$t('technicalRequirements.inputUrlText')}}</v-card-subtitle>
                <!-- </div> -->
                <div
                  v-for="(redirectUri, index) in redirectUris"
                  v-bind:key="index"
                  class="row v-form px-4"
                >
                  <v-text-field
                    v-model="redirectUris[index]"
                    :label="$t('technicalRequirements.labelRedirectUrl')"
                    type="text"
                    filled
                    @blur="addUri"
                    append-icon="mdi-minus"
                    @click:append="clearUri(index)"
                    @click:prepend="addUri"
                    :rules="[rules.url]"
                    class="addUri"
                    outlined
                  ></v-text-field>
                  <!-- :rules="[rules.required]" -->
                </div>
                <v-card-subtitle
                  class="text-left padding-0"
                >{{$t('technicalRequirements.JWKSText')}}</v-card-subtitle>
                <Input
                  v-model="jwksUri"
                  counter="500"
                  :label="$t('technicalRequirements.labelJWKSUrl')"
                  type="text"
                  :rules="[rules.required, rules.url, rules.maxLength(500)]"
                  class="pt-6"
                />
                <div class="row">
                  <div class="col-5">
                    <Select
                      v-model="idTokenSignedResponseAlg"
                      :label="$t('technicalRequirements.labelIdTokenSignedResponseAlg')"
                      :items="tokenAlgoritham"
                      :rules="[rules.required]"
                      outlined
                    />
                  </div>
                  <v-spacer />
                  <div class="col-5">
                    <Select
                      v-model="userinfoSignedResponseAlg"
                      :label="$t('technicalRequirements.labelUserinfoSignedResponseAlg')"
                      :items="userAlgoritham"
                      :rules="[rules.required]"
                      outlined
                      class="col-6"
                    />
                  </div>
                </div>
                <!-- </v-form> -->
                <v-divider></v-divider>
                <v-card-actions>
                  <!-- <v-btn text @click="$refs.form.reset()">Clear</v-btn> -->
                  <v-spacer></v-spacer>
                  <Button
                    @click="$router.push(`/project/${projectId}/info/`)"
                    aria-label="Back Button"
                    secondary
                  >{{$t('technicalRequirements.btnBack')}}</Button>
                  <Button
                    :disabled="!form"
                    :loading="isLoading"
                    class="white--text submit-req ml-6"
                    depressed
                    @click="addTechnicalReq"
                  >Next{{$t('technicalRequirements.next')}}</Button>
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

import {
  tokenSignatureAlgoritham,
  userInfoSignedResponseAlgoritham
} from '@/constants/algoritham';
import { TechnicalReqModel } from '@/models/TechnicalReqModel';
const TechnicalReqModule = namespace('TechnicalReqModule');
const ProjectInfoModule = namespace('ProjectInfoModule');

@Component({
  components: { Input, Button, Select }
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

  @ProjectInfoModule.Getter('getSingleProjectInfo')
  public getSingleProjectInfo!: any;
  @ProjectInfoModule.Action('loadSingleProjectInfo')
  public loadSingleProjectInfo!: any;

  public form: boolean = false;
  private isLoading: boolean = false;
  private projectId: number = this.id || 0;
  private clientUri: string = '';
  private redirectUris: any = [''];
  private jwksUri: string = '';
  private idTokenSignedResponseAlg: string = 'RS256';
  private userinfoSignedResponseAlg: string = 'RS256';
  private tokenAlgoritham: any = tokenSignatureAlgoritham;
  private userAlgoritham: any = userInfoSignedResponseAlgoritham;
  private blockRemoval = true;

  // private id: string = '';
  private isEditmode: boolean = false;
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
      jwksUri: this.jwksUri,
      idTokenSignedResponseAlg: this.idTokenSignedResponseAlg,
      userinfoSignedResponseAlg: this.userinfoSignedResponseAlg
    };

    if (this.isEditmode) {
      data.id = this.id;
      this.updateTechnicalReqStore(data);
    } else {
      this.addTechnicalReqStore(data);
    }
    // (this.$refs.form as HTMLFormElement).reset();
    // this.$router.push('/technicalreq/');
  }

  private updteEdit(val: any) {
    this.projectId = val.projectId;
    this.clientUri = val.clientUri;
    this.redirectUris = val.redirectUris;
    this.jwksUri = val.jwksUri;
    this.idTokenSignedResponseAlg = val.idTokenSignedResponseAlg;
    this.userinfoSignedResponseAlg = val.userinfoSignedResponseAlg;
    this.id = val.id;
    this.isEditmode = true;
  }

  private mounted() {
    this.isEditmode = false;
    if (this.action && this.action === 'edit' && this.id !== 0) {
      this.isEditmode = true;
      this.loadTechnicalReqDetails(this.id);
    }

    if (this.getSingleProjectInfo && this.getSingleProjectInfo.id) {
      this.projectId = this.getSingleProjectInfo.id;
    } else {
      this.loadSingleProjectInfo(this.id);
    }
  }
  private addUri() {
    const checkEmptyLines = this.redirectUris.filter((uri: any) => uri === '');
    if (checkEmptyLines.length >= 1 && this.redirectUris.length > 0) {
      return;
    }
    this.redirectUris.push('');
  }
  private clearUri(uriId: number) {
    this.blockRemoval = this.redirectUris.length <= 1;
    if (!this.blockRemoval) {
      this.redirectUris.splice(uriId, 1);
    }
  }
}
</script>
<style lang="scss" scoped>
.padding-0 {
  padding-left: 0px !important;
}
</style>

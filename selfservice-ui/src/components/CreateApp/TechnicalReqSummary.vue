/** * TechnicalReqSummary component */

<template>
  <v-card
    class="mt-5"
    :class="
      showCannotSubmitError && !isTechnicalInfoAvailable ? 'red-border' : ''
    "
  >
    <v-toolbar dense class="bc-subtitle-2" dark>
      <v-card-title>
        {{ $t('summaryPage.technicalReqTitle') }}
        <span
          @click="$router.push(`/project/${id}/technical`)"
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
      <v-list-item>
        <v-list-item-content class="pr-30">
          {{ $t('summaryPage.labelApplicationUrl') }}
          <span
            class="small-hint pad-50"
            v-html="$t('summaryPage.applicationUrlHint')"
          ></span>
        </v-list-item-content>
        <v-list-item-content class="align-end">
          <div v-if="technicalReq.clientUri">
            <v-icon small class="mr-1">mdi-link</v-icon>
            {{ technicalReq.clientUri }}
          </div>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <v-list-item>
        <v-list-item-content class="align-self-start pr-30">
          {{ $t('summaryPage.labelRedirectUrl') }}
          <span
            class="small-hint pad-50"
            v-html="$t('summaryPage.labelRedirectUrlHint')"
          ></span>
        </v-list-item-content>
        <v-list-item-content class="align-end">
          <div v-for="redirectUri in technicalReq.redirectUris" :key="redirectUri">
            <v-icon small class="mr-1" v-if="redirectUri !== ''">mdi-link</v-icon>
            {{ redirectUri }}
          </div>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <v-list-item>
        <v-list-item-content class="pr-30">
          {{ $t('summaryPage.labelTestingMethod') }}
          <span
            class="small-hint pad-50"
            v-html="$t('summaryPage.labelTestingMethodHint')"
          ></span>
        </v-list-item-content>

        <v-list-item-content class="align-end">
          <div v-if="technicalReq.signingEncryptionType">
            <v-icon small class="mr-1">mdi-format-list-checks</v-icon>
            {{
            $t(`summaryPage.${algorithm[technicalReq.signingEncryptionType]}`)
            }}
          </div>
        </v-list-item-content>
      </v-list-item>
      <v-divider v-if="technicalReq.signingEncryptionType == algorithm.SecureJWT"></v-divider>
      <v-list-item v-if="technicalReq.signingEncryptionType == algorithm.SecureJWT">
        <v-list-item-content class="pr-30">
          {{ $t('summaryPage.labelJWKSUrl') }}
          <span
            class="small-hint pad-50"
            v-html="$t('summaryPage.labelJWKSUrlHint')"
          ></span>
        </v-list-item-content>

        <v-list-item-content class="align-end">
          <div v-if="technicalReq.jwksUri">
            <v-icon small class="mr-1">mdi-link</v-icon>
            {{ technicalReq.jwksUri }}
          </div>
        </v-list-item-content>
      </v-list-item>
      <v-divider v-if="technicalReq.signingEncryptionType == algorithm.SecureJWT"></v-divider>
      <v-list-item v-if="technicalReq.signingEncryptionType == algorithm.SecureJWT">
        <v-list-item-content class="pr-30">
          {{ $t('summaryPage.labelEncryptedResponseEnc') }}
          <span
            class="small-hint pad-50"
            v-html="$t('summaryPage.labelEncryptedResponseEncHint')"
          ></span>
        </v-list-item-content>
        <v-list-item-content class="align-end">
          <v-list-item-content class="align-end">
            <div v-if="technicalReq.encryptedResponseEnc">
              <v-icon small class="mr-1">mdi-shield-key</v-icon>
              {{ technicalReq.encryptedResponseEnc }}
            </div>
          </v-list-item-content>
        </v-list-item-content>
      </v-list-item>
      <v-divider v-if="technicalReq.signingEncryptionType == algorithm.SecureJWT"></v-divider>
      <v-list-item v-if="technicalReq.signingEncryptionType == algorithm.SecureJWT">
        <v-list-item-content class="pr-30">
          {{ $t('summaryPage.labelEncryptedResponseAlg') }}
          <span
            class="small-hint pad-50"
            v-html="$t('summaryPage.labelEncryptedResponseAlgHint')"
          ></span>
        </v-list-item-content>
        <v-list-item-content class="align-end">
          <v-list-item-content class="align-end">
            <div v-if="technicalReq.encryptedResponseAlg">
              <v-icon small class="mr-1">mdi-shield-key</v-icon>
              {{ technicalReq.encryptedResponseAlg }}
            </div>
          </v-list-item-content>
        </v-list-item-content>
      </v-list-item>
      <v-divider v-if="technicalReq.signingEncryptionType"></v-divider>
      <v-list-item v-if="technicalReq.signingEncryptionType">
        <v-list-item-content class="pr-30">
          {{ $t('summaryPage.labelSignedResponseAlg') }}
          <span
            class="small-hint pad-50"
            v-html="$t('summaryPage.labelSignedResponseAlgHint')"
          ></span>
        </v-list-item-content>
        <v-list-item-content class="align-end">
          <v-list-item-content class="align-end">
            <div v-if="technicalReq.signedResponseAlg">
              <v-icon small class="mr-1">mdi-shield-key</v-icon>
              {{ technicalReq.signedResponseAlg }}
            </div>
          </v-list-item-content>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import { algorithmBase } from '@/constants/enums';

@Component
export default class TechnicalReqSummary extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  @Prop({ default: {} })
  public technicalReq!: any;

  @Prop({ default: false })
  public showCannotSubmitError!: boolean;
  @Prop({ default: false })
  public isTechnicalInfoAvailable!: boolean;

  private algorithm: any = algorithmBase;
}
</script>

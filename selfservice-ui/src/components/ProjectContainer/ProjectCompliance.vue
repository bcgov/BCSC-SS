/** * ProjectCompliance of app */

<template>
  <v-container>
    <v-row class="ma-5">
      <v-col cols="12">
        <v-card flat>
          <h2 class="text-left tab-headline page-title-h2">
            {{ $t('projectCompliance.pageTitle') }}
          </h2>
          <p class="text-left pt-5">
            After successful experimentation, if your BPS team wants to pursue
            an integration with real citizen BC Services Cards, a BPS team
            member <strong>triggers</strong> a promotion of the project’s
            <em>Development Access Request</em> into a
            <em>Production Access Request</em>.
          </p>
          <p class="text-left">
            The Provincial IDIM Program is mandated to provide identity and
            authentication services using the BC Services Card to support
            citizen transactions with government services.
          </p>
          <p class="text-left">
            Before any Production Access occurs, Open ID Connect (OIDC)
            technical details are provided by the BPS team and a series of
            checks and balances are needed to provide the IDIM Program with the
            confidence required to support the BPS organization’s use of the BC
            Services Card integration.
          </p>
          <p class="text-left">
            We anticipate the method of compliance is through an approval and
            attestation model as follows:
          </p>
          <ol class="text-left">
            <li>
              The BPS Manager declared in the project approves the checklist
              items in a specific compliance section.
            </li>
            <li>
              Subsequently the BPS Executive Sponsor attests to each of the
              checklist items in the compliance section.
            </li>
          </ol>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component({})
export default class ProjectCompliance extends Vue {}
</script>

<style lang="scss" scoped></style>

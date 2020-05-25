/** * Footer of app */
<template>
  <v-footer height="auto">
    <v-layout justify-center row wrap class="side-left-margin">
      <v-flex dark text-xs-center white--text xs12>
        <v-row justify="left" no-gutters>
          <a href="/" class="footer-link">{{$t('footer.linkHome')}}</a>
          <a
            href="https://www2.gov.bc.ca/gov/content/home/disclaimer"
            class="footer-link"
            target="_ss"
          >{{$t('footer.linkDisclaimer')}}</a>
          <a
            href="https://www2.gov.bc.ca/gov/content/home/privacy"
            class="footer-link"
            target="_ss"
          >{{$t('footer.linkPrivacy')}}</a>
          <a
            href="https://www2.gov.bc.ca/gov/content/home/accessibility"
            class="footer-link"
            target="_ss"
          >{{$t('footer.linkAccessibility')}}</a>
          <a
            href="https://www2.gov.bc.ca/gov/content/home/copyright"
            class="footer-link"
            target="_ss"
          >{{$t('footer.linkCopyright')}}</a>
          <a href="/contact-us" class="footer-link">{{$t('footer.linkContactus')}}</a>
        </v-row>
      </v-flex>
    </v-layout>
  </v-footer>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class Footer extends Vue {}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
footer {
  background-color: $BCgovBlue5 !important;
  border-top: 2px solid $BCgovGold5 !important;
  color: $BCgovWhite !important;
  padding: 4px 16px;
  z-index: 5;

  .footer-link {
    padding: 10px 16px;
    border-radius: unset;
    color: $BCgovWhite;
    text-decoration: none;
    font-size: 15px;
    @include sm {
      border-right: 1px solid $BCgovBlue3;
    }
  }
}
</style>

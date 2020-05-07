/** * Footer of app */

<template>
  <v-footer height="auto">
    <v-layout justify-center row wrap class="side-left-margin">
      <v-flex dark text-xs-center white--text xs12>
        <v-row justify="left" no-gutters>
          <a href="/" class="footer-link">Home</a>
          <a
            href="https://www2.gov.bc.ca/gov/content/home/disclaimer"
            class="footer-link"
            target="_ss"
          >Disclaimer</a>
          <a
            href="https://www2.gov.bc.ca/gov/content/home/privacy"
            class="footer-link"
            target="_ss"
          >Privacy</a>
          <a
            href="https://www2.gov.bc.ca/gov/content/home/accessibility"
            class="footer-link"
            target="_ss"
          >Accessibility</a>
          <a
            href="https://www2.gov.bc.ca/gov/content/home/copyright"
            class="footer-link"
            target="_ss"
          >Copyright</a>
          <a href="/contact-us" class="footer-link">Contact Us</a>
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

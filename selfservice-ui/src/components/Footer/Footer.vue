/** * Footer of app */

<template>
  <v-footer height="auto">
    <v-layout justify-center row wrap class="side-left-margin">
      <v-flex dark text-xs-center white--text xs12>
        <v-row justify="left" no-gutters>
          <v-btn color="white" text>
            Home
          </v-btn>
          <v-btn color="white" text>
            Disclaimer
          </v-btn>
          <v-btn color="white" text>
            Privacy
          </v-btn>
          <v-btn color="white" text>
            Accessibility
          </v-btn>
          <v-btn color="white" text>
            Copyright
          </v-btn>
          <v-btn color="white" text>
            Contact Us
          </v-btn>
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
  @include sm {
    // padding: 6px 65px 6px 65px;
  }

  .v-btn {
    border-radius: unset;
    color: $BCgovWhite !important;
    @include sm {
      border-right: 1px solid $BCgovBlue3;
    }
  }
}
</style>

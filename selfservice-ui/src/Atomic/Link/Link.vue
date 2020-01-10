/** * link atomic component * Primary buttons allow users to carry out an
important action on your service, such as Download or Submit. */

<template>
  <router-link :to="to" class="router-link-main"><slot></slot></router-link>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

/**
 *
 * @displayName  Link
 */

@Component
export default class Link extends Vue {
  /**
   * The Url for the link.
   *
   */
  @Prop({
    default: ''
  })
  private to!: string;
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.router-link-main {
  color: $BCgovWhite;
  text-decoration: none;
  font-size: 16px;
  font-weight: 500;
}
</style>

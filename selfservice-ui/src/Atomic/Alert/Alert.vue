/** * Alert atomic component. */

<template>
  <v-alert
    v-bind="$attrs"
    :type="type"
    :dense="dense"
    :outlined="outlined"
    class="text-left"
    :icon="icon"
  >
    <slot></slot>
  </v-alert>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

/**
 *
 * @displayName  Alert
 */

@Component
export default class Alert extends Vue {
  /**
   * The type for the alert.
   *
   */
  @Prop({
    default: 'error',
  })
  private type!: string;

  /**
   * dense
   */
  @Prop({
    default: false,
  })
  private dense!: boolean;

  /**
   * outlined
   */
  @Prop({
    default: true,
  })
  private outlined!: boolean;

  /**
   *  outlined
   */
  @Prop({
    default: true,
  })
  private icon!: boolean;
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
</style>

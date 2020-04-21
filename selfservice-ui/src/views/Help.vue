<template>
  <v-card class="mx-auto outer-card " flat>
    <div class="help-page text-left ">
      <Help :step="step" />
    </div>
  </v-card>
</template>
<script lang="ts">
// @ is an alias to /src
import { Component, Vue, Prop } from 'vue-property-decorator';
import Help from '@/html/Help.vue';

@Component({
  components: {
    Help,
  },
})
export default class HelpHome extends Vue {
  @Prop({ default: 'help' })
  public step!: string;
}
</script>
<style lang="scss">
@import './../assets/styles/theme.scss';
.help-page h1,
.help-page h2,
.help-page h3 {
  letter-spacing: -0.04rem;
  font-weight: 700;
  margin: 20px 0;
}
.help-page img {
  margin: 30px 0;
}
.help-page {
  margin-bottom: 30px;
}
.help-page .menu ul {
  background-color: $gray10;
  display: flex;
  padding: 15px;
  & li {
    list-style: none;
    margin-right: 12px;
    color: $BCgovFontColorInverted;
    & a {
      color: $BCgovFontColorInverted;
    }
  }
}
</style>

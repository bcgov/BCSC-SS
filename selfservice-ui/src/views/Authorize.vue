<template>
  <Loading />
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Loading from '@/Atomic/Loading/Loading.vue';

@Component({
  components: { Loading }
})
export default class Authorize extends Vue {}
</script>

<style lang="scss" scoped>
@import '@/assets/styles/theme.scss';
</style>

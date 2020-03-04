<template>
  <div class="home">
    <Profile />
  </div>
</template>

<script lang="ts">
// @ is an alias to /src
import { Component, Vue, Prop } from 'vue-property-decorator';
import Profile from '@/components/Profile/Profile.vue';

@Component({
  components: {
    Profile
  }
})
export default class ProfileHome extends Vue {}
</script>

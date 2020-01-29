/** * Header of app */

<template>
  <v-card class="mx-auto">
    <v-navigation-drawer app clipped fixed height="100%" permanent>
      <!-- v-model="drawer" -->
      <v-list dark>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="title">Self Service</v-list-item-title>
            <!-- <v-list-item-subtitle>
              subtext
            </v-list-item-subtitle>-->
          </v-list-item-content>
        </v-list-item>

        <v-divider></v-divider>

        <v-list dense nav>
          <v-list-item v-for="item in items" :key="item.title" link>
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title :to="item.title">
                <Link :to="item.link">{{ item.title }}</Link>
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import Link from '@/Atomic/Link/Link.vue';

const KeyCloakModule = namespace('KeyCloakModule');

@Component({
  components: {
    Link
  }
})
export default class Sidebar extends Vue {
  @Prop() private drawer!: boolean;
  private items: any = [
    { title: 'Dashboard', icon: 'mdi-view-dashboard', link: '/' },
    { title: 'Create Project', icon: 'mdi-plus-circle', link: '/project/info' },
    { title: 'About', icon: 'mdi-help-box', link: '/about' }
  ];
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';

.v-navigation-drawer {
  text-align: left;
  background-color: $BCgovBlue5 !important;
}
</style>

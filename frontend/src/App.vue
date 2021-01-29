<template>
  <div
    id="app"
    style="display: flex; flex-flow: column; height:100% width:100%"
  >
    <navbar v-if="isLogdedIn"></navbar>
    <b-container style="flex-grow: 1; padding: 5px">
      <router-view></router-view>
    </b-container>
  </div>
</template>
<script>
import Navbar from "./components/Navbar";

export default {
  components: { Navbar },
  name: "App",
  computed: {
    isLogdedIn() {
      return this.$route.name != "Login";
    },
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  color: #1e2731;
}
</style>

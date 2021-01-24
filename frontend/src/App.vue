<template>
  <div id="app" style="display: flex; flex-flow: column; height:100% width:100%">
    <Navbar v-if="isLogdedIn"></Navbar>
       <b-container style="flex-grow: 1; padding:0">
            <router-view></router-view>
        </b-container>
  </div>
</template>
<style scoped>

</style>
<script>
import Navbar from "./components/Navbar";

export default {
  components: { Navbar},
  name: "App",
  computed: {
    isLogdedIn() { 
    return this.$route.name != "Login";},
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  color: #2c3e50;
}
</style>

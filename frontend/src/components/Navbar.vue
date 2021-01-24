<template>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <Slide v-if="isLogdedIn">
        <a href="/Inicio">Inicio</a>
      <ul>
          Menu
    <br>
        {{this.storage.email }}
      </ul>
      <a href='/Inicio/Usuarios' v-if="IsAdmin">
        <span><b-icon icon='person'></b-icon> Usuarios</span>
      </a>
      <a href='/Inicio' v-if="isPaciente">
        <span><b-icon icon='person'></b-icon> Llenar Formularios</span>
      </a>
      <a href='/Inicio' v-if="isPaciente">
        <span><b-icon icon='person'></b-icon> Realizar Diario?</span>
      </a>
      <a href='/Inicio' v-if="isPaciente">
        <span><b-icon icon='person'></b-icon> Reportar Problemas</span>
      </a>
      <a href='/Inicio' v-if="isQuimicoSr">
        <span ><b-icon icon='person'></b-icon> Verificar Fidelidad en Pacientes</span>
      </a>
      <a href='/Inicio' v-if="isQuimicoSr">
        <span  ><b-icon icon='person'></b-icon> Visualizar Respuestas del Test1 en Pacientes</span>
      </a>
      <a href='/Inicio' v-if="isQuimicoSr">
        <span><b-icon icon='person'></b-icon> Ver Listado de Seguimientos de Pacientes</span>
      </a>
       <a href='/Inicio' v-if="isQuimicoSr">
        <span v-if="IsAdmin"><b-icon icon='person'></b-icon> Asignar SFT a Pacientes</span>
      </a>
      <a href='/Inicio' v-if="isQuimicoJr">
        <span v-if="IsAdmin"><b-icon icon='person'></b-icon>Entrevistas</span>
      </a>
      <hr>
      <hr>
      <a href='/Logout'>
        <span><b-icon icon='door-closed-fill'></b-icon> Cerrar Sesión</span>
      </a>
    </Slide>
    <b-navbar-brand style="position:absolute; right: 80%; top: 20px">{{
      this.$route.name
    }}</b-navbar-brand>

    <b-navbar-nav class="ml-auto">
      <div>
        <h4  v-if="isLogdedIn" id="h4_username" class="h4_username">
          {{ this.storage.username }}-{{ this.storage.type_user }}
        </h4>
        <img
          class="image_navbar"
          src="../assets/Logo_disprodelsa_con_letras.jpeg"
        >
        <a class="navbar-brand" href="#">
          <b-icon  v-if="isLogdedIn"
            icon="person-circle"
            title="Perfil"
            style="position: absolute; right: -10px; top: -5px"
            scale="3"
          ></b-icon>
        </a>
      </div>
    </b-navbar-nav>
  </b-navbar>
</template>
<style scoped>
@import "./css/navbar.css";
</style>
<script>
import { Slide } from "vue-burger-menu";

export default {
  components: { Slide },
  name: "NavBar",
  data() {
    return {};
  },
  computed: {
    isLogdedIn() {
      return this.storage.token != "";
    },
    IsAdmin() {
      return this.storage.type_user == "Administrador";
    },
    isPaciente() {
      return this.storage.type_user == "Paciente";
    },
    isQuimicoSr() {
      return this.storage.type_user == "QuimicoSr";
    },
    isQuimicoJr() {
      return this.storage.type_user == "QuimicoJr";
    },
   
  }
};
</script>
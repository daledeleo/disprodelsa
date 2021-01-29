<template>
  <b-navbar class='navbar navbar-light' style="background-color: #84A9CD;" toggleable="lg" position: sticky>
    <Slide v-if="isLogdedIn">
        <a href="/Inicio">Inicio</a>
      <ul>
          Menu
    <br>
        {{email }}
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
        <span ><b-icon icon='person-check'></b-icon> Verificar Fidelidad en Pacientes</span>
      </a>
      <a href='/Inicio' v-if="isQuimicoSr || isQuimicoJr">
        <span  ><b-icon icon='eye'></b-icon> Visualizar Respuestas del Test1 en Pacientes</span>
      </a>
      <a href='/Inicio' v-if="isQuimicoSr">
        <span><b-icon icon='layout-text-sidebar-reverse'></b-icon> Ver Listado de Seguimientos de Pacientes</span>
      </a>
       <a href='/Inicio' v-if="isQuimicoSr">
        <span ><b-icon icon='person'></b-icon> Asignar SFT a Pacientes</span>
      </a>
      <a href='/Inicio' v-if="isQuimicoJr">
        <span><b-icon icon='person'></b-icon> Entrevistas</span>
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
        <h4 v-if="isLogdedIn" id="h4_username" class="h4_username">
          {{ username }}-{{ type_user }}
        </h4>
        <img v-if="isLogdedIn" class="image_navbar_else" id="image" src="../assets/Logo_disprodelsa_con_letras.jpeg">
        <img v-else class="image_navbar" src="../assets/Logo_disprodelsa_con_letras.jpeg">
        <a class="navbar-brand" v-if="isLogdedIn" href="/Perfil">
          <b-icon  
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
  data(){
    return{
      isCrearCuenta:this.$route.name!='Crear Cuenta' || this.$$route.name!='Reestablecer contraseña',
      username:localStorage.getItem('username'),
      type_user:localStorage.getItem('type_user'),
      email:localStorage.getItem('email'),
    }
  },
  computed: {
    isLogdedIn() {
      return localStorage.length > 1 || localStorage.getItem('token') != undefined;
    },
    IsAdmin() {
      return localStorage.getItem('type_user') == "Administrador";
    },
    isPaciente() {
      return localStorage.getItem('type_user') == "Paciente";
    },
    isQuimicoSr() {
      return localStorage.getItem('type_user') == "Quimico Sr";
    },
    isQuimicoJr() {
      return localStorage.getItem('type_user') == "Quimico Jr";
    },
  },
 
};
</script>
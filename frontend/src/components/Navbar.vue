<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand to="/"> Disprodelsa</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-ccollapse id="nav-collapse" is-nav>
        <b-navbar-nav v-if="isLogdedIn">
          <b-nav-item>Menu</b-nav-item>
          <b-nav-item>email_user</b-nav-item>
          <b-nav-item to="/" v-if="isAdmin">Usuarios</b-nav-item>
          <b-nav-item to="/" v-if="isPaciente">Llenar Formulario</b-nav-item>
          <b-nav-item to="/" v-if="isPaciente">Realizar Diario?</b-nav-item>
          <b-nav-item to="/" v-if="isPaciente">Reportar Problemas</b-nav-item>
          <b-nav-item to="/" v-if="isQuimicoSr"
            >Verificar Fidelidad en Pacientes</b-nav-item
          >
          <b-nav-item to="/" v-if="isQuimicoSr || isQuimicoJr"
            >Visualizar Respuestas del Test 1 en Pacientes</b-nav-item
          >
          <b-nav-item to="/" v-if="isQuimicoSr"
            >Ver listado de seguimiento de Pacientes</b-nav-item
          >
          <b-nav-item to="/" v-if="isQuimicoSr"
            >Seguimientos Farmacoterapeuticos</b-nav-item
          >
          <b-nav-item to="/" v-if="isQuimicoSr"
            >Asignar SFT a Pacientes</b-nav-item
          >
          <b-nav-item to="/" v-if="isQuimicoJr"
            >Listaddo de Pacientes</b-nav-item
          >
          <b-nav-item to="/" v-if="isQuimicoJr">Entrevistas</b-nav-item>
          <b-nav-item to="">Cerrar Sesión</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
          <div v-if="isLoggedIn">
            <b-nav-item-dropdown right>
              <v-avatar color="indigo">
                <v-icon dark> mdi-account-circle </v-icon>
              </v-avatar>
            </b-nav-item-dropdown>
          </div>
        </b-navbar-nav>
      </b-ccollapse>
    </b-navbar>
  </div>
</template>
<script>
export default {
  data: function () {
    return {};
  },
  computed: {
    isLogdedIn() {return this.storage.token != '';},
    IsAdmin() {return this.storage.loggedInUser != null && this.storage.loggedInUser.type == "Administrador"}
  },
};
</script>
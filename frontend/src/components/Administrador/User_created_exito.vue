<template>
  <div class="container">
    <h2><strong> Registro de usuario Exitoso</strong></h2>
    <br />
    <br />
    <img src="../../assets/exito.jpg" />
    <br />
    <br />
    <h4>
      El registro del usuario asociado al correo electronico: {{ email }} se
      realizo exitosamente y sera un(a): {{type_user}}, adicional a esto se le envio un correo electronico a: 
      {{ email }} con la confirmacion de registro.
    </h4>
    <button v-on:click="Inicio" class="btn btn-primary">
      Regresar al menu principal
    </button>
  </div>
</template>
<style scoped>
.container {
  align-content: center;
  padding: 50px;
}
</style>
<script>
import forceLogin from'../utils/force_login';
export default {
  name: "Exito_en_Registro_Usuario",
  data() {
    return {
      email: '',
      type_user: "",
    };
  },
  created() {
    this.email = this.$route.params.email;
    this.type_user = this.$route.params.type_user;
  },
  methods: {
    Inicio() {
      this.$router.push({ name: "Inicio" });
    },
  },
  mixins: [forceLogin]
};
</script>
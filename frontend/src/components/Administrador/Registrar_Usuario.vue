<template>
<div class='container-form'>
        <FlashMessage class="message"></FlashMessage>

  <form
  id="form"
  @submit="checkForm"
>
  <p v-if="errors.length" class="message_error">
    <b>Por favor, corrija el(los) siguiente(s) error(es):</b>
    <ul>
      <li v-bind:key="error" v-for='error in errors'>{{ error }}</li>
    </ul>
  </p>
 <div class="form-group">
    <label for="exampleInputEmail1">Correo electrónico</label>
    <input v-model='email' type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Ingrese un correo electrónico">
    <small id="emailHelp" class="form-text text-muted">Esta información no se compartira con nadie.</small>
  </div>
  <div class="form-group" >
      <label class="mr-sm-2" for="inlineFormCustomSelect">Tipo de Usuario</label>
      <select v-model='type_user' class="custom-select sm-sm-1" id="inlineFormCustomSelect" place-holder='Seleccione'>
        <option value="1">Administrador</option>
        <option value="2">Químico Sr</option>
        <option value="3">Químico Jr</option>
      </select>
    </div>
  <button type="submit" class="btn btn-primary">Registrar</button>

</form>
      <vue-confirm-dialog class="dialog"></vue-confirm-dialog>

</div>
</template>
<style scoped>
.container-form {
  align-content: center;
  padding: 80px;
  margin: 20px;
}
.dialog {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
</style>
<script>
import Api from "../utils/api";
import help from "../utils/function_helps";

export default {
  name: "Registro_Usuario",
  beforeMount() {
    if (this.storage.token == "") {
      this.$router.push({ name: "Login" });
    }
  },
  data: function () {
    return {
      errors: [],
      type_user: null,
      email: null,
    };
  },
  methods: {
    checkForm: function (e) {
      e.preventDefault();
      this.errors = [];

      if (!this.type_user && this.type_user != "Seleccione...") {
        this.errors.push("Por favor eliga un tipo de Usuario");
      }
      if (!this.email) {
        this.errors.push("El correo electrónico es obligatorio.");
      } else if (!this.validEmail(this.email)) {
        this.errors.push("El correo electrónico debe ser válido.");
      }

      if (!this.errors.length) {
        this.handleClick();
        return true;
      }
    },
    validEmail: function (email) {
      var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
    handleClick() {
      this.$confirm({
        title: "Esta a punto de crear un nuevo usuario para el sistema!!",
        message:
          "email: " +
          this.email +
          " tipo de usuario: " +
          help.methods.getTypeuser(this.type_user),
        button: {
          no: "Cancelar",
          yes: "Confirmar",
        },
        /**
         * Callback Function
         * @param {Boolean} confirm
         */
        callback: (confirm) => {
          if (confirm) {
            Api.post(
              "email/",
              {
                email: this.email,
                type_user: this.type_user,
                creado_por: this.storage.username,
              },
              { headers: { token: this.storage.token } }
            )
              .then((exito) => {
                this.$router.push({
                  name: "Registro Usuario Exitoso",
                  params: {
                    email: this.email,
                    type_user: help.methods.getTypeuser(this.type_user),
                  },
                });
              })
              .catch((error) => {
                if (error.response.status == 400) {
                  this.flashMessage.error({
                    title: "Error al registrar correo electronico",
                    message: "El correo ya existe",
                  });
                } else {
                  this.flashMessage.error({
                    title: "Error al registrar correo electronico",
                    message:
                      "Error inesperado intente mas tarde intente de nuevo" +
                      error,
                  });
                }
              });
          }
        },
      });
    },
  },
};
</script>
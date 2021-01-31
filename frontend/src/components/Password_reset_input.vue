<template>
  <div class="grid-item" id="container">
    <FlashMessage class="message"></FlashMessage>
     <v-card class="mx-auto" id='v-card-parametros' max-width="60%" outlined>
  <ul class="list-group" id="ul_list">
   
      <p>
        <strong>Su contraseña debe de cumplir los siguientes parámetros</strong>
      </p>
      <li class="list1">
        No ser tan corta, contener al menos 8 caracteres
      </li>
      <li class="list2">
        No ser una contraseña muy común ejemplo (1234, su nombre de usuario)
      </li>
      <li class="list2">No ser solo numérica</li>
      <li class="list4">
        Usar números y letras (incluso caracteres especiales)
      </li>
    </ul>
    </v-card>
    <v-card
      class="mx-auto"
      max-width="1000"
      outlined
      color="purple"
      id="v-card"
    >
      <form class="needs-validation" @submit="checkForm">
        <div class="row">
          <div class="col-sm">
            <strong>Ingrese su contraseña nueva:</strong>
          </div>
          <div class="col-md-5 mb-1">
            <input
              type="password"
              v-model="password"
              class="form-control"
              id="validationCustom2"
              placeholder="Ingrese su contraseña nueva"
              required
            />
          </div>
          <div class="col-1">
            <span class="span_password1"
              ><b-icon
                id="icon-password"
                :icon="icon2"
                v-on:click="toggle2"
                scale="1.4"
              ></b-icon
            ></span>
          </div>
        </div>
        <div class="row">
          <div class="col-sm">
            <strong>Ingrese su contraseña nueva nuevamente:</strong>
          </div>
          <div class="col-md-5 mb-1">
            <input
              type="password"
              v-model="repet_password"
              class="form-control"
              id="validationCustom3"
              placeholder="Ingrese su contraseña nueva otra vez."
              required
            />
          </div>
          <div class="col-1">
            <span class="span_password2"
              ><b-icon
                id="icon-password"
                :icon="icon3"
                v-on:click="toggle3"
                scale="1.4"
              ></b-icon
            ></span>
          </div>
        </div>

        <div class="col-md-4 mb-1">
          <button class="btn btn-primary">Reestablecer contraseña</button>
          <small id="emailHelp6" class="form-text text-muted"
            >Para reestablecer su contraseña por favor llene todos los
            campos.</small
          >
        </div>
      </form>
    </v-card>
  </div>
</template>

<style scoped>
#container {
  padding: 80px;
}
#v-card {
  padding: 30px;
}
#ul_list {
  padding: 30px;
}
.message {
  position: relative;
  z-index: 5;
}
#v-card-parametros{
  padding: 20px;
  margin: 3px;
}
</style>

<script>
var state2 = false;
var state3 = false;
import Api from "./utils/api";
export default {
  data() {
    return {
      password: "",
      repet_password: "",
      icon2: "eye-fill",
      icon3: "eye-fill",
    };
  },
  methods: {
    checkForm(evt) {
      evt.preventDefault();
      if (this.password != this.repet_password) {
        this.flashMessage.error({
          title: "Error al reestablecer la contraseña",
          message: "Las contraseñas no coinciden",
        });
      } else {
        Api.post("api/password_reset/confirm/", {
          token: this.$route.query.token,
          password: this.password,
        })
          .then((response) => {
            if (response.data.status == "OK") {
              this.flashMessage.success({
                title: "Éxito",
                message: "su contraseña se reestablecio correctamente, ya puede iniciar sesión con su nueva contraseña..",
                time:4500,
              },{
                   destroyed: this.returnLogin
              });
                this.password= "";
                this.repet_password= "";
            }
          })
          .catch((error) => {
            var value = error.message;
            if (value == 'Request failed with status code 400') {
              this.flashMessage.error({
                title: "Error",
                message:
                  "Su contrseña no cumple con los estandares detallados, por favor verificar estos... ",
              });
            } else if (value == 'Request failed with status code 404') {
              this.flashMessage.error({
                title: "Error al cambiar la contraseña",
                message:
                  "Al parecer usted ya uso o expiró este enlace, por favor solicitar nuevamente el cambio de contraseña ",
              });
            } else {
              this.flashMessage.error({
                title: "Error inisperado",
                message: "Por favor intente mas tarde " + error,
              });
            }
          });
      }
    },
    returnLogin() {
      this.$router.replace({ name: "Login" });
    },
    toggle2() {
      this.icon2 = state2 ? "eye-fill" : "eye-slash-fill";
      if (state2) {
        document
          .getElementById("validationCustom2")
          .setAttribute("type", "password");
        state2 = false;
      } else {
        document
          .getElementById("validationCustom2")
          .setAttribute("type", "text");
        state2 = true;
      }
    },
    toggle3() {
      this.icon3 = state3 ? "eye-fill" : "eye-slash-fill";
      if (state3) {
        document
          .getElementById("validationCustom3")
          .setAttribute("type", "password");
        state3 = false;
      } else {
        document
          .getElementById("validationCustom3")
          .setAttribute("type", "text");
        state3 = true;
      }
    },
  },
};
</script>
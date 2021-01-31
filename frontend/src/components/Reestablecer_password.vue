<template>
  <div class="container" id="container">
    <FlashMessage class="message"></FlashMessage>
    <h2 class="h2">
      Aqui podrá reestablecer su contraseña en caso de no recordarla<br />
      Con el correo electrónico asociado a Disprodelsa..
    </h2>
    <p id="mensaje_id">{{ mensaje }}</p>
    <form class="needs-validation" @submit="buscar_correo">
      <div class="col-md-8 mb-3">
        <label for="validationCustom3">Correo Electronico</label>
        <input
          type="email"
          v-model="email_request"
          class="form-control"
          id="validationCustom03"
          placeholder="Ingrese un correo electronico que haya sido registrado antes"
          required
          title="Lütfen işaretli yerleri doldurunuz"
        />
        <small id="emailHelp4" class="form-text text-muted">{{
          mensaje_small
        }}</small>
      </div>
      <div class="col-md-4 mb-3">
        <button class="btn btn-primary">Comprobar correo</button>
      </div>
    </form>
  </div>
</template>

<style scoped>
.container {
  padding: 15%;
  margin: 2px;
}
h2 {
  font-size: 25px;
}


</style>

<script>
import Api from "./utils/api";
export default {
  data() {
    return {
      mensaje: "",
      exito_email: false,
      email_request: "",
      email_finding: "",
      mensaje_small: "Esta información no se compartira con nadie.",
    };
  },
  methods: {
    buscar_correo(evt) {
      evt.preventDefault();
      Api.get("usuarios%20del%20sitema/", {
        auth: { username: "dalede", password: "1234" },
      })
        .then((users) => {
          users.data.filter((user) => {
            if (user.email == this.email_request) {
              this.email_finding = user.email;
            }
          });
          if (this.email_finding != "") {
            Api.post("api/password_reset/", {
              'email': this.email_finding,
            })
              .then((exito) => {
                this.flashMessage.success({
                  icon: true,
                  title: "Email encontrado",
                  message:
                    "Se procedio a enviarle un correo un electronico para empezar el proceso de reestablecimiento de su contraseña" +
                    " por favor revise su buzón.",
                  time: 10000,
                });
                this.$router.push({name:'Login'});
              })
              .catch((error) => {
                this.flashMessage.error({
                  icon: true,
                  title: "Error al reestablecer su contraseña",
                  message: "Error inesperado por favor intente mas tarde."+error,
                });
              });
          } else {
            this.flashMessage.error({
              icon: true,
              title: "Error al comprobar su correo electrónico",
              message:
                "Al parecer no tenemos registrado su correo electronico como usuario" +
                " para este sistema, si necesita ayuda contactese con nostrosos estaremos gustosos a ayudarle o no se ha creado una cuenta con nosotros.",
            });
          }
          this.mensaje = "";
          this.email_request = "";
          this.email_finding = "";
        })
        .catch((error) => {
          this.flashMessage.error({
            icon: true,
            title: "Error al comprobar su correo electrónico",
            message: "Error inesperado por favor intente mas tarde.",
          });
        });
    },
  },
  watch: {
    mensaje_small: function (val, val2) {
      this.mensaje_small = "Esperando a que termine de escribir...";
    },
  },
};
</script>
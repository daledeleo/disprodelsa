<template>
  <div class='container' id='container'>
    <FlashMessage class="message"></FlashMessage>
    <h2 class='h2'>Aqui podrá reestablecer su contraseña en caso de no recordarla<br> Con el correo electrónico asociado a Disprodelsa..</h2>
    <p id='mensaje_id'>{{mensaje}}</p>
    <form class="needs-validation" @submit="buscar_correo">
      <div class="col-md-8 mb-3">
        <label for="validationCustom3">Correo Electronico</label>
        <input type="email" v-model="email" class="form-control" id="validationCustom03" placeholder="Ingrese un correo electronico que haya sido registrado antes" required/>
        <small id="emailHelp4" class="form-text text-muted">Esta información no se compartira con nadie.</small>
      </div>
      <div class="col-md-4 mb-3">
        <button class="btn btn-primary">Comprobar correo</button>
        
      </div>
    </form>
  </div>
</template>

<style scoped>
.container{
    padding: 15%;
    margin: 2px;
}
h2{
  font-size: 25px;
}
</style>

<script>
import Api from "./utils/api";
export default {
  data() {
    return {
      mensaje: "",
      exito: false,
      email: "",

    };
  },
  methods: {
    buscar_correo(evt) {
      evt.preventDefault();
      Api.get("email/", { auth: { username: "admin", password: "admin" } })
        .then((exito) => {
          exito.data.filter((email) => {
            if (email.email == this.email_object) {
              this.email = email.email;
            }
          });
          if (this.email != "") {
            this.mensaje='Email encontrado, se procedio a enviarle un correo un electronico para empezar el proceso de reestablecimiento de contraseña'
          } else {
            this.flashMessage.error({
              icon: true,
              title: "Error al comprobar su correo electrónico",
              message:
                "Al parecer no tenemos registrado su correo electronico como usuario" +
                " para este sistema, si necsita ayuda contactese con nostrosos estaremos gustosos a ayudarle.",
            });
          }
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
};
</script>
<template>
  <div class="grid-container">
    <FlashMessage class="message" :position="'right bottom'"></FlashMessage>
    <h5 class="h5"><strong>Datos Personales</strong></h5>
    <br />
    <div class="grid-item">
      <v-card class="mx-auto" max-width="1000" outlined color="purple">
        <div class="row">
          <div class="col-sm">
            <strong>Nombre:</strong>
          </div>
          <div class="col-sm">
            {{ nombre }}
          </div>
        </div>
        <div class="row">
          <div class="col-sm">
            <strong>Apellidos:</strong>
          </div>
          <div class="col-sm">
            {{ apellidos }}
          </div>
        </div>
        <div class="row">
          <div class="col-sm">
            <strong>Correo:</strong>
          </div>
          <div class="col-sm">
            {{ email }}
          </div>
        </div>
        <div class="row">
          <div class="col-sm">
            <strong>Nombre de usuario:</strong>
          </div>
          <div class="col-sm">
            {{ usuario }}
          </div>
        </div>
      </v-card>
    </div>
    <br /><br /><br /><br />
    <h5 class="h5"><strong>Cambio de contraseña</strong></h5>
    <br />
    <div class="grid-item">
      <v-card class="mx-auto" max-width="1000" outlined color="purple">
        <form class="needs-validation" @submit="buscar_correo">
          <div class="row">
            <div class="col-sm">
              <strong>Ingrese su contraseña actual:</strong>
            </div>
            <div class="col-md-5 mb-1">
              <input
                type="password"
                v-model="password_actual"
                class="form-control"
                id="validationCustom1"
                placeholder="Ingrese su contraseña actual"
                required
              />
            </div>
            <div class="col-1">
              <span class="span_password1"
                ><b-icon
                  id="icon-password"
                  :icon="icon1"
                  v-on:click="toggle1"
                  scale="1.4"
                ></b-icon
              ></span>
            </div>
          </div>
          <div class="row">
            <div class="col-sm">
              <strong>Ingrese su contraseña nueva:</strong>
            </div>
            <div class="col-md-5 mb-1">
              <input
                type="password"
                v-model="password_nueva"
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
                v-model="password_nueva_repetida"
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
            <button class="btn btn-primary">Cambiar contraseña</button>
            <small id="emailHelp6" class="form-text text-muted"
              >Para cambiar su contraseña por favor llene todos los campos.</small
            >
          </div>
        </form>
      </v-card>
    </div>
  </div>
</template>

<style scoped>
.grid-container {
  margin-top: 30px;
}
.row {
  padding: 5px;
  margin: 5px;
}
#icon-password {
  position: 10px;
}
.message{
    position:relative;
    z-index:5;
}
</style>

<script>
import Api from "./utils/api";
import forceLogin from './utils/force_login';

var state1 = false;
var state2 = false;
var state3 = false;
export default {
  data() {
    return {
      email: localStorage.getItem("email"),
      usuario: localStorage.getItem("username"),
      apellidos: "",
      nombre: "",
      password_actual: "",
      password_nueva: "",
      password_nueva_repetida: "",
      icon1: "eye-fill",
      icon2: "eye-fill",
      icon3: "eye-fill",
      pk_user:'',
    };
  },
  methods: {
    getPerfil() {
      Api.get("usuarios%20del%20sitema/", {
        headers: { token: localStorage.getItem("token") },
      })
        .then((data) => {
          data = data.data[0];
          this.apellidos = data.apellido_paterno + " " + data.apellido_materno;
          this.nombre = data.nombre;
          this.pk_user=data.id
        })
        .catch((error) => {
          this.flashMessage.error({
            icon: true,
            title: "No se pudo acceder a su información",
            message: "Por favor intente acceder a su perfil mas tarde " + error,
          });
          this.$router.push({ name: "Inicio" });
        });
    },
    buscar_correo(evt) {
      evt.preventDefault();
      if(this.password_nueva==this.password_nueva_repetida){
          Api.patch("usuarios%20del%20sitema/"+this.pk_user+'/',{
              currentPassword:this.password_actual,
              password:this.password_nueva,
          },{headers: { token: localStorage.getItem("token") }}).then(exito=>{
            this.flashMessage.success({icon:true,title: 'Éxito al cambiar de contraseña', message: 'Su contraseña fue cambiada exitosamente..'});
            this.password_actual='';
            this.password_nueva='';
            this.password_nueva_repetida='';
        }).catch(error=>{
            if(error.response.status==403){
                this.flashMessage.error({icon:true,title: 'Error al cambiar la contraseña', message: 'La contraseña actual no coincide',blockClass: 'custom-block-class'});
            }else{
            this.flashMessage.error({icon:true,title: 'Error al cambiar la contraseña', message: 'Por favor intente mas tarde..',blockClass: 'custom-block-class'});
            }
        })
      }else{
           this.flashMessage.error({icon:true,title: 'Error al cambiar la contraseña', message: 'Por favor verifique que las contraseñas coincidan..'});
        }
    },
    toggle1() {
      this.icon1 = state1 ? "eye-fill" : "eye-slash-fill";
      if (state1) {
        document
          .getElementById("validationCustom1")
          .setAttribute("type", "password");
        state1 = false;
      } else {
        document
          .getElementById("validationCustom1")
          .setAttribute("type", "text");
        state1 = true;
      }
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
  created() {
    this.getPerfil();
  },
  mixins:[forceLogin],
};
</script>
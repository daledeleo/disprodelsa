
<template>

  <div class="container" id="container"  :style="{'background-image':'url(https://www.farmaceuticonline.com/wp-content/uploads/2019/07/medicaments-presentacio.jpg)'}">
    <div class="d-flex justify-content-center h-100">
      <FlashMessage class="message"></FlashMessage>
      <div class="card">
        <div>
          <img
            class="img img_logo"
            src="../assets/Logo_disprodelsa_con_letras.jpeg"
          />
        </div>

        <div class="card-header">
          <h3>Inicie Sesión</h3>
          <h4>Bienvenido inicie sesion para poder usar nuestro sistema</h4>
        </div>
        <div class="card-body">
          <form @submit="onSubmit">
            <div class="input-group form-group">
              <div class="input-group-prepend">
                <span class="input-group-text"
                  ><b-icon icon="person-fill"></b-icon></span>
              </div>
              <input type="text" v-model="form.username" class="form-control" placeholder="Ingrese su nombre de usuario">
            </div>
            <div class="input-group form-group">
              <div class="input-group-prepend">
                <span class="input-group-text" ><b-icon icon="key-fill"></b-icon></span>
              </div>
              <input id="password" type="password" v-model="form.password" class="form-control" placeholder="Ingrese su contrseña"><div class="input-password">
                <span class="span_password"><b-icon id='icon-password' :icon="icon" v-on:click="toggle()" scale='1.5'></b-icon></span>
              </div>
            </div>

            <div class="form-group">
              <input
                type="submit"
                value="Iniciar Sesión"
                class="btn float-center login_btn"
              >
            </div>
          </form>
        </div>
        <div class="card-footer">
          <div class="d-flex justify-content-center links">
            ¿Desea tener una cuenta?<a href="/Crear-cuenta">Crear cuenta</a>
          </div>
          <div class="d-flex justify-content-center link">
            <a href="#">¿Olvido su contraseña?</a>
          </div>
        </div>
      </div>
    </div>
  </div>
  
</template>
<style scoped >
@import "./css/login.css";
</style>

<script>
import Api from "./utils/api";
var state=false;

export default {
  name: "Login",
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
      icon: 'eye-fill',
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      Api.post("login/", {
        username: this.form.username,
        password: this.form.password,
      })
        .then((tokenResponse) => {
          this.storage.token = tokenResponse.data.token;
          this.storage.username = tokenResponse.data.username;
          this.storage.email = tokenResponse.data.email.split("-")[0];
          this.storage.type_user = tokenResponse.data.type_user;
          this.$router.push({name:"Inicio"});
        })
        .catch((error) => {
          if (error.response) {
            const status = error.response.status;
            if (status == 401) {
              this.flashMessage.error({icon:true,title: 'Error en el inicio de sesión', message: 'Las credenciales proporcionadas fueron incorrectas, ' 
              +'por favor intente denuevo con su usuario y su contraseña correcta. Consejo: verifique que las mayúsculas automáticas no esten activadas'});
            } else if (status == 404) {
              this.flashMessage.error({icon:true,title: 'Error en el inicio de sesión', message: 'Las credenciales proporcionadas fueron incorrectas, ' 
              +'por favor intente denuevo con su usuario y su contraseña correcta. Consejo: verifique que las mayúsculas automáticas no esten activadas'});
            } else {
               this.flashMessage.error({title: 'Error en el inicio de sesión', message: 'Ha ocurrido un error por favor intente de nuevo'});
            }
          } else {
               this.flashMessage.error({title: 'Error en el inicio de sesión', message: 'Error inesperado intente mas tarde intente de nuevo'+error});
          }
        });
    },
    toggle(){
      this.icon=state ? "eye-fill": 'eye-slash-fill';
      if (state){
        document.getElementById("password").setAttribute("type","password");
        state=false;
      }else{
        document.getElementById('password').setAttribute("type","text");
        state=true;
      }
    }
  },
  computed:{
    
  }
};
</script>
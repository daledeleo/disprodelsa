<template>
  <div class="pt-3" style="padding-left: 14px; padding-right: 14px">
    <b-alert v-if="error" show variant="danger">
      Error! Usuario o Contraseña Incorrectos
    </b-alert>

    <b-form @submit="onSubmit">
      <img src="../assets/Logo_disprodelsa_con_letras.jpeg" align-h="center" />
      <b-form-group id="input-group-1" label="Usuario:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="form.username"
          type="text"
          required
          placeholder="Nombre de usuario"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Contraseña: " label-for="input-2">
        <b-form-input
          id="input-2"
          type="password"
          v-model="form.password"
          required
          placeholder="Ingrese la contraseña"
        ></b-form-input>
      </b-form-group>

      <b-container>
        <b-row align-h="center">
          <b-col cols="3" class="text-center">
            <b-button type="submit" variant="primary">Iniciar Sesión</b-button>
          </b-col>
          <b-col cols="3" class="text-center">
            <b-button to="" variant="secondary">Crear Cuenta</b-button>
          </b-col>
          <b-col cols="3" class="text-center">
            <b-button to="" variant="warning">Olvide mi contraseña</b-button>
          </b-col>
        </b-row>
      </b-container>
    </b-form>
  </div>
</template>

<script>
import Api from './utils/api'
//import Message from './utils/message'
export default {
    name: 'Login',
    data(){
        return {
            form:{
                username:'',
                password:'',
                },
            error:false
        }
    },
    methods:{
        onSubmit(evt){
            evt.preventDefault()
            Api.post("login/",{
                "username":this.form.username,
                "password":this.form.password
            })
            .then(tokenResponse=>{
                this.storage.token=tokenResponse.data.token;
                Message.success("Ha iniciado sesión con éxito")
            })
            .catch((error)=>{
                if(error.response){
                    const status =error.response.status
                    if(status==401){
                        Message.error("Las credenciales no son válidad, intente de nuevo con las credenciales válidas")

                    }else if(status==404){
                        Message.error("El usuario no se encuentra registrado")
                    }else{
                        Message.error("Ha ocurrido un error intente de nuevo")
                    }
                }else{
                    Message.error("Error inesperado intente denuevo mas tarde")
                }
            })
        }
    }
        
}
</script>
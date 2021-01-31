
<template>
<div>
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
  <form class="needs-validation" @submit="buscar_correo"> 
    <div class="col-md-6 mb-3">
      <label for="validationCustom3">Correo Electronico</label>
      <input type="email" :disabled='form.desabilitar_comprobar_correo' v-model="form.email" class="form-control" id="validationCustom03" placeholder="Ingrese un correo electronico que haya sido registrado antes" required />
      <small id="emailHelp4" v-if="form.desabilitar_comprobar_correo" class="form-text text-muted">Esta información no se compartira con nadie. <strong>{{form.mensaje_confirmacion}}</strong></small>
       <small id="emailHelp4" v-else class="form-text text-muted">Esta información no se compartira con nadie.</small>
    </div>
      <div class="col-md-4 mb-3">
        <div ><button class="btn btn-secondary" :disabled='form.desabilitar_comprobar_correo'>Comprobar correo</button></div>
      </div>
  </form>
  <form class="needs-validation"  @submit="crear_usuario">
    <div class="form-row">
      <div class="col-md-4 mb-3">
        <label >Nombre</label>
        <input type="text"  v-model="form.nombre" class="form-control" id="validationCustom01" placeholder="Ingrese su nombre" required/>
        <small id="emailHelp1" class="form-text text-muted">Esta información no se compartira con nadie.</small>
      </div>
      
      <div class="col-md-4 mb-3">
        <label for="validationCustom02">Apellido Paterno</label>
        <input type="text"  v-model="form.apellido_paterno" class="form-control" id="validationCustom02" placeholder="Ingrese su apellido paterno" required/>
        <small id="emailHelp2" class="form-text text-muted">Esta información no se compartira con nadie.</small>
      </div>

      <div class="col-md-4 mb-3">
        <label for="validationCustomUsername">Apellido Materno</label>
      <input type="text"  v-model="form.apellido_materno" class="form-control" id="validationCustomUsername" placeholder="Ingrese su apellido materno" aria-describedby="inputGroupPrepend" required/>
      <small id="emailHelp3" class="form-text text-muted">Esta información no se compartira con nadie.</small>
     </div>
    </div>

    <div class="form-row">
     

      <div class="col-md-4 mb-3">
        <label for="validationCustom4">Nombre de usuario</label>
        <input type="text"  v-model="form.username" class="form-control" id="validationCustom44" placeholder="Ingrese un nombre de usuario" required/>
        <small id="emailHelp5" class="form-text text-muted">Esta información no se compartira con nadie.</small>
      </div>

    
      <div class="col-md-4 mb-1">
        <label for="validationCustom5">Contraseña</label>
        <input type="password"  v-model="form.password" class="form-control" id="validationCustom55" placeholder="Ingrese una contraseña" required/>
        <span class="span_password"><b-icon id='icon-password' :icon="icon" v-on:click="toggle" scale='1.5'></b-icon></span>
        <small id="emailHelp6" class="form-text text-muted">Esta información no se compartira con nadie.</small>
      </div>

      <div class="col-md-4 mb-1">
        <label for="validationCustom555">Repita la Contraseña</label>
        <input type="password"  v-model="form.password_repetida" class="form-control" id="validationCustom05" placeholder="Ingrese nuevamente la contraseña" required/>
        <div class="span_password2">
          <span class="span_password2"><b-icon id='icon-password2' :icon="icon2" v-on:click="toggle2" scale='1.5'></b-icon></span>
        </div>
      </div>
       <div class="col-md-4 mb-3">

        <label for="validationCustom4">Tipo de usuario</label>
        <input type="text"  v-model="form.tipo_usuario" class="form-control" id="validationCustom04" placeholder='Por favor verifique su correo electronico' required :disabled="ban"/>
      </div>
    </div>
    <button class="btn btn-primary" :disabled="isInValid">Crear Cuenta</button>
    <small v-if='form.desabilitar_crear_cuenta' id="emailHelp7" class="form-text text-muted">Para activar este boton de <strong>Crear Cuenta</strong> 
    debe de dar click en <strong>Comprobar correo</strong> para verificar su correo electronico. <a href="/">Ir al Inicio</a></small>
    <small v-else id="emailHelp7" class="form-text text-muted"><strong>Correo comprobado con exito </strong> <a href="/">Ir al Inicio</a></small>
  </form>
  </div>
</template>

<style scoped>
#v-card-parametros{
  padding: 20px;
  margin: 3px;
}
</style>

<script>
import Api from './utils/api';
import help from './utils/function_helps';
var state=false;
var state2=false;
var email_f='';
export default {
  name: "Crear_cuenta",
  data(){
    return{
      form:{
        nombre:'',
        apellido_paterno:'',
        apellido_materno:"",
        email:"",
        password:'',
        password_repetida:'',
        desabilitar_crear_cuenta:true,
        desabilitar_comprobar_correo:false,
        tipo_usuario:'',
        mensaje_confirmacion:'',
      },
      ban:true,
      icon:"eye-fill",
      icon2:"eye-fill",
    }
  },
  methods:{
   buscar_correo(evt){
    evt.preventDefault();
    //console.log(process.env.VUE_APP_USERNAME)
     Api.get('email/',{auth:{username:'dalede',password:'1234'}}).then(exito=>{
       
       exito.data.filter(email=>{
         if(email.email==this.form.email){
           email_f=email
           }
       });
       if(email_f != ''){
          this.form.tipo_usuario=help.methods.getTypeuser(email_f.type_user)
          document.getElementById('validationCustom04').setAttribute('placeholder',this.form.tipo_usuario)
          this.form.desabilitar_comprobar_correo=true;
          this.form.mensaje_confirmacion='Correo confirmado con exito';
       }else{
          this.flashMessage.error({icon:true,title: 'Error al comprobar su correo electrónico', message: 'Al parecer no tenemos registrado su correo electronico como usuario'+ 
            ' para este sistema, si necesita ayuda contactese con nostrosos estaremos gustosos a ayudarle.'});
       }
     }).catch(error=>{
       this.flashMessage.error({icon:true,title: 'Error al comprobar su correo electrónico', message: 'Error inesperado por favor intente mas tarde.'});
     })
   },
   crear_usuario(evt){
     evt.preventDefault();
     if(this.form.password!=this.form.password_repetida){
       this.flashMessage.warning({icon:true,title: 'Las contraseñas no coinciden', message: 'Por favor verifique que su contraseña.'});
     }else{
       Api.post('usuarios%20del%20sitema/',{
          creado_por:'self',
          email:email_f.email,
          tipo_usuario:this.form.tipo_usuario,
          nombre:this.form.nombre,
          apellido_paterno:this.form.apellido_paterno,
          apellido_materno:this.form.apellido_materno,
          password:this.form.password,
          username:this.form.username,
       },{auth:{username:'dalede',password:'1234'}},{headers:{}}).then(exito=>{
          this.flashMessage.success({icon:true,title: 'Exito al crear la cuenta', message: 'Usted ya forma parte de nuestro grupo de usuarios, gracias por su registro, ya puede iniciar sesión..'});
          this.$router.push({name:"Login"});
       }).catch(error=>{
         var error_specific=error.response.request.response
         if(error_specific.email!=undefined){
            this.flashMessage.error({icon:true,title: 'Error al crear una cuenta', message: 'Ya existe una cuenta asociada a este correo'});
         }else if(error_specific.password!=undefined){
            this.flashMessage.error({icon:true,title: 'Error al crear una cuenta', message: 'su contraseña no cumple con los estandares establecidos'});
         }else if(error_specific.username!=undefined){
            this.flashMessage.error({icon:true,title: 'Error al crear una cuenta', message: 'el usuario: '+this.username+' ya esta en uso, intento con otro'});
         }else{
            this.flashMessage.error({icon:true,title: 'Error al crear una cuenta', message: 'Esto no tenia que haber pasado por favor intente mas tarde..'});
         }
       })
     }
   },
    toggle(){
      this.icon=state ? "eye-fill": 'eye-slash-fill';
      if (state){
        document.getElementById("validationCustom55").setAttribute("type","password");
        state=false;
      }else{
        document.getElementById('validationCustom55').setAttribute("type","text");
        state=true;
      }
    },
     toggle2(){
      this.icon2=state2 ? "eye-fill": 'eye-slash-fill';
      if (state2){
        document.getElementById("validationCustom05").setAttribute("type","password");
        state2=false;
      }else{
        document.getElementById('validationCustom05').setAttribute("type","text");
        state2=true;
      }
    },
  },
  computed:{
    isInValid(){
      return !this.form.desabilitar_comprobar_correo || this.nombre=='' || this.form.apellido_paterno=='' || this.form.apellido_materno=='' || this.form.email==''||
      this.password=='' || this.username=='' || this.form.password_repetida=="" || this.form.tipo_usuario=="";
    }
  }
};
</script>
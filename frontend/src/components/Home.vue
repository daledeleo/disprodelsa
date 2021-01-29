<template>
<div>
    <FlashMessage class="message"></FlashMessage>
    <h2 id="mensaje_bienvenida" class='mensaje_bienvenida'>
        Bienvenido {{username}}
    </h2>
    </div>
</template>
<style scoped>
@import "./css/home.css";
</style>
<script>
import forceLogin from './utils/force_login';
export default {
    name:'Inicio',
    data(){
        return{
            username:localStorage.getItem('username')
        }
    },
    methods:{
        Inicio:function(){
               this.flashMessage.success({icon:true,title: 'Inicio de sesión con éxito', message: 'Bienvenido usuario: '+
          localStorage.getItem('username')+ '\n usted es un tipo de usuario: '+ localStorage.getItem('type_user')+ '\n correo: '+ localStorage.getItem('email')});
        },
    },
    created(){
        if(localStorage.getItem('token')!=null){
        this.Inicio()
        }
    },
    mixins:[forceLogin]
 
}
</script>
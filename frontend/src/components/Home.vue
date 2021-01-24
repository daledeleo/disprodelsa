<template>
<div>
    <FlashMessage class="message"></FlashMessage>
    <h2 id="mensaje_bienvenida" class='mensaje_bienvenida'>
        Bienvenido {{this.storage.username}}
    </h2>
    </div>
</template>
<style scoped>
@import "./css/home.css";
</style>
<script>
export default {
    name:'Inicio',
    methods:{
        Inicio:function(){
               this.flashMessage.success({icon:true,title: 'Inicio de sesión con éxito', message: 'Bienvenido usuario: '+
          this.storage.username+ '\n usted es un tipo de usuario: '+ this.storage.type_user+ '\n correo: '+ this.storage.email});
        },
    },
    beforeMount(){
        if (this.storage.token==''){
            this.$router.push({name:'Login'});
        }else{
        this.Inicio()
        }
    }
 
}
</script>
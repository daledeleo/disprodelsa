import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/Login'
import Home from '../components/Home'
import Usuarios from '../components/Administrador/Usuarios_home'
import Registro_Usuario from '../components/Administrador/Registrar_Usuario';
import Registro_Usuario_Exito from '../components/Administrador/User_created_exito';
import Crear_cuenta from '../components/Crear_cuenta'
import Logout from '../components/Logout';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path:"/Inicio",
      name:"Inicio",
      component:Home,
    },
    {
      path:'/Inicio/Usuarios',
      name:"Usuarios",
      component:Usuarios,
    },
    {
      path:'/Inicio/Usuarios/Registrar',
      name:'Registro Usuario',
      component:Registro_Usuario,
    },
    {
      path:'/Inicio/Usuarios/Registrar/Exito',
      name:'Registro Usuario Exitoso',
      component:Registro_Usuario_Exito,
    },
    {
      path:"/Crear-cuenta",
      name:"Crear Cuenta",
      component:Crear_cuenta,
    },
    {
      path:'/Logout',
      name:'Logout',
      component:Logout,
    }
  ],
  mode:"history"
})

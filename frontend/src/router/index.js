import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ListaProductos from "@/components/Productos/ListaProductos"
import EditProducto from "@/components/Productos/EditProducto"

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path:'/productos',
      name:'ListaProductos',
      component:ListaProductos
    },
    {
      path:'/productos/:productoId/edicion',
      name:'EdicionProducto',
      component:EditProducto
    },
  ],
  mode:"history"
})

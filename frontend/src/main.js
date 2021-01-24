import '@babel/polyfill'
import 'mutationobserver-shim'
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App'
import router from './router'
import { BootstrapVue, BootstrapVueIcons  } from 'bootstrap-vue';
import ReactiveStorage from "vue-reactive-localstorage";
import FlashMessage from '@smartweb/vue-flash-message';
import Vuetify from "vuetify"
import VueConfirmDialog from 'vue-confirm-dialog'
 
Vue.use(VueConfirmDialog)
Vue.component('vue-confirm-dialog', VueConfirmDialog.default)

import 'vuetify/dist/vuetify.min.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap-vue/dist/bootstrap-vue-icons.min.css'

Vue.use(FlashMessage);
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(Vuetify);

Vue.use(ReactiveStorage, {
  "token": "",
  "type_user": '', 
  "otherUserPk": 0,
  "loggedInUser": {},
  "username":'',
  "email":''
});

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  
})

<template>
  <div>
    <h2 class="h2">{{ title }}</h2>
    <form class="form" @submit="onSubmit">
      <div class="form-row">
        <div class="col-md-3">
          <input
            class="form-control mr-sm-1"
            type="search"
            placeholder="Buscar"
            aria-label="Search"
            v-model="filter"
          />
          <small
            >Puede hacer busquedas por correo, username, nombre y
            apellidos</small
          >
        </div>
      </div>
      <label for="inputState">Filtrar por tipo de usuario:</label>
      <div class="col-md-3 mb-2">
        <select id="inputState" class="form-control" v-model="tipo_usuario">
          <option selected>Quimico Sr</option>
          <option>Quimico Jr</option>
        </select>
      </div>
    </form>
    <Esqueleto :usuarios="usuarios"></Esqueleto>
    <h5 v-if="usuarios.length < 1" class='h3'>No hay usuarios disponibles</h5>
  </div>
</template>

<style scoped>
.v-card {
  margin-top: 20px;
  width: 300;
}
.h2 {
  padding: 2px;
  text-align: center;
    font-weight: bold;
}
.h3 {
    padding: 20px;
    text-align: center;
    font-size: 20px;
}
</style>

<script>
import Api from "../utils/api";
import Esqueleto from "./Esqueleto_User";
import forceLogin from "../utils/force_login";

export default {
  components: { Esqueleto },
  data() {
    return {
      usuarios: [],
      tipo_usuario: "Quimico Sr",
      title: "Usuarios Quimico Sr",
      filter: "",
      selected: "A",
      options: [
        { text: "Uno", value: "A" },
        { text: "Dos", value: "B" },
        { text: "Tres", value: "C" },
      ],
    };
  },
  created() {
    Api.get("usuarios%20del%20sitema/", {
      headers: { token: localStorage.getItem("token") },
    })
      .then((data) => {
        data.data.filter((usuario) => {
          if (usuario.tipo_usuario == this.tipo_usuario) {
            this.usuarios.push(usuario);
          }
        });
      })
      .catch((error) => {
        alert(error);
      });
  },

  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      var usuarios_nuevos = [];
      this.usuarios.filter((usuario) => {
        if (this.filter == usuario.username) {
          usuarios_nuevos.push(usuario);
        } else if (this.filter == usuario.email) {
          usuarios_nuevos.push(usuario);
        } else if (this.filter == usuario.nombre) {
          usuarios_nuevos.push(usuario);
        } else if (this.filter == usuario.apellido_paterno) {
          usuarios_nuevos.push(usuario);
        } else if (this.filter == usuario.apellido_materno) {
          usuarios_nuevos.push(usuario);
        }
        this.usuarios = usuarios_nuevos;
        if (this.filter == "") {
          this.getData();
        }
      });
    },
    getData() {
      Api.get("usuarios%20del%20sitema/", {
        headers: { token: localStorage.getItem("token") },
      })
        .then((data) => {
          data.data.filter((usuario) => {
            if (usuario.tipo_usuario == this.tipo_usuario) {
              this.usuarios.push(usuario);
            }
          });
        })
        .catch((error) => {
          alert(error);
        });
    },
  },
  watch: {
    filter: function () {
      if (this.filter == "") {
        this.usuarios = [];

        this.getData();
      }
    },
    tipo_usuario: function () {
      if (this.tipo_usuario == "Quimico Sr") {
        this.title = "Usuarios Químicos Sr";
        this.usuarios = [];
        this.getData();
      } else if (this.tipo_usuario == "Quimico Jr") {
        this.title = "Usuarios Químicos Jr";
        this.usuarios = [];

        this.getData();
      }
    },
  },
  mixins: [forceLogin]
};
</script>
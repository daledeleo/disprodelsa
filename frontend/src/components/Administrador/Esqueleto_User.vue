<template>
  <div class="grid">
    <div class="row">
      <div class="col-4" v-bind:key="usuario.id" v-for="usuario in usuarios">
        <v-card class="v-card" elevation="40" shaped max-width="280">
          <v-card-title
            ><strong>{{ usuario.username }}</strong></v-card-title
          >
          <v-card-text
            ><strong>Nombre: </strong>{{ usuario.nombre }} <br />
            <strong>Apellidos:</strong> {{ usuario.apellido_paterno }}
            {{ usuario.apellido_materno }}<br />
            <strong> Correo: </strong>{{ usuario.email }}<br />
            <strong>Tipo de usuario:</strong>{{ usuario.tipo_usuario }}
          </v-card-text>
        </v-card>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Esqueleto",
  props: {
    usuarios: Array,
    selection: 1,
  },
};
</script>
<template>
  <div class="grid-container">
    <div class="grid-item">
      <v-card class="mx-auto" max-width="400" outlined color='purple'>
        <v-list-item three-line>
          <v-list-item-content>
            <div class="overline mb-4">Registrar Usuarios</div>
            <v-list-item-subtitle
              >Aqui podra registrar nuevos usuarios <br />para que puedan
              acceder al sistema.</v-list-item-subtitle
            >
          </v-list-item-content>

          <b-icon icon="person-plus" scale="3"></b-icon>
        </v-list-item>

        <v-card-actions>
          <v-btn to='/Inicio/Usuarios/Registrar' outlined rounded text> Entrar </v-btn>
        </v-card-actions>
      </v-card>
    </div>
    <div class="grid-item">
      <v-card class="mx-auto" max-width="400" outlined color='purple'>
        <v-list-item three-line>
          <v-list-item-content>
            <div class="overline mb-4">Ver Usuarios</div>
            <v-list-item-subtitle
              >Aquí podra visualizar a todos los <br >usuarios del sistema.</v-list-item-subtitle
            >
          </v-list-item-content>

          <b-icon icon="person-check" scale="3"></b-icon>
        </v-list-item>

        <v-card-actions>
          <v-btn outlined rounded text> Entrar </v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </div>
</template>
<style scoped>
.grid-container {   
    display: grid;
    grid-template-columns: auto auto auto;
    padding: 10px;
    align-content: center;
    transform: translate(10%,150%);
}
.mx-auto{
  color:aqua;
}
</style>
<script>
export default {
  name:'Usuarios',
   beforeMount(){
        if (this.storage.token==''){
          this.$router.push({name:"Login"});
         }
    }
};
</script>
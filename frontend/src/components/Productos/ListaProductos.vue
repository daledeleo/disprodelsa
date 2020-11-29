<template>
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h2>Listado de Productos</h2>
        <div class="col-md-2">
          <b-table striped hover :items="productos" :fileds="fields">
            <template v-slot:cell(actions)="data">
              <b-button size="sm" variant="primary" :to="{ name:'EdicionProducto', params: {productoId: data.item.id} }">
                Editar
              </b-button>
              <b-button size="sm" variant="danger">
                Eliminar
              </b-button>
            </template>
          </b-table>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      fields: [
        { key: "SKU", label: "SKU" },
        { key: "COD_BARRA", label: "COD_BARRA" },
        { key: "IMAGEN_DISPONIBLE", label: "Imagen Disponible" },
        { key: "LABORATORIO", label: "Laboratorio" },
        { key: "VISITADOR", label: "Visitador" },
        { key: "PRODUCTO", label: "Producto" },
        { key: "REGISTRO_SANITARIO", label: "Registro Sanitario" },
        { key: "TIPO_DE_MEDICAMENTO", label: "Tipo de medicamento" },
        { key: "PRINCIPIO_ACTIVO", label: "Principio activo" },
        { key: "ESPECIALIDAD", label: "Especialidad" },
        { key: "GRUPO_O_CLASE", label: "Grupo o clase" },
        { key: "FAMILIA", label: "Familia" },
        {
          key: "REQUIERE_VENTA_CON_RECETA_PRESCRITA_POR_MEDICO",
          label: "Requiere venta con receta prescrita por medico",
        },
        { key: "PROCEDENCIA_PAIS", label: "Procedencia pais" },
        { key: "UBICACIÓN", label: "Ubicación" },
        { key: "clasificacion", label: "Clasificación" },
        { key: "PESO", label: "Peso" },
        { key: "UNIDAD_PESO", label: "Unidad peso" },
        { key: "VOLUMEN", label: "Volumen" },
        { key: "UNIDADES_VOLUMEN", label: "Unidades Volumen" },
        { key: "PRESENTACION", label: "Presentación" },
        { key: "UNIDADES_PRESENTACIÓN", label: "Unidades presentación" },
        { key: "UNIDAD", label: "Unidad" },
        { key: "UNIDADES_POR_EMPAQUE", label: "Unidades por empaque" },
        { key: "PRECIO_1", label: "Precio 1" },
        { key: "PRECIO_2", label: "Precio 2" },
        { key: "PRECIO_3", label: "Precio 3" },
        { key: "PRECIO_DISPRODELSA", label: "Precio DISPRODELSA" },
        { key: "DESCUENTO", label: "Descuento" },
        { key: "PRECIO_INCLUYE_IVA", label: "Precio incluye IVA" },
        { key: "EXISTENCIA_MINIMA", label: "Existencia Minima" },
        { key: "EXISTENCIA_MAXIMA", label: "Existencia Maxima" },
        { key: "PRODUCTO_ACTIVO", label: "Producto Activo" },
        { key: "BAJO_PEDIDO", label: "Bajo Pedido" },
        { key: "DESCRIPCION", label: "Descripción" },
        { key: "REACCIONES_ADVERSAS", label: "Reaccion Adversas" },
        { key: "SOLUCION", label: "Solución" },
        {key:"action",label:"Acción"},
      ],
      productos: [],
    };
  },
  methods: {
    getProductos() {
      const path = "http://localhost:8000/api/productos/";
      axios
        .get(path)
        .then((response) => {
          this.productos = response.data;
        })
        .catch((error) => {
          alert(error);
        });
    },
  },
  created() {
    this.getProductos();
  },
};
</script>
<style scoped lang='css'>
</style>
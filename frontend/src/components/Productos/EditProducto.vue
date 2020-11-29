<template lang="html">
<div class='container'>
    <div class="row">
        <div class="col text-left">
            <h2> Edite la informacion de un Producto</h2>
        </div>
    </div>
    <div class="row">
        <div class="col">
            <div class="card">
                <div class="card-body">
                    <form @onSubmit="onSubmit">
                        <div class="form-group row">
                            <label for="SKU" class="col-sm-2 col-form-label">SKU</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="SKU" name="SKU" class="form-control" v-model.trim="form.SKU">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="COD_BARRA" class="col-sm-2 col-form-label">COD/BARRA</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="COD/BARRA" name="COD_BARRA" class="form-control"v-model.trim="form.COD_BARRA">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="IMAGEN_DISPONIBLE" class="col-sm-2 col-form-label">IMAGEN DISPONIBLE</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="IMAGEN DISPONIBLE" name="IMAGEN_DISPONIBLE" class="form-control" v-model.trim="form.IMAGEN_DISPONIBLE">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="LABORATORIO" class="col-sm-2 col-form-label">Laboratorio</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="LABORATORIO" name="LABORATORIO" class="form-control" v-model.trim="form.LABORATORIO">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="VISITADOR" class="col-sm-2 col-form-label">Visitador</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="VISITADOR" name="VISITADOR" class="form-control" v-model.trim="form.VISITADOR">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="PRODUCTO" class="col-sm-2 col-form-label">Producto</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="PRODUCTO" name="PRODUCTO" class="form-control" v-model.trim="form.PRODUCTO">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="REGISTRO_SANITARIO" class="col-sm-2 col-form-label">Registro Sanitario</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="REGISTRO SANITARIO" name="REGISTRO_SANITARIO" class="form-control" v-model.trim="form.REGISTRO_SANITARIO">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="TIPO_DE_MEDICAMENTO" class="col-sm-2 col-form-label">Tipo de Medicamento</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="TIPO DE MEDICAMENTO" name="TIPO_DE_MEDICAMENTO" class="form-control" v-model.trim="form.TIPO_DE_MEDICAMENTO">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="PRINCIPIO_ACTIVO" class="col-sm-2 col-form-label">Principio Activo</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="PRINCIPIO_ACTIVO" name="PRINCIPIO_ACTIVO" class="form-control" v-model.trim="form.PRINCIPIO_ACTIVO">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="ESPECIALIDAD" class="col-sm-2 col-form-label">Especialidad</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="ESPECIALIDAD" name="ESPECIALIDAD" class="form-control" v-model.trim="form.ESPECIALIDAD">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="GRUPO_O_CLASE" class="col-sm-2 col-form-label">Grupo o Clase</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="GRUPO O CLASE" name="GRUPO_O_CLASE" class="form-control" v-model.trim="form.GRUPO_O_CLASE">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="FAMILIA" class="col-sm-2 col-form-label">Familia</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="Familia" name="FAMILIA" class="form-control" v-model.trim="form.FAMILIA">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="REQUIERE_VENTA_CON_RECETA_PRESCRITA_POR_MEDICO" class="col-sm-2 col-form-label">REQUIERE_VENTA_CON_RECETA_PRESCRITA_POR_MEDICO</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="REQUIERE_VENTA_CON_RECETA_PRESCRITA_POR_MEDICO" name="REQUIERE_VENTA_CON_RECETA_PRESCRITA_POR_MEDICO" class="form-control" v-model.trim="form.REQUIERE_VENTA_CON_RECETA_PRESCRITA_POR_MEDICO">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="PROCEDENCIA_PAIS" class="col-sm-2 col-form-label">Procedencia Pais</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="PROCEDENCIA PAIS" name="PROCEDENCIA_PAIS" class="form-control" v-model.trim="form.PROCEDENCIA_PAIS">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="UBICACIÓN" class="col-sm-2 col-form-label">Ubicación</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="Ubicación" name="UBICACIÓN" class="form-control" v-model.trim="form.UBICACIÓN">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="clasificacion" class="col-sm-2 col-form-label">clasificación</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="clasificacion" name="clasificacion" class="form-control" v-model.trim="form.clasificacion">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="PESO" class="col-sm-2 col-form-label">PESO</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="Peso" name="PESO" class="form-control" v-model.trim="form.PESO">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="UNIDAD_PESO" class="col-sm-2 col-form-label">UNIDAD_PESO</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="UNIDAD_PESO" name="UNIDAD_PESO" class="form-control" v-model.trim="form.UNIDAD_PESO">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="VOLUMEN" class="col-sm-2 col-form-label">VOLUMEN</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="VOLUMEN" name="VOLUMEN" class="form-control" v-model.trim="form.VOLUMEN">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="UNIDADES_VOLUMEN" class="col-sm-2 col-form-label">UNIDADES_VOLUMEN</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="UNIDADES_VOLUMEN" name="UNIDADES_VOLUMEN" class="form-control" v-model.trim="form.UNIDADES_VOLUMEN">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="PRESENTACION" class="col-sm-2 col-form-label">PRESENTACION</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="PRESENTACION" name="PRESENTACION" class="form-control" v-model.trim="form.PRESENTACION">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="UNIDADES_PRESENTACIÓN" class="col-sm-2 col-form-label">UNIDADES_PRESENTACIÓN</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="UNIDADES_PRESENTACIÓN" name="UNIDADES_PRESENTACIÓN" class="form-control" v-model.trim="form.UNIDADES_PRESENTACIÓN">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="UNIDAD" class="col-sm-2 col-form-label">UNIDAD</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="UNIDAD" name="UNIDAD" class="form-control" v-model.trim="form.UNIDAD">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="UNIDADES_POR_EMPAQUE" class="col-sm-2 col-form-label">UNIDADES_POR_EMPAQUE</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="UNIDADES_POR_EMPAQUE" name="UNIDADES_POR_EMPAQUE" class="form-control" v-model.trim="form.UNIDADES_POR_EMPAQUE">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="PRECIO_1" class="col-sm-2 col-form-label">PRECIO_1</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="PRECIO_1" name="PRECIO_1" class="form-control" v-model.trim="form.PRECIO_1">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="PRECIO_2" class="col-sm-2 col-form-label">PRECIO_2</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="PRECIO_2" name="PRECIO_2" class="form-control" v-model.trim="form.PRECIO_2">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="PRECIO_3" class="col-sm-2 col-form-label">PRECIO_3</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="PRECIO_3" name="PRECIO_3" class="form-control" v-model.trim="form.PRECIO_3">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="PRECIO_DISPRODELSA" class="col-sm-2 col-form-label">PRECIO_DISPRODELSA</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="PRECIO_DISPRODELSA" name="PRECIO_DISPRODELSA" class="form-control" v-model.trim="form.PRECIO_DISPRODELSA">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="DESCUENTO" class="col-sm-2 col-form-label">DESCUENTO</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="DESCUENTO" name="DESCUENTO" class="form-control" v-model.trim="form.DESCUENTO">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="PRECIO_INCLUYE_IVA" class="col-sm-2 col-form-label">PRECIO_INCLUYE_IVA</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="PRECIO_INCLUYE_IVA" name="PRECIO_INCLUYE_IVA" class="form-control" v-model.trim="form.PRECIO_INCLUYE_IVA">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="EXISTENCIA_MINIMA" class="col-sm-2 col-form-label">EXISTENCIA_MINIMA</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="EXISTENCIA_MINIMA" name="EXISTENCIA_MINIMA" class="form-control" v-model.trim="form.EXISTENCIA_MINIMA">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="EXISTENCIA_MAXIMA" class="col-sm-2 col-form-label">EXISTENCIA_MAXIMA</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="EXISTENCIA_MAXIMA" name="EXISTENCIA_MAXIMA" class="form-control" v-model.trim="form.EXISTENCIA_MAXIMA">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="PRODUCTO_ACTIVO" class="col-sm-2 col-form-label">PRODUCTO_ACTIVO</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="PRODUCTO_ACTIVO" name="PRODUCTO_ACTIVO" class="form-control" v-model.trim="form.PRODUCTO_ACTIVO">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="BAJO_PEDIDO" class="col-sm-2 col-form-label">BAJO_PEDIDO</label>
                            <div class="col-sm-6">
                                <input type="text" placeholder="BAJO_PEDIDO" name="BAJO_PEDIDO" class="form-control" v-model.trim="form.BAJO_PEDIDO">
                            </div>
                        </div>

                         <div class="form-group row">
                            <label for="DESCRIPCION" class="col-sm-2 col-form-label">Descripción</label>
                            <div class="col-sm-6">
                                <textarea name="DESCRIPCION" class="form-control" placeholder='Descripción' rows='3' v-model.trim="form.DESCRIPCION"></textarea>
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="REACCIONES_ADVERSAS" class="col-sm-2 col-form-label">REACCIONES_ADVERSAS</label>
                            <div class="col-sm-6">
                                <textarea name="REACCIONES_ADVERSAS" class="form-control" placeholder='REACCIONES_ADVERSAS' rows='3' v-model.trim="form.REACCIONES_ADVERSAS"></textarea>
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="SOLUCION" class="col-sm-2 col-form-label">Solucion</label>
                            <div class="col-sm-6">
                                <textarea name="SOLUCION" class="form-control" placeholder='Solucion' rows='3' v-model.trim="form.SOLUCION"></textarea>
                            </div>
                        </div>

                        <div class="rows">
                            <div class="col text-left">
                                <b-button type='submit' variant='primary'>Editar</b-button>
                                <b-button type='submit' class="btn-large-space" :to="{name: 'ListaProductos'}">Cancelar</b-button>
                            </div>
                        </div>

                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
    
</template>
<script>
import axios from "axios"

export default {
    data(){
        return{
            productoId:this.$route.params.productoId,
            form:{
                SKU:'',
                COD_BARRA:'',
                IMAGEN_DISPONIBLE:'',
                LABORATORIO :'',
                VISITADOR :'',
                PRODUCTO:'',
                REGISTRO_SANITARIO:'',
                TIPO_DE_MEDICAMENTO:'',
                PRINCIPIO_ACTIVO:'',
                ESPECIALIDAD:'',
                GRUPO_O_CLASE:'',
                FAMILIA:'',
                REQUIERE_VENTA_CON_RECETA_PRESCRITA_POR_MEDICO :'',
                PROCEDENCIA_PAIS :'',
                UBICACIÓN:'',
                clasificacion:'',
                PESO :'',
                UNIDAD_PESO:'',
                VOLUMEN:'',
                UNIDADES_VOLUMEN:'',
                PRESENTACION:'',
                UNIDADES_PRESENTACIÓN:'',
                UNIDAD:'',
                UNIDADES_POR_EMPAQUE :'',
                PRECIO_1:'',
                PRECIO_2:'',
                PRECIO_3:'',
                PRECIO_DISPRODELSA:'',
                DESCUENTO:'',
                PRECIO_INCLUYE_IVA:'',
                EXISTENCIA_MINIMA:'',
                EXISTENCIA_MAXIMA:'',
                PRODUCTO_ACTIVO:'',
                BAJO_PEDIDO:'',
                DESCRIPCION :'',
                REACCIONES_ADVERSAS:'',
                SOLUCION:'',
            }
        }
    },
    methods:{
        onSubmit(evt){
            evt.preventDefault()
        },
        getProducto(){
            const path=`http://localhost:8000/api/productos/${this.productoId}`
            axios.get(path).then((response)=>{
                this.form=response.data
                }
            ).catch((error)=>{
                alert(error)
            })
        }
    },
    created(){
        this.getProducto();
    }
};
</script>
<style lang="css" scoped>
</style>
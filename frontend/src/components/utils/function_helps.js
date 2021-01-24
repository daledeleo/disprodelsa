export default {
    name:'Inicio',
    methods:{
       getTypeuser(i){
        if(i=='1'){
            return "Administrador"
        }else if(i=='2'){
            return 'Quimico Sr'
        }else{
            return 'Quimico Jr'
        }
       }
    }
 
}
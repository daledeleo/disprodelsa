<template>
    <p>
        Saliendo de la cuenta.......
    </p>
</template>

<script>
export default {
    name:'Logout',
    created() {
        localStorage.clear()
        this.$router.push({name:"Login"});
    }
}
</script>
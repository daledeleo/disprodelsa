<template>
    <p>
    </p>
</template>

<script>
export default {
    created() {
        this.storage.token = "";
        this.storage.loggedInUser = {};
        this.storage.otherUserPk = 0;
        this.storage.email='';
        this.storage.username='';
        this.storage.type_user='';
        this.$router.replace("/");
    }
}
</script>
<template>
    <div class="nav">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/AddArticle/">Dodaj post</RouterLink>
    </div>
</template>

<script>
export default {
    name: 'NavComponent',
}
</script>

<style scoped>
.nav {}
</style>
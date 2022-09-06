<template>
    <div class="addarticle">
        dodawanie artykulu
    </div>

    <form>
        <label>Tytuł:</label>
        <input type="text">
        <label>Treść:</label>
        <input type="text">

    </form>
</template>

<script>
export default {
    name: 'AddArticleComponent',

    //alert("Mój artykuł: " + article.value.title+ ", " + article.value.content );

}
</script>

<style scoped>
.home {}
</style>
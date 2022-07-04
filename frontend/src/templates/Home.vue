<template>
    <div class="home">
        <div v-for="article in articles" :key="article.id">
            <div>{{ article.title }}</div>
            <div>{{ article.text }}</div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'HomeComponent',
    setup() {
        const articles = [
            {
                id: 1,
                title: 'Art1',
                text: 'Lorem ipsum 1'
            },
            {
                id: 2,
                title: 'Art2',
                text: 'Lorem ipsum 2'
            },
            {
                id: 3,
                title: 'Art3',
                text: 'Lorem ipsum 3'
            },
        ]

        return { articles }
    }
}
</script>

<style scoped>
.home {}
</style>
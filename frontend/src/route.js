import { createRouter, createWebHistory } from 'vue-router';

import HomeComponent from "./templates/Home.vue"
import AddArticle from "./templates/AddArticle.vue"

const routes = [
    {
        path:"/",
        name:"home",
        component:HomeComponent

    },

    {
        path:"/addarticle/",
        name:"AddArticle",
        component:AddArticleComponent
    },


]

const router = createRouter({ history: createWebHistory('/'), routes})

export default router
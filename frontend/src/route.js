import { createRouter, createWebHistory } from 'vue-router';

import HomeComponent from "./templates/Home.vue"
import DupkaComponent from "./templates/Dupka.vue"

const routes = [
    {
        path:"/",
        name:"home",
        component:HomeComponent

    },

    {
        path:"/dupka/",
        name:"Dupka",
        component:DupkaComponent
    },
]

const router = createRouter({ history: createWebHistory('/'), routes})

export default router
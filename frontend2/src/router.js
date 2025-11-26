import {createRouter,createWebHistory} from 'vue-router'
import Login from './Login.vue'
import Users from './Users.vue'
import Articles from './Articles.vue'

const routes =[
    {path:'/',redirect:'/login'},
    {path:'/login',component:Login},
    {path:'/users',component:Users},
    {path:'/articles',component:Articles}
]

export default createRouter({history:createWebHistory(),routes})
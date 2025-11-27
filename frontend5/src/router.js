import {createRouter, createWebHashHistory} from 'vue-router'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('./Home.vue')
  }
]

export default createRouter({
  history: createWebHashHistory(),
  routes
})

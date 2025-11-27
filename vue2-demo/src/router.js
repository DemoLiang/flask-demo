// 由于使用全局引入的Vue Router，我们直接使用全局变量

// 创建路由实例
const router = VueRouter.createRouter({
  // 使用hash模式
  history: VueRouter.createWebHashHistory(),
  // 定义路由
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('./components/HelloWorld.vue')
    }
  ]
})

export default router
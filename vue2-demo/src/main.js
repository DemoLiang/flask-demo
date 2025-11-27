// 由于使用CDN引入，Vue已经作为全局变量可用
// 但为了保持代码结构，我们仍然保留import
import Vue from 'vue'
import App from './App.vue'
import router from './router'

// 使用通过CDN引入的Vue Router
Vue.use(VueRouter)

// 使用通过CDN引入的Element Plus
// 注意：Element Plus主要为Vue 3设计，但这里使用的是Vue 2兼容版本
Vue.use(ElementPlus)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')

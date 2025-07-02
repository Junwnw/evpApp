import { createRouter, createWebHashHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Home from '../views/Home.vue'
import Welcome from '../views/Welcome.vue'
import Crawler from '../views/Crawler.vue'
const routes = [
    { path: '/', redirect: '/login' },
    { path: '/login', component: Login },
    {
      path: '/home',
      component: Home,
      children: [
        { path: '', component: Welcome },           // ✅ 默认展示欢迎页
        { path: 'crawler', component: Crawler } // ✅ 爬虫页面
      ]
    }
  ]
  
  const router = createRouter({
    history: createWebHashHistory(),
    routes
  })
  
  export default router
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css' //element plus 的默认样式引入：
import './assets/global.css' //引入全局样式，统一设置所有页面通用的CSS样式，比如字体，背景色和页面边距等等
createApp(App).use(router).use(ElementPlus).mount('#app')

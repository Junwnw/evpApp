<template>
    <el-aside :width="isCollapse ? '64px' : '200px'" class="sidebar">
      <el-menu
        :default-active="activeIndex"
        class="el-menu-vertical-demo"
        :collapse="isCollapse"
        background-color="#2d3a4b"
        text-color="#fff"
        active-text-color="#ffd04b"
      >
        <el-menu-item index="1" @click="goTo('')">
          <el-icon><HomeFilled /></el-icon>
          <template #title>首页</template>
        </el-menu-item>
  
        <el-sub-menu index="2">
          <template #title>
            <el-icon><Setting /></el-icon>
            <span>工具模块</span>
          </template>
          <el-menu-item index="2-1" @click="goTo('crawler')">爬虫工具</el-menu-item>
          <el-menu-item index="2-2" @click="goTo('analyzer')">分析工具</el-menu-item>  
            <!-- 可扩展工具模块children列 -->
        </el-sub-menu>
  
        <el-menu-item index="3" @click="goTo('settings')">
          <el-icon><Tools /></el-icon>
          <template #title>设置</template>
        </el-menu-item>

        
      </el-menu>
  
      <!-- 折叠按钮 -->
      <div class="collapse-btn" @click="isCollapse = !isCollapse">
        <el-icon>
          <component :is="isCollapse ? Expand : Fold" />
        </el-icon>
      </div>
    </el-aside>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import {
    HomeFilled,
    Setting,
    Tools,
    Fold,
    Expand,
  } from '@element-plus/icons-vue'
  
  const isCollapse = ref(false)
  const activeIndex = ref('1')
  const router = useRouter()
  
  const goTo = (path) => {
    router.push('/home/' + path)
  }
  </script>
  
  <style scoped>
  .sidebar {
    background-color: #5175a3;
    color: rgb(126, 43, 185);
    position: relative;
    height: 100vh;
    transition: width 0.3s ease; /* 添加平滑过渡动画 */
    overflow: hidden; /* 防止子元素超出时抖动 */
  }
  .collapse-btn {
    position: absolute;
    bottom: 10px;
    left: 0;
    right: 0;
    text-align: center;
    cursor: pointer;
    color: #fff;
    font-size: 20px;
    
  }
  /* 修改 el-menu 背景色 */
    ::v-deep(.el-menu-vertical-demo) {
    background-color: #486077;
    color: #0c0101;
    border: none;
    }

    /* 修改菜单激活项颜色 */
    ::v-deep(.el-menu-vertical-demo .el-menu-item.is-active) {
    background-color: #1f2d3d;
    color: #ffd04b;
    }
  </style>
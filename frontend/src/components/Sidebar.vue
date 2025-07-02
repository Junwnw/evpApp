<template>
    <el-aside width="200px" style="background: #2d3a4b; color: white;">
      <el-menu default-active="1" background-color="#2d3a4b" text-color="#fff">
        <el-menu-item index="1" @click="goTo('')">🏠 首页</el-menu-item>
        <el-menu-item index="2" @click="goTo('crawler')">🕷️ 爬虫工具</el-menu-item>
      </el-menu>
    </el-aside>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router'
  const router = useRouter()
  const goTo = (path) => {
    router.push('/home/' + path)
  }
  </script>
  
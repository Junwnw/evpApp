<template>
    <el-container style="height: 100vh;">
      <Sidebar />
      <el-container>
        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </template>
  
  <script setup>
  import Sidebar from '../components/Sidebar.vue'
  </script>
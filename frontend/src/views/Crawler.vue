<template>
    <el-card class="box-card" style="max-width: 600px; margin: 30px auto;">
      <h2 style="text-align: center;">🔥 微博热搜爬取</h2>
      <el-input
        v-model="keyword"
        placeholder="请输入关键词（留空查看热搜）"
        clearable
        style="margin-bottom: 20px"
      />
      <el-button type="primary" @click="search" :loading="loading">搜索</el-button>
  
      <el-divider>结果</el-divider>
      <el-empty v-if="results.length === 0 && !loading" description="暂无结果" />
      <el-list v-else>
        <el-list-item v-for="item in results" :key="item.title">
          <span>{{ item.title }}</span>
        </el-list-item>
      </el-list>
    </el-card>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { crawlAPI } from '../api/crawler.js'
  
  const keyword = ref('')
  const results = ref([])
  const loading = ref(false)
  
  const search = async () => {
    loading.value = true
    try {
      results.value = await crawlAPI(keyword.value)
    } catch (err) {
      console.error('爬虫请求失败:', err)
    }
    loading.value = false
  }
  </script>
  
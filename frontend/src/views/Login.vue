<template>
    <el-card style="width: 400px; margin: 100px auto;">
      <h3 style="text-align: center;">🔐 登录系统</h3>
      <el-form>
        <el-form-item>
          <el-input v-model="username" placeholder="用户名" />
        </el-form-item>
        <el-form-item>
          <el-input v-model="password" placeholder="密码" type="password" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleLogin" style="width: 100%;">登录</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  
  const username = ref('')
  const password = ref('')
  const router = useRouter()
  
  const handleLogin = () => {
    if (username.value && password.value) {
      router.push('/home')
    } else {
      alert('请输入用户名和密码')
    }
  }
  </script>
  <style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: #f2f2f2;
}
.login-card {
  width: 400px;
  padding: 20px;
}
</style>
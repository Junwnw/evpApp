<template>
    <div class="login-container">
      <!-- 左侧背景 + LOGO -->
      <div class="left-panel">
        <img src="@/assets/logo.png" class="main-logo" />
      </div>
  
      <!-- 右侧登录表单 -->
      <div class="right-panel">
        <div class="login-card">
          <h2 class="login-title">技术人员登录系统</h2>
          <el-form @submit.prevent>
            <el-form-item>
              <el-input
                v-model="username"
                placeholder="用户名"
                prefix-icon="el-icon-user"
                clearable
              />
            </el-form-item>
            <el-form-item>
              <el-input
                v-model="password"
                type="password"
                placeholder="密码"
                prefix-icon="el-icon-lock"
                show-password
                clearable
              />
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="handleLogin" class="login-btn">
                LOGIN
              </el-button>
            </el-form-item>
          </el-form>
        </div>
      </div>
    </div>
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
      ElMessage.error('请输入用户名和密码')
    }
  }
  </script>
  
  <style scoped>
  .login-container {
    display: flex;
    height: 100vh;
    overflow: hidden;
  }
  
  /* 黄金比例：左 61.8% */
  .left-panel {
    flex: 618;
    background: linear-gradient(135deg, #f6f7f8, #aac9f0);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .main-logo {
    height: 1000px;
  }
  
  /* 黄金比例：右 38.2%，加左阴影 */
  .right-panel {
    flex: 382;
    background: #f8f8f8;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: -10px 0 20px rgba(0, 0, 0, 0.08);
  }
  
  /* 登录卡片 */
  .login-card {
    background-color: white;
    padding: 200px 50px;
    border-radius: 12px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 360px;
  }
  
  .login-title {
    text-align: center;
    margin-bottom: 20px;
    color: #4a92da;
    font-weight: 600;
  }
  
  .login-btn {
  width: 50%;
  height: 48px; 
  background-color: #dd6464;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 700;
  transition: all 0.3s ease;
  cursor: pointer;
  margin: 0 auto; /* ✅ 水平居中 */
  display: block; /* ✅ 让 margin 生效 */
}

.login-btn:hover {
  background-color: white;
  color: #000000;
  box-shadow: 0 0 8px rgba(45, 58, 75, 0.2);
}
  </style>
  
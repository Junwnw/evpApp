<template>
    <div class="welcome-container">
      <h1>欢迎来到我的网站</h1>
      <el-input v-model="name" placeholder="请输入你的名字" class="input-box" />
  
      <el-button type="primary" @click="sayHi" class="btn"> 
        点击欢迎我
      </el-button>
  
      <p v-if="greeting" class="greeting">{{ greeting }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data () {
      return {
        name: '',
        greeting: ''
      }
    },
    methods: {
      sayHi () {
        if (this.name.trim()) {
          this.greeting = `你好，${this.name}！欢迎来到这里 😊`;
        } else {
          this.greeting = '请先输入你的名字哦~';
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .welcome-container {
    max-width: 400px;
    margin: 100px auto;
    text-align: center;
    padding: 30px;
    border: 1px solid #eee;
    border-radius: 12px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
    background-color: #fff;
  }
  
  .input-box {
    margin: 20px 0;
  }
  
  .btn {
    margin-bottom: 20px;
  }
  
  .greeting {
    font-size: 18px;
    color: #409EFF;
    font-weight: bold;
  }
  </style>
<script setup>
import {ref} from 'vue'
import {login} from './api'
import {ElMessage}from 'element-plus'
import router from './router'
const username = ref('')
const password = ref('')

async function submit(){
 const res =  await login(username.value,password.value)
  console.log('res',res)
  if (res.id!==null){
    localStorage.setItem('token',res.token)
    localStorage.setItem('username',res.username)
    ElMessage.info("登录成功")
    await router.push('/users')
  }else{
    ElMessage.info("登录失败")
  }
}

</script>

<template>
  <div>
    <h2 style="margin-bottom:16px;">登录</h2>
    <div style="display:flex; flex-direction:column; gap:12px; max-width:420px;">
      <el-input v-model="username" placeholder="用户名" />
      <el-input v-model="password" type="password" placeholder="密码" />
      <el-button type="primary" :disabled="!username || !password " @click="submit">登录</el-button>
    </div>
  </div>
</template>

<style scoped>

</style>
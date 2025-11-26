<script setup>

import {ref} from 'vue'
import { ElMessage } from 'element-plus'
import {login} from './api'
import {useRouter} from 'vue-router'


const username = ref('')
const password = ref('')
const loading = ref(false)
const router = useRouter()

async function submit(){
  if (!username.value||!password.value)
      return
  loading.value =true
  try{
    await login(username.value,password.value)
    console.log('login',username.value,password.value)
    localStorage.setItem('username',username.value)
    ElMessage.success('登录成功')
    router.push('/users')
  }catch (e){
    console.log('e',e)
    ElMessage.error(e.message)
  }finally {
    loading.value = false
  }
}

</script>

<template>
<div>
  <h2 style="margin-bottom: 16px">登录</h2>
  <div>
    <el-input v-model="username" placeholder="用户名" />
    <el-input v-model="password" type="password" placeholder="密码"></el-input>
    <el-button type="primary" :disabled=!username||!password||loading @click="submit">登录</el-button>
  </div>
</div>
</template>

<style scoped>

</style>

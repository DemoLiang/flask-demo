<script setup lang="ts">
import {ref}from 'vue'
import {login} from './api.js'
import {ElMessage} from 'element-plus'
import {useRouter} from 'vue-router'

const username=ref('')
const password=ref('')
const router = useRouter()

const submit=()=>{
  console.log(username.value,password.value)
  login(username.value,password.value).then((res)=>{
    if (res.status===200){
      console.log(res)
      ElMessage.info("登录成功")
      router.push('/users')
    }else{
      ElMessage.error(res.error)
      router.push('/users')
    }
  }).catch((err)=>{
    console.log(err)
    ElMessage.error("登录失败")
  })
}

</script>


<template>

  <h2 style="margin-bottom: 16px">登录</h2>
  <div style="display: flex;flex-direction:column;gap:16px;max-width:420px">
    <el-input v-model="username" placeholder="请输入用户名"></el-input>
    <el-input v-model="password" placeholder="请输入密码"></el-input>
    <el-button type="primary" @click="submit">登录</el-button>
  </div>

</template>

<style scoped>

</style>
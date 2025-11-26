<script setup>
import {ref} from 'vue'
import {login} from './api'
import {useRouter} from 'vue-router'
import {ElMessage} from 'element-plus'

const username = ref('')
const password = ref('')
const router = useRouter()

async function submit(){
  if (!username||!password)
    return
  try{
    console.log('usernmae:',username.value,password.value)
    const res = await login(username.value,password.value)
    if (res){
      localStorage.setItem("token",res.token)
      localStorage.setItem("username",res.username)
      router.push('/users')
    }
    ElMessage.success("登陆成功")
  }catch(e){
    console.log(e)
    ElMessage.error("登陆失败")
  }
}


</script>

<template>
<div style="display: flex;gap: 16px;flex-direction: column">
  <div>
    <h2 style="margin-bottom: 16px">用户登陆</h2>
  </div>
  <div style="display: flex;gap:12px;flex-direction: column;width: 400px;">
    <el-input v-model="username" placeholder="请输入用户名"></el-input>
    <el-input v-model="password" placeholder="请输入密码" type="password"></el-input>
    <el-button type="primary" @click="submit" :disabled="!username || !password">登陆</el-button>
  </div>

</div>
</template>

<style scoped>

</style>
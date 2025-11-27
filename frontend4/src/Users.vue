<script setup>

import {ref,onMounted}from 'vue'
import {fetchUsers,createUser}from './api.js'
import {ElMessage} from 'element-plus'

const users=ref([])

const showCreate = ref(false)
const addUserName = ref('')
const addUserPassw = ref('')

async function loadUsers(){
  const res = await fetchUsers()
  users.value = res
}

async function addUser(){
  const res = await createUser(addUserName.value,addUserPassw.value)
  if (!res){
    ElMessage.error("添加用户失败")
  }
  if (res.success ){
    ElMessage.success("添加用户成功")
    showCreate.value=false
    await loadUsers()
  }
}

onMounted(loadUsers)
</script>

<template>

  <div style="flex-direction: column;display: flex;width: 900px">
    <div>
      <el-button @click="loadUsers">刷新</el-button>
          <el-button @click="showCreate=true">添加用户</el-button>
    </div>
    <div>
          <el-table :data="users">
            <el-table-column prop="id" label="ID"></el-table-column>
            <el-table-column prop="name" label="用户名"></el-table-column>
          </el-table>
    </div>


    <el-dialog v-model="showCreate">
    <el-input v-model="addUserName" placeholder="用户名名"></el-input>
    <el-input v-model="addUserPassw" placeholder="用户密码"></el-input>
    <template #footer>
      <el-button @click="addUser">添加用户</el-button>
    </template>
  </el-dialog>

  </div>

</template>

<style scoped>

</style>
<script setup >
import {ref,onMounted} from 'vue'
import {fetchUsers} from './api'

const loading = ref(false)
const users = ref([])

async function loadUsers(){
  loading.value = true
  const res = await fetchUsers()
  if (res!=={}){
    users.value = res
  }
  loading.value = false
}

onMounted(loadUsers)
</script>

<template>

  <div>
    <h2 style="margin-bottom: 16px;">用户列表</h2>
    <div style="display: flex;gap: 12px;margin-bottom: 16px">
      <el-button :disabled="loading" @click="loadUsers">刷新</el-button>
    </div>
    <el-table :data="users" border style="width: 100%">
      <el-table-column prop="id" label="ID"/>
      <el-table-column prop="name" label="用户名"/>
    </el-table>
  </div>
</template>

<style scoped>

</style>
<script setup>
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import { fetchUsers } from './api'

const users = ref([])
const loading = ref(false)

async function loadUsers() {
  loading.value = true
  try {
    users.value = await fetchUsers()
  } catch (e) {
    ElMessage.error(String(e.message || e))
  } finally {
    loading.value = false
  }
}

onMounted(loadUsers)
</script>

<template>
  <div>
    <h2 style="margin-bottom:16px;">用户列表</h2>
    <div style="display:flex; gap:12px; margin-bottom:16px;">
      <el-button :disabled="loading" @click="loadUsers">刷新</el-button>
    </div>
    <el-table :data="users" border style="width:100%;">
      <el-table-column prop="id" label="ID" width="120" />
      <el-table-column prop="name" label="用户名" />
    </el-table>
  </div>
  </template>

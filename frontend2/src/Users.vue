<script setup>

import {ref,onMounted} from 'vue'
import {fetchUsers} from "./api";

const users = ref([])

async function loadUsers(){
  const res = await fetchUsers()
  users.value= res
}


onMounted(loadUsers)
</script>

<template>
  <div>
    <h2 style="display: flex;gap:12px;margin-bottom: 12px">用户列表</h2>
    <div style="display: flex;gap: 12px;margin-bottom: 12px;" >
      <el-button @click="loadUsers">刷新</el-button>
    </div>

    <el-table :data="users" border style="display: flex;width: 100%">
      <el-table-column prop="id" label="ID" width="120px"></el-table-column>
      <el-table-column prop="name" label="用户名"></el-table-column>
    </el-table>
  </div>
</template>

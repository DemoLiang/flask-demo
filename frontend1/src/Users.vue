<script setup>
import {ref,onMounted } from 'vue'
import {fetchUsers} from "./api.js";


const users = ref({})
const loading = ref(false)

async function loadUsers(){
  loading.value = true

  users.value = await fetchUsers()
  loading.value = false
}

onMounted(loadUsers)

</script>

<template>
<div>
  <el-button :disable="loading" @click="loadUsers">刷新</el-button>
  <el-table :data="users" border>
    <el-table-column prop="id" lable="ID"></el-table-column>
    <el-table-column prop="name" lable="用户名"></el-table-column>
  </el-table>
</div>

</template>

<style scoped>

</style>
<script setup>
import {ref,onMounted}from 'vue'
import {fetchArticles}from './api.js'

const articles=ref([])
const showCreate = ref(false)

async function loadArticles(){
  const res = await fetchArticles()
  articles.value = res
}

onMounted(loadArticles)
</script>

<template>
  <div>
    <div style="display: flex;margin-bottom: 12px;gap: 12px;">
      <el-button type="primary" @click="showCreate=true">新增文章</el-button>
      <el-button @click="loadArticles">刷新</el-button>
    </div>
    <el-table :data="articles" border style="width: 100%">
      <el-table-column prop="id" label="ID" width="80"/>
      <el-table-column prop="title" label="标题"/>
      <el-table-column prop="author_name" label="作者" width="160"/>
      <el-table-column prop="created_at" label="创建时间" width="220"/>
      <el-table-column prop="content" label="内容"/>
    </el-table>
  </div>
</template>



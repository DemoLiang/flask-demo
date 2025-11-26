<script setup >

import {ref,onMounted} from 'vue'
import {fetchArticles,createArticle} from './api.js'
import {ElMessage} from 'element-plus'

// 创建文章
const articles=ref([])
const loading=ref(false)
const showCreate=ref(false)
const newTitle=ref('')
const newContent=ref('')


//编辑文章
const showEdit=ref(false)
const editId=ref(null)
const editTitle=ref('')
const editContent=ref('')

// 评论
const showComment=ref(false)
const comments=ref([])
const commentsLoading=ref(false)
const commentTxt=ref('')
const currentArticle=ref('')

async function loadArticles(){
  loading.value=true
  const res = await fetchArticles()
  if (res!=={}){
    articles.value=res
  }
  loading.value= false
}

function currentUsername(){
  return localStorage.getItem('username')
}


async function submitCreate(){
  if (!newTitle.value||!newContent.value)
      return
  try {
    await createArticle(newTitle.value, newContent.value, currentUsername())
    newTitle.value = ''
    newContent.value = ''
    await loadArticles()
    ElMessage.success('创建成功')
    showCreate.value=false
  }catch(e){
    ElMessage.error(String(e.message || e))
  }
}

onMounted(loadArticles)
</script>

<template>
<div>
  <div style="display: flex;gap:12px;margin-bottom: 16px;">
    <el-button type="primary" @click="showCreate = true">创建文章</el-button>
    <el-button :disabled="loading" @click="loadArticles">刷新</el-button>
  </div>
  <el-table :data="articles" border style="width:100%">
    <el-table-column prop="id" label="ID" width="80px"></el-table-column>
    <el-table-column prop="title" label="标题" width="120px"></el-table-column>
    <el-table-column prop="content" label="内容" width="300px"></el-table-column>
    <el-table-column prop="author_name" label="作者" width="60px"></el-table-column>
    <el-table-column prop="created_at" label="创建时间" width-="60px"></el-table-column>
    <el-table-column label="操作">
      <template #default="{row}">
        <el-button size="small" @click="openEdit(row)">编辑</el-button>
        <el-button size="small" type="danger" @click="removeArticle(row)">删除</el-button>
        <el-button size="small" type="success" @click="openComent(row)">评论</el-button>
      </template>
    </el-table-column>
  </el-table>

  <!-- 创建文章-->
  <el-dialog v-model="showCreate" title="创建文章" width="600px">
    <div style="display: flex;flex-direction: column;gap: 12px">
      <el-input v-model="newTitle" placeholder="请输入标题"></el-input>
      <el-input v-model="newContent" placeholder="请输入内容"></el-input>
    </div>
    <template #footer>
      <el-button @click="showCreate= false">取消</el-button>
      <el-button type="primary" @click="submitCreate">创建</el-button>
    </template>
  </el-dialog>

  <!-- 编辑文章 -->
  <el-dialog v-model="showEdit" title="编辑文章" width="600px">
    <div style="display: flex;flex-direction: column;gap: 12px;">
      <el-input v-model="editTitle" placeholder="标题"></el-input>
      <el-input v-model="editContent" placeholder="内容"></el-input>
    </div>
    <template #footer>
      <el-button @click="showEdit=false">取消</el-button>
      <el-button type="primary" @click="submitEdit">保存</el-button>
    </template>
  </el-dialog>

  <!-- 评论文章-->
  <el-dialog v-model="showComment" :title="currentArticle?('评论-'+currentArticle.title):'评论'" style="width: 700px">
    <div>
      <div style="display: flex;gap:12px;margin-bottom: 12px">
        <el-input v-model="commentTxt" placeholder="请输入评论"></el-input>
        <el-button type="primary" :disabled="!commentTxt||commentsLoading" @click="submitComment">发表评论</el-button>
      </div>
      <el-table :data="comments" border>
        <el-table-column prop="id" label="ID" width="60px"></el-table-column>
        <el-table-column prop="author" label="作者"></el-table-column>
        <el-table-column prop="content" label="内容"></el-table-column>
        <el-table-column prop="created_at" label="创建时间"></el-table-column>
        <el-table-column lable="操作">
          <template #default="{row}">
            <el-button size="small" type="danger" @click="removeComment(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </el-dialog>
</div>
</template>

<style scoped>

</style>
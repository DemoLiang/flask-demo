<script setup>
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import { fetchArticles, createArticle, updateArticle, deleteArticle, fetchArticleComments, addComment, deleteComment } from './api'

const articles = ref([])
const loading = ref(false)
const showCreate = ref(false)
const newTitle = ref('')
const newContent = ref('')

const showEdit = ref(false)
const editId = ref(null)
const editTitle = ref('')
const editContent = ref('')

const showComments = ref(false)
const comments = ref([])
const commentsLoading = ref(false)
const commentText = ref('')
const currentArticle = ref(null)

function currentUsername() {
  return localStorage.getItem('username') || ''
}

async function loadArticles() {
  loading.value = true
  try {
    articles.value = await fetchArticles()
  } catch (e) {
    ElMessage.error(String(e.message || e))
  } finally {
    loading.value = false
  }
}

async function submitCreate() {
  if (!newTitle.value || !newContent.value) return
  try {
    await createArticle(newTitle.value, newContent.value, currentUsername())
    newTitle.value = ''
    newContent.value = ''
    showCreate.value = false
    await loadArticles()
    ElMessage.success('创建成功')
  } catch (e) {
    ElMessage.error(String(e.message || e))
  }
}

function openEdit(a) {
  editId.value = a.id
  editTitle.value = a.title
  editContent.value = a.content
  showEdit.value = true
}

async function submitEdit() {
  if (!editId.value) return
  try {
    await updateArticle(editId.value, editTitle.value, editContent.value)
    showEdit.value = false
    await loadArticles()
    ElMessage.success('修改成功')
  } catch (e) {
    ElMessage.error(String(e.message || e))
  }
}

async function removeArticle(a) {
  try {
    await deleteArticle(a.id)
    await loadArticles()
    ElMessage.success('删除成功')
  } catch (e) {
    ElMessage.error(String(e.message || e))
  }
}

async function openComments(a) {
  currentArticle.value = a
  commentsLoading.value = true
  showComments.value = true
  try {
    comments.value = await fetchArticleComments(a.id)
  } catch (e) {
    ElMessage.error(String(e.message || e))
  } finally {
    commentsLoading.value = false
  }
}

async function submitComment() {
  if (!currentArticle.value || !commentText.value) return
  try {
    await addComment(currentArticle.value.id, commentText.value, currentUsername())
    commentText.value = ''
    comments.value = await fetchArticleComments(currentArticle.value.id)
    ElMessage.success('评论成功')
  } catch (e) {
    ElMessage.error(String(e.message || e))
  }
}

async function removeComment(c) {
  try {
    await deleteComment(c.id)
    comments.value = await fetchArticleComments(currentArticle.value.id)
    ElMessage.success('删除评论成功')
  } catch (e) {
    ElMessage.error(String(e.message || e))
  }
}

onMounted(loadArticles)
</script>

<template>
  <div>
    <div style="display:flex; gap:12px; margin-bottom:16px;">
      <el-button type="primary" @click="showCreate = true">新增文章</el-button>
      <el-button :disabled="loading" @click="loadArticles">刷新</el-button>
    </div>
    <el-table :data="articles" border style="width:100%;">
      <el-table-column prop="id" label="ID" width="80" />
      <el-table-column prop="title" label="标题" />
      <el-table-column prop="author_name" label="作者" width="160" />
      <el-table-column prop="created_at" label="创建时间" width="220" />
      <el-table-column label="操作" width="280">
        <template #default="{ row }">
          <el-button size="small" @click="openEdit(row)">编辑</el-button>
          <el-button size="small" type="danger" @click="removeArticle(row)">删除</el-button>
          <el-button size="small" type="success" @click="openComments(row)">评论</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog v-model="showCreate" title="新增文章" width="600px">
      <div style="display:flex; flex-direction:column; gap:12px;">
        <el-input v-model="newTitle" placeholder="标题" />
        <el-input v-model="newContent" type="textarea" rows="6" placeholder="内容" />
      </div>
      <template #footer>
        <el-button @click="showCreate = false">取消</el-button>
        <el-button type="primary" @click="submitCreate">保存</el-button>
      </template>
    </el-dialog>

    <el-dialog v-model="showEdit" title="编辑文章" width="600px">
      <div style="display:flex; flex-direction:column; gap:12px;">
        <el-input v-model="editTitle" placeholder="标题" />
        <el-input v-model="editContent" type="textarea" rows="6" placeholder="内容" />
      </div>
      <template #footer>
        <el-button @click="showEdit = false">取消</el-button>
        <el-button type="primary" @click="submitEdit">保存</el-button>
      </template>
    </el-dialog>

    <el-dialog v-model="showComments" :title="currentArticle ? ('评论 - ' + currentArticle.title) : '评论'" width="700px">
      <div>
        <div style="display:flex; gap:12px; margin-bottom:12px;">
          <el-input v-model="commentText" placeholder="输入评论" />
          <el-button type="primary" :disabled="!commentText || commentsLoading" @click="submitComment">发表评论</el-button>
        </div>
        <el-table :data="comments" border>
          <el-table-column prop="id" label="ID" width="80" />
          <el-table-column prop="author_name" label="作者" width="160" />
          <el-table-column prop="content" label="内容" />
          <el-table-column prop="created_at" label="时间" width="220" />
          <el-table-column label="操作" width="160">
            <template #default="{ row }">
              <el-button size="small" type="danger" @click="removeComment(row)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </el-dialog>
  </div>
  </template>

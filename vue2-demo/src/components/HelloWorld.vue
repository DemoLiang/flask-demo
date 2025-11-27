<template>
  <div class="hello">
    <el-card>
      <template #header>
        <div class="card-header">
          <span>测试页面</span>
        </div>
      </template>
      <el-button type="primary">这是一个Element Plus按钮</el-button>
      <p>本地库引入测试成功！</p>
      <p v-if="$route">当前路由路径: {{ $route.path }}</p>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  mounted() {
    console.log('组件已挂载，Vue Router:', this.$router)
    console.log('Element Plus:', window.ElementPlus)
  }
}
</script>

<style scoped>
.hello {
  margin: 20px;
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>

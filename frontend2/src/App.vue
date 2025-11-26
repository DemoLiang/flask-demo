<script setup>
</script>

<template>
  <div style="padding:16px;max-width: 900px;margin:0 auto">
    <div style="margin-bottom: 16px;display:flex;gap:12px">
      <router-link to="/login">登录</router-link>
      <router-link to="/users">用户管理</router-link>
      <router-link to="/articles">文章管理</router-link>
    </div>
  <router-view></router-view>
  </div>
</template>

<style scoped></style>

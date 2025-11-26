<script setup>
</script>

<template>
  <div>
    <router-link to='/login'>登录</router-link>
    <router-link to="/users">用户管理</router-link>
    <router-link to="/articles">文章</router-link>
  </div>
  <router-view></router-view>
</template>

<style scoped></style>

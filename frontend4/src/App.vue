<script setup>
</script>

<template>
  <div style="padding:12px;gap: 12px;max-width: 900px; margin: 0 auto">
    <div style="display: flex;gap: 12px">
      <router-link to="/login">登陆</router-link>
      <router-link to="/users">用户</router-link>
      <router-link to="/articles">文章</router-link>
    </div>
    <router-view />
  </div>
</template>

<style scoped></style>

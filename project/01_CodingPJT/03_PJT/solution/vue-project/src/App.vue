<!-- App.vue -->

<template>
  <header>
    <nav>
      <RouterLink :to="{ name:'ArticleView' }">Articles</RouterLink> | 
      <div v-show="!accountStore.isLogin">
        <RouterLink :to="{ name:'SignUpView' }">SignUpPage</RouterLink> |
        <RouterLink :to="{ name:'LogInView' }">LogInPage</RouterLink> | 
      </div>
      <form @submit.prevent="logOut">
        <input type="submit" value="Logout">
      </form>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'

  const accountStore = useAccountStore()
  const logOut = function () {
    accountStore.logOut()
  }
</script>

<style scoped>
</style>

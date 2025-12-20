<!-- views/ArticleView.vue -->

<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{ name:'CreateView' }">
      [CREATE]
    </RouterLink>
    <hr>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useArticleStore } from '@/stores/articles'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style>

</style>

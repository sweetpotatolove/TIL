<template>
  <div>
    <h1>Article Page</h1>
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue';
import { useArticleStore } from '@/stores/article';
import { onMounted } from 'vue';
const articleStore = useArticleStore()
// articleStore.getArticles()  // 이렇게 해도 상관은 없음
onMounted(() => {
  articleStore.getArticles()
})
</script>

<style>

</style>

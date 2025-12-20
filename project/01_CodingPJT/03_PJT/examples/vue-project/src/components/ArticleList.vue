<template>
  <div>
    <h3>Article List</h3>
    <!-- <p>{{ articleStore.articles }}</p>  -->
    <ArticleListItem 
      v-for="article in articleStore.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import ArticleListItem from '@/components/ArticleListItem.vue'
import { useArticleStore } from '@/stores/article';
const articleStore = useArticleStore()
</script>

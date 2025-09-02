<template>
  <div>
    <img :src="imageSrc">
    <a :href="myUrl">Move to url</a>
    <p :[dynamicattr]="dynamicValue">Dynamic Attr</p>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const imageSrc = ref('https://picsum.photos/200')
  const myUrl = ref('https://www.google.co.kr/')
  const dynamicattr = ref('title')
  const dynamicValue = ref('Hello Vue.js')
</script>

<style scoped>

</style>
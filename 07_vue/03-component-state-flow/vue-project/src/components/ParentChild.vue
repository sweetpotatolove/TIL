<template>
  <article>
    <h3>Parent Child</h3>
    <p>{{ myMsg }}</p>
    <p>{{ myBalance }}</p>
  </article>
</template>

<script setup>
// 1. 배열 형태 -> prop받은 객체 명만 작성
// defineProps(['myMsg'])
// 2. 객체 형태 -> 더 복잡하고 상세한 정의
defineProps({
  myMsg: String, // prop 받은 데이터의 타입
  myBalance: Number
})
</script>

<style scoped>

</style>
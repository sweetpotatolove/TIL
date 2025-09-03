<template>
  <div>
    <!-- Binding to Objects -->
    <div :class="{ 'active': isActive }">Text</div>
    <div class="static" :class="{ active: isActive, 'text-primary': hasInfo }">Text</div>
    <div class="static" :class="classObj">Text</div>

    <!-- Binding to Arrays -->
    <div :class="[activeClass, infoClass]">Text</div>
    <div :class="[{ active: isActive }, infoClass]">Text</div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  const isActive = ref(false)
  const hasInfo = ref(true)
  
  // ref는 반응 객체의 속성으로 액세스되거나 변경될 때 자동으로 래핑 해제
  const classObj = ref({
    active: isActive,
    'text-primary': hasInfo
  })
  const activeClass = ref('active')
  const infoClass = ref('text-primary')
</script>

<style scoped>
  .active {
    color: crimson;
  }

  .text-primary {
    color: blue;
  }
</style>
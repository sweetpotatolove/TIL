<template>
  <div class="wrapper">
    <header class="sidebar">
      <div class="nav" v-for="item in componentsList" :key="item.name">
        <button @click="selected = item.name">{{item.name}}</button>
      </div>
    </header>

    <section class="content">
      <component :is="currentComponent" v-if="currentComponent"></component>
    </section>
  </div>
</template>

<script setup>
import { defineAsyncComponent, ref, computed } from 'vue'

const componentsList = [
  { name: 'Computed' },
  { name: 'Watcher' },
  { name: 'LifecycleHooks' },
]

const selected = ref('Computed')

const currentComponent = computed(() => {
  const selectedComponent = componentsList.find(item => item.name === selected.value)
  if (selectedComponent) {
    return defineAsyncComponent(() => import(`./components/${selectedComponent.name}.vue`))
  }
  return null
})
</script>

<style scoped>
.wrapper {
  display: flex;
}

.sidebar {
  position: relative;
  left: 0;
  top: 0;
  width: 200px;
  height: 100vh;
  border-right: 1px solid black;
  padding: 20px;
  background-color: #ececec;
  margin-right: 20px;
}

.nav {
  margin-bottom: 10px;
}

.nav button {
  width: 100%;
  background-color: white; /* Green background */
  border: 1px solid black; /* Remove borders */
  padding: 10px 20px; /* Some padding */
  text-align: center; /* Center the text */
  text-decoration: none; /* Remove underline */
  display: inline-block; /* Get elements to sit next to each other */
  cursor: pointer; /* Pointer/hand icon */
  border-radius: 5px; /* Rounded corners */
  transition: background-color 0.3s; /* Animation for background color */
}

.nav button:hover,
.nav button:focus  {
  background-color:  #4CAF50; /* Darker green on hover */
  color: white;
}

.content {
  margin-left: auto;
  width: 75vw;
  padding: 20px;
}
</style>

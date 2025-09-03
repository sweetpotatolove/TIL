<template>
  <div>
    <!-- Inline Handlers -->
    <!-- <button v-on:click="count++">Add 1</button> -->
    <button @click="count++">Add 1</button>
    <p>Count: {{ count }}</p>

    <!-- Method Handlers -->
    <button @click="myFunc">Hello</button>

    <!-- Calling Methods in Inline Handlers -->
    <button @click="greeting('hello')">Say hello</button>
    <button @click="greeting('bye')">Say bye</button>

    <!-- Accessing Event Argument in Inline Handlers -->
    <button @click="warning('경고입니다.', $event)">Submit</button>

    <!-- event modifiers -->
    <form @submit.prevent="onSubmit">...</form>
    <a @click.stop.prevent="onLink">...</a>

    <!-- key modifiers -->
    <input @keyup.enter="onSubmit">
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const count = ref(0)

  const name = ref('Alice')
  const myFunc = function (event) {
    console.log(event)
    console.log(event.currentTarget)
    console.log(`Hello ${name.value}!`)
  }

  const greeting = function (message) {
    console.log(message)
    // console.log(event)
  }
  
  const warning = function (message, event) {
    console.log(message)
    console.log(event)
  }

  const onSubmit = function() {
    console.log('on Submit!!')
  }
</script>

<style scoped>

</style>
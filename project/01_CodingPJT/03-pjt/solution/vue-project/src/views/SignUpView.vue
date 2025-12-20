<!-- views/SignUpView.vue -->

<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="useranme">useranme: </label>
      <input type="text" id="username" v-model.trim="username" /> <br>
      
      <label for="password1">password: </label>
      <input type="password" id="password1" v-model.trim="password1" /> <br>
      
      <label for="password2">password confirmation: </label>
      <input type="password" id="password2" v-model.trim="password2" /> <br>
      
      <label for="age">age: </label>
      <input type="number" id="age" v-model.trim="age" /> <br>

      <input type="submit" value="signup">
    </form>
  </div>
</template>

<script setup>
  import { useAccountStore } from '@/stores/accounts' 
  import { ref } from 'vue'

  const username = ref('')
  const password1 = ref('')
  const password2 = ref('')
  const age = ref(0)

  const accountStore = useAccountStore()
  const signUp = function () {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      age: age.value
    }
    accountStore.signUp(payload)
  }
</script>

<style>

</style>

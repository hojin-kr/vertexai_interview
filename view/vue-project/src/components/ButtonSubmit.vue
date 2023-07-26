<script setup lang="ts">

</script>

<template>
  <div class="button-submit">
    <router-link :to="{ name: 'result' }" >질문 생성하기</router-link>
  </div> 
</template>

<style scoped>
  .button-submit {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 1rem;
  }

  .button-submit__label {
    margin-bottom: 0.5rem;
  }

  .button-submit__input {
    width: 100%;
    max-width: 400px;
  }

  input {
    width: 100%;
    height: 40px;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 0 0.5rem;
    font-size: 1rem;
    color: #333;
  }

  input:focus {
    outline: none;
    border-color: #333;
  }
</style>
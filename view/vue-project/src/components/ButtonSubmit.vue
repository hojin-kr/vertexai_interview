<script setup lang="ts">

</script>

<template>
  <div class="button-submit">
    <router-link class="route-link" :to="{ name: 'result', state: {from: 'submit'}}">질문 생성하기</router-link>
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

  .route-link {
    width: 70%;
    height: 40px;
    /* border: 1px solid #ccc; */
    border-radius: 4px;
    padding: 0 0.5rem;
    font-size: 1rem;
    font-weight: 300;
    color: white;
    text-decoration: none;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color:  hsla(160, 100%, 37%, 0.8);
  }

  .route-link:focus {
    
    border-color: hsla(160, 100%, 37%, 1);
  }

  .route-link:hover {
    background-color:  hsla(160, 100%, 37%, 0.2);
  }

  /* text area round */
  textarea {
    width: 100%;
    height: 200px;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 0 0.5rem;
    font-size: 1rem;
  }


</style>
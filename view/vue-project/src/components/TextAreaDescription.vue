<script setup lang="ts">
import { useUserStore } from '@/stores/user';

const userStore = useUserStore();

</script>


<template>
  <div class="text-area">
    <textarea
      id="text-area"
      class="text-area__input"
      placeholder="경력 기술을 입력해주세요."
      rows="5"
      v-model="userStore.description"
    ></textarea>
  </div>
</template>

<style scoped>

  .text-area {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 1rem;
  }

  .text-area__label {
    margin-bottom: 0.5rem;
  }

  .text-area__input {
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

  /* text area round */
  textarea {
    width: 100%;
    height: 150px;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 0 0.5rem;
    font-size: 1rem;
    color: #333;
  }
</style>


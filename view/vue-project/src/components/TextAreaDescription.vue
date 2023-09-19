<script setup lang="ts">
import { useUserStore } from '@/stores/user';

const userStore = useUserStore();

</script>


<template>
  <div class="text-area">
    <textarea
      id="text-area"
      class="text-area__input"
      rows="5"
      v-model="userStore.description"
      maxlength="800"
      placeholder="면접 정보 혹은 경력이나 자기소개를 입력하세요."
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
    max-width: 500px;
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
    height: 200px;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 0.5rem;
    font-size: 1rem;
    color: #333;
  }
</style>


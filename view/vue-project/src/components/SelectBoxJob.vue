<script setup lang="ts">
import { useUserStore } from '@/stores/user';

const userStore = useUserStore();

</script>

<template>
  <div class="selectbox">
    <div class="selectbox__select">
      <select name="selectbox" id="selectbox" v-model="userStore.title">
        <option value="서버 개발자">서버 개발자</option>
        <option value="프론트엔드 개발자">프론트엔드 개발자</option>
        <option value="데브옵스">데브옵스</option>
        <option value="데이터 엔지니어">데이터 엔지니어</option>
        <option value="B2B 마케팅">B2B 마케팅</option>
        <option value="B2C 마케팅">B2C 마케팅</option>
        <option value="모바일 게임 QA">모바일 게임 QA</option>
      </select>
    </div>
  </div>
</template>

<style scoped>
  .selectbox {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 1rem;
  }

  .selectbox__label {
    margin-bottom: 0.5rem;
  }

  .selectbox__select {
    width: 100%;
    max-width: 500px;
  }

  select {
    width: 100%;
    height: 40px;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 0 0.5rem;
    font-size: 1rem;
    color: #333;
  }

  select:focus {
    outline: none;
    border-color: #333;
  }
</style>

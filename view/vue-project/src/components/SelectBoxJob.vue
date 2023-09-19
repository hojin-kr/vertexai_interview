<script setup lang="ts">
import { useUserStore } from '@/stores/user';
import { ModelSelect } from 'vue-search-select'
import 'vue-search-select/dist/VueSearchSelect.css'

const userStore = useUserStore();
// 100가지 직무
const options = [
    { value: '서버 개발자', text: '서버 개발자' },
    { value: '클라이언트 개발자', text: '클라이언트 개발자' },
    { value: '데브옵스 엔지니어', text: '데브옵스 엔지니어' },
    { value: '데이터 엔지니어', text: '데이터 엔지니어' },
    { value: 'B2B 마케팅', text: 'B2B 마케팅' },
    { value: 'B2C 마케팅', text: 'B2C 마케팅' },
    { value: '개발자', text: '개발자' },    
    { value: '게임 기획자', text: '게임 기획자' },
    { value: '게임 개발자', text: '게임 개발자' },
    { value: '영상 제작', text: '영상 제작' },
    { value: 'UI/UX 디자이너', text: 'UI/UX 디자이너' },
    { value: '웹 디자이너', text: '웹 디자이너' },
    { value: '그래픽 디자이너', text: '그래픽 디자이너' },
    { value: '프로덕트 디자이너', text: '프로덕트 디자이너' },
    { value: '프론트엔드 개발자', text: '프론트엔드 개발자' },
    { value: '백엔드 개발자', text: '백엔드 개발자' },
    { value: '풀스택 개발자', text: '풀스택 개발자' },
    { value: '데이터 엔지니어', text: '데이터 엔지니어' },
    { value: '데이터 사이언티스트', text: '데이터 사이언티스트' },
    { value: '데이터 분석가', text: '데이터 분석가' },
    { value: '데이터 엔지니어', text: '데이터 엔지니어' },
    { value: '사업 개발', text: '사업 개발' },
  ]

</script>
<template>
  <!-- object value -->
  <div class="selectBox">
    <!-- <model-select :options="options"
                          v-model="userStore.title"
                          placeholder="select item">
   </model-select> -->
   <!-- user input -->
    <input class="selectBox input" v-model="userStore.title" placeholder="직무를 입력하세요. ex) 서버 개발자, 기획자, B2B 마케팅 … ">
  </div>
  
</template>

<style scoped>
  .selectBox {
    width: 100%;
    max-width: 500px;
    margin: 0 auto;
  }
  .selectBox input {
    width: 100%;
    height: 40px;
    padding: 0 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    box-sizing: border-box;
    margin: 10px 0;
  }
</style>
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
    { value: '퍼포먼스 마케팅', text: '퍼포먼스 마케팅' },
    { value: '콘텐츠 마케팅', text: '콘텐츠 마케팅' },
    { value: '개발자', text: '개발자' },    
    { value: '게임 기획자', text: '게임 기획자' },
    { value: '게임 개발자', text: '게임 개발자' },
    { value: '영상 제작', text: '영상 제작' },
    { value: '사진 제작', text: '사진 제작' },
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
    { value: '영업', text: '영업' },
    { value: '마케팅', text: '마케팅' },
    { value: '기획', text: '기획' },
    { value: '디자인', text: '디자인' },
    { value: '개발', text: '개발' },
    { value: '연구', text: '연구' },
    { value: '영상 제작', text: '영상 제작' },
    { value: '사진 제작', text: '사진 제작' },
    { value: '영상 편집', text: '영상 편집' },
    { value: '사진 편집', text: '사진 편집' },
    { value: '영상 촬영', text: '영상 촬영' },
    { value: '사진 촬영', text: '사진 촬영' },
    { value: '영상 디자인', text: '영상 디자인' },
    { value: '사진 디자인', text: '사진 디자인' },
    { value: '영상 기획', text: '영상 기획' },
    { value: '사진 기획', text: '사진 기획' },
    { value: '영상 마케팅', text: '영상 마케팅' },
    { value: '사진 마케팅', text: '사진 마케팅' },
    { value: '영상 콘텐츠', text: '영상 콘텐츠' },
    { value: '사진 콘텐츠', text: '사진 콘텐츠' },
  ]

</script>
<template>
  <!-- object value -->
  <div class="selectBox">
    <model-select :options="options"
                          v-model="userStore.title"
                          placeholder="select item">
   </model-select>
  </div>
  
</template>

<style scoped>
  .selectBox {
    width: 100%;
    max-width: 500px;
    margin: 0 auto;
  }
</style>
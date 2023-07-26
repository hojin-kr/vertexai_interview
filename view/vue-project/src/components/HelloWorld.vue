<script setup lang="ts">
defineProps<{
  msg: string
}>()
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>
      면접 질문 생성 서비스는 JD(직무 기술서)와 이력서를 기반으로 개인에 맞는 맞춤형 면접 질문을 제공하는 서비스입니다. <br><br>
    </h3>
    이 서비스는 구직자들이 채용 과정에서 직면할 수 있는 다양한 질문들을 예측하고, 적절한 대답을 준비할 수 있도록 도와줄 것입니다.
  </div>
</template>

<style scoped>
h1 {
  font-weight: 400;
  font-size: 1.3rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1rem;
}


.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>

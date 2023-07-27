<script setup lang="ts">
import WelcomeItem from './WelcomeItem.vue'
import SelectBoxJob from './SelectBoxJob.vue'
import TextAreaDescription from './TextAreaDescription.vue'
import ButtonSubmit from './ButtonSubmit.vue'
</script>

<template>
  <WelcomeItem>
    <template #heading>직무 선택</template>
    선택한 직무에 따라 맞춤 질문을 생성합니다.
  </WelcomeItem>
  <SelectBoxJob></SelectBoxJob>
  <WelcomeItem>
    <template #heading>면접 정보 & 경력 & 자기소개</template>
    면접 정보 혹은 경력이나 자기소개를 통해서 맞춤화된 질문을 생성합니다.
  </WelcomeItem>
  <TextAreaDescription></TextAreaDescription>
  
  <ButtonSubmit></ButtonSubmit>
</template>

<script setup lang="ts">
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'
import SelectBoxJob from './SelectBoxJob.vue'
import TextAreaDescription from './TextAreaDescription.vue'
import ButtonSubmit from './ButtonSubmit.vue'
</script>

<template>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>직무 선택</template>
    선택한 직무에 따라 질문이 달라집니다.
  </WelcomeItem>
  <SelectBoxJob></SelectBoxJob>
  <WelcomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading>경력 기술</template>
    경력 기술은 사용자의 경력을 기반으로 사용자의 기술을 분석합니다.
  </WelcomeItem>
  <TextAreaDescription></TextAreaDescription>
  
  <ButtonSubmit></ButtonSubmit>
</template>

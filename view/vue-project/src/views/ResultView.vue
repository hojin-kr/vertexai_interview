<script setup lang="ts">
import { useUserStore } from '@/stores/user';
import { vertex } from '@/stores/vertex';

const userStore = useUserStore();
const vertexUtils = vertex();

// if result is null, then redirect to home
vertexUtils.predict()

console.log(userStore.description)
console.log(userStore.title)
console.log(vertexUtils.result)

</script>

<template>
  <div class="result">
    <!-- vertexUtils.result list -->
    <li v-for="(answer, index) in vertexUtils.result.answer">
      <div>
        <h3 class="question">Q{{ index + 1 }}. {{ answer.question }}</h3>
        <p class="reason">질문의 이유 : {{ answer.reason }}</p>
      </div>
    </li>
  </div>
</template>

<style>
@media (min-width: 1024px) {

  /* li styling */
  li {
    display: flex;
    flex-direction: column;
    align-items: left;
    margin-bottom: 1rem;
  }

  /* question styling */
  /* bold */
  .question {
    font-weight: bold;
    margin-bottom: 0.5rem;
  }

  /* reason styling */

  .reason {
    width: 100%;
    
  }

  /* expectation styling */

  .expectation {
    width: 100%;
    
  }

  
}




</style>

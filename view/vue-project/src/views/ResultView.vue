<script setup lang="ts">
import { useUserStore } from '@/stores/user';
import { vertex } from '@/stores/vertex';

const userStore = useUserStore();
const vertexUtils = vertex();

// history.state foreach
if (isSubmit()) {
  vertexUtils.resetResult()
  let isPredict = true
  if (vertexUtils.loading == 1) {
    isPredict = false
  }
  if (isPredict) {
    repeatPredict()
  }
}

function repeatPredict() {
  vertexUtils.setLoadding(1)
    let step = 0
    for (step = 0; step < 3; step++) {
      vertexUtils.predict()
    }
}

// history.state check
function isSubmit() {
  for (const key in history.state) {
    if (key === 'from') {
        if (history.state[key] === 'submit') {
            return true
        }
    }
  }
  return false
}

// if vertexUtils.loadding is true, then show progress bar
if (vertexUtils.loading) {
  const progress = document.querySelector('.progress') as HTMLProgressElement
  
} else {
  const progress = document.querySelector('.progress') as HTMLProgressElement
  
} 

</script>

<template>
  <div class="result">
    <div class="title" v-if="vertexUtils.loading != 1">
      <h2>{{ userStore.title }}</h2>
    </div>
    <!-- vertexUtils.result list -->
    <div class="progress" v-if="vertexUtils.loading == 1">
      <!-- progress -->
      <div>
        <p>질문 생성중...</p>
      </div>
    </div>
    <div class="scrollbox">
      <div class="placeholder" v-if="vertexUtils.result.length == 0 && vertexUtils.loading == 0">
        <p>면접 정보 입력후 질문 생성하기를 진행해주세요 </p>
      </div>
      <ul>
        <li v-for="(answer, index) in vertexUtils.result">
          <div>
            <h4 class="question">Q{{ index + 1 }}. {{ answer.question }}</h4>
            <p class="reason">{{ answer.reason }}</p>
          </div>
        </li>
      </ul>
    </div>
    <div v-if="vertexUtils.result.length > 0 && vertexUtils.loading != 1">
      <button class="button-submit__input" @click="repeatPredict">추가 생성하기</button>
    </div>
  </div>


</template>

<style>
/* result styling */
  .result {
    margin-top: 3rem;
    margin-bottom: 3rem;
  }

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

  /* progress styling, center modal */
  .progress {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 1rem;
  }

  /* button styling */
  .button-submit__input {
    width: 100%;
    max-width: 300px;
    height: 40px;
    border: 1px solid hsla(160, 100%, 37%, 0.8);
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

  /* center */
  .button-submit__input {
    margin: 0 auto;
  }

  .button-submit__input:focus {
    
    border-color: hsla(160, 100%, 37%, 1);
  }

  .button-submit__input:hover {
    background-color:  hsla(160, 100%, 37%, 0.2);
  }

  /* scrollbox styling */
  .scrollbox {
    width: 100%;
    max-width: 800px;
    height: 400px;
    overflow: scroll;
    border: 1px solid hsla(160, 100%, 37%, 0.8);
    border-radius: 4px;
    padding: 0 0.5rem;
    font-size: 1rem;
    font-weight: 300;
    margin-bottom: 2rem;
    padding-top: 1rem;
    padding-right: 1.5rem;
  }

  .title {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 1rem;
  }

  .title h2 {
    font-weight: 600;
  }

  .placeholder {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 1rem;
  }





</style>

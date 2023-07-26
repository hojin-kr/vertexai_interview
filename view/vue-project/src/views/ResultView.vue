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
    {{ vertexUtils.result }}

  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

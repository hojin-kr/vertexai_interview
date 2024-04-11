<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header>
    <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="60" height="60" /> -->
    <div class="wrapper">
      <HelloWorld msg="인터뷰어 AI" />

      <nav>
        <RouterLink to="/">면접 정보 입력</RouterLink>
        <!-- <RouterLink to="/about">이력서 기반</RouterLink> -->
        <RouterLink to="/result">생성된 질문 보기</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />
  <footer>문의 : <a href="https://www.linkedin.com/in/hojin-jang-221aa3198/">Linkedin</a></footer>
  <footer>Using Google Cloud Platform Vertex AI PaLM 2</footer>
</template>

<style scoped>
footer {
  text-align: center;
  font-size: 12px;
  margin-top: 2rem;
}
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>

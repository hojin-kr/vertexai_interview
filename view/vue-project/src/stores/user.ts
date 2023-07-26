import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
  const description = ref('')
  const title = ref('서버 개발자')
  

  function setDescription(newDescription: string) {
    description.value = newDescription
  }

  function setTitle(newTitle: string) {
    title.value = newTitle
  }

  return { description, title, setDescription, setTitle}
})
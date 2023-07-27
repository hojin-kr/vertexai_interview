import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useUserStore } from '@/stores/user';

  // SAMPLE response
  // ```json
  // { "answer" : [
  //       {
  //         "질문": "TCP, UDP, HTTP, HTTPS의 차이를 설명해주세요.",
  //         "질문 이유": "서버 개발자는 통신 프로토콜에 대한 이해가 필요합니다.",
  //         "답변": "TCP, UDP, HTTP, HTTPS는 모두 통신 프로토콜입니다. TCP는 신뢰성 있는 통신을 위한 프로토콜로, 데이터가 정확하게 전송되었는지 확인하는 기능을 제공합니다. UDP는 신뢰성 있는 통신을 보장하지 않는 프로토콜로, 데이터가 정확하게 전송되지 않더라도 전송에 실패했다고 알려주지 않습니다. HTTP는 웹에서 통신을 위한 프로토콜로, 웹 브라우저와 웹 서버 간의 통신을 정의합니다. HTTPS는 HTTP에 보안 기능을 추가한 프로토콜로, 암호화된 통신을 제공합니다.",
  //       },
  //       {
  //         "질문": "서버 개발자로서 가장 큰 난관은 무엇이었나요?",
  //         "질문 이유": "서버 개발자는 다양한 난관에 직면할 수 있습니다. 이를 극복하기 위해서는 끈기와 열정이 필요합니다.",
  //         "답변": "서버 개발자로서 가장 큰 난관은 버그를 찾고 해결하는 것입니다. 버그는 컴퓨터 프로그램에 있는 오류로, 프로그램의 정상적인 동작을 방해합니다. 버그를 찾고 해결하는 것은 매우 어려운 일이지만, 끈기와 열정을 가지고 해결한다면 충분히 극복할 수 있습니다.",
  //       },
  //       {
  //         "질문": "서버 개발자로 일하면서 가장 보람찬 순간은 언제였나요?",
  //         "질문 이유": "서버 개발자는 자신의 코드가 실행되는 것을 보며 보람을 느낄 수 있습니다.",
  //         "답변": "서버 개발자로 일하면서 가장 보람찬 순간은 자신의 코드가 실행되는 것을 보며 보람을 느낄 수 있습니다. 예를 들어, 서버 개발자가 만든 웹사이트가 많은 사람들에게 사용되고 있을 때, 자신의 코드가 사람들에게 유용하게 쓰이고 있다는 것을 느끼며 보람을 느낄 수 있습니다.",
  //       }
  //     ]}
  // ```

const userStore = useUserStore()

export const vertex = defineStore('vertex', () => {
  const description = ref('')
  const title = ref('')
  const result = ref([])
  const loading = ref(0) // 0: not loading, 1: loading, 2: loaded



  function parsingResult(data: any) {
    // foreach data.answer
    data.answer.forEach((element: any) => {
      if (element.reason == "" || element.question == "" ) {
        return
      }
      result.value.push(element)
    })
    
    setLoadding(2)
  }

  function resetResult () {
    result.value = []
  }

  function setLoadding (status: number) {
    loading.value = status
  }


  // requset to server
  async function predict() {
    description.value = userStore.description
    title.value = userStore.title
    // to https POST requset content type application/json
    const response = await fetch('https://interview.tl-dr.in/predict', {
      method: 'POST',
      body: JSON.stringify({
        title: title.value,
        description:description.value,
        cnt_question_type_deep:'3',
        cnt_question_type_job:'0',
        token:'onesoju2023$%^',
    }),
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      }  
    })
    parsingResult(await response.json()) 
  }
  
  return { result, predict, resetResult, setLoadding, loading}
})
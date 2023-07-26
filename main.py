import vertexai
from vertexai.language_models import TextGenerationModel

from typing import Union

from fastapi import FastAPI
import os

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# get prediction from post data
@app.post("/predict")
def predict(data: dict):
    print(data)
    # check security
    token = data.get("token")
    # get environment variable
    if token != os.environ.get("TOKEN"):
        return {"data": "token error"}
    data = get_prediction(data)
    return data


# func to get prediction from model
def get_prediction(data: dict):
    print("predict")
    vertexai.init(project="etcd-389303", location="us-central1")
    parameters = {
        "temperature": 0.8,
        "max_output_tokens": 1024,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison@001")

    description = data.get("description")
    title = data.get("title")
    cnt_question_type_deep = data.get("cnt_question_type_deep")
    cnt_question_type_job = data.get("cnt_question_type_job")
    response = model.predict(
    """ 
    Extract question from the title & description below in a JSON format.
    Each question should be followed by a reason and an expectation.
    Each reason Length should be more than 150 characters.
    Please answer in Korean.

    Title: """ + title + """
    Text: """ + description + """
    Question Count limit  : """ + cnt_question_type_deep + """
    JSON: {"answer": [{
    \"question\":\"\",
    \"reason\":\"\"
    },{
    \"question\":\"\",
    \"reason\":\"\"
    }]}

    JSON:    
    """,
    **parameters
    )

    #   SAMPLE response
    # {
    # 	"answer": [
    # 		{
    # 			"question": "php 언어를 얼마나 잘 사용하고 있나요?",
    # 			"reason": "php 언어를 주로 사용했다고 했으니 php 언어에 대한 질문을 하면 좋을 것 같습니다.",
    # 			"expectation": "php 언어를 잘 사용하고 있다는 것을 증명할 수 있는 예시를 들어주세요."
    # 		},
    # 		{
    # 			"question": "백오피스 및 게임 서버를 주로 했는데 어떤 경험이 있나요?",
    # 			"reason": "백오피스 및 게임 서버를 주로 했다고 했으니 해당 분야에 대한 질문을 하면 좋을 것 같습니다.",
    # 			"expectation": "백오피스 및 게임 서버 개발 경험에 대해 자세히 알려주세요."
    # 		},
    # 		{
    # 			"question": "어떤 프로젝트를 진행했나요?",
    # 			"reason": "프로젝트 경험을 물어보는 것은 지원자의 경험을 파악하기 좋은 방법입니다.",
    # 			"expectation": "프로젝트 경험을 자세히 알려주세요."
    # 		},
    # 		{
    # 			"question": "어떤 기술을 사용했나요?",
    # 			"reason": "기술 스택을 물어보는 것은 지원자의 기술 수준을 파악하기 좋은 방법입니다.",
    # 			"expectation": "기술 스택을 자세히 알려주세요."
    # 		},
    # 		{
    # 			"question": "왜 이 회사에서 일하고 싶나요?",
    # 			"reason": "지원 동기를 물어보는 것은 지원자가 회사에 관심이 있는지 파악하기 좋은 방법입니다.",
    # 			"expectation": "이 회사에서 일하고 싶은 이유를 알려주세요."
    # 		}
    # 	]
    # }
    # del ``` from response.text
    response.text = response.text.replace("```", "")

    print(response.text)
    print(eval(response.text))
    return eval(response.text)

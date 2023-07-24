import vertexai
from vertexai.language_models import TextGenerationModel

from typing import Union

from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# get prediction from post data
@app.post("/predict")
def predict(data: dict):
    # check security
    token = data.get("token")
    # get environment variable
    if token != os.environ.get("TOKEN"):
        return {"data": "token error"}
    data = get_prediction(data)
    return {"data": data}


# func to get prediction from model
def get_prediction(data: dict):
    vertexai.init(project="etcd-389303", location="us-central1")
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 1024,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison@001")

    condition = data.get("data")
    job = data.get("job")
    cnt_question_type_deep = data.get("cnt_question_type_deep")
    cnt_question_type_job = data.get("cnt_question_type_job")
    
    message = """```{}
    ``` 
    {} 면접을 해야하는데, 정보를 기반으로 질문 {}개하고 직군에 대해 깊게 고민해서 {}개
    출력형태는 template에 맞춰서 json format
    template: "질문":"","질문 이유":"""""
    message = message.format(condition, job, cnt_question_type_deep, cnt_question_type_job)
    # insert condition to string
    response = model.predict(
        message
        ,
        **parameters
    )

    # {"data": "```json\n[\n  {\n    \"질문\": \"최근에 개발한 프로젝트에서 가장 어려웠던 점은 무엇인가요?\",\n    \"질문 이유\": \"개발자가 직면하는 어려움을 파악하고, 지원자가 이를 극복할 수 있는 역량을 갖추고 있는지 확인하기 위함입니다.\"\n  },\n  {\n    \"질문\": \"프로젝트를 진행하면서 가장 중요하게 생각하는 것은 무엇인가요?\",\n    \"질문 이유\": \"지원자가 프로젝트를 진행할 때 어떤 부분을 중요하게 생각하는지를 파악하고, 지원자가 팀과 협업할 때 어떤 태도를 보일지 예측하기 위함입니다.\"\n  },\n  {\n    \"질문\": \"서버 개발자로서 가장 중요한 역량은 무엇이라고 생각하나요?\",\n    \"질문 이유\": \"서버 개발자로서 갖추어야 할 역량을 파악하고, 지원자가 해당 역량을 갖추고 있는지 확인하기 위함입니다.\"\n  }\n]\n```"}
    # data parsing json
    res = eval(response.text.split("```json")[1].split("```")[0])
    return res

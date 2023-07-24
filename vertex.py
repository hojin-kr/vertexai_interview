import vertexai
from vertexai.language_models import TextGenerationModel

vertexai.init(project="etcd-389303", location="us-central1")
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 1024,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison@001")
response = model.predict(
    """```
https://hojin-kr.github.io/history
AWS, GCP 클라우드 인프라 아키텍쳐 구성 및 유지보수
약 5천만 유저 데이터베이스 유지 관리
일간 액티브 유저 10만 이상 웹 서버 운영
TPS 1,000 이상의 서비스 구성 및 운영
데이터레이크 구성 및 비즈니스 인텔리전트(BI) 툴 Zeppelin 운영
PHP 게임 서버 개발
서버 운영 유저 문의 (CS) 대응
Legacy 환경의 현대화 작업
모놀로틱 서버 인프라의 Container 기반의 Full Managed Serverless 전환 및 쿠버네티스 적용
멀티 플랫폼 클라우드 환경 구성 및 연구
로그기반 데이터를 통한 이상 탐지 및 알람 구성
```
서버 개발자 면접을 해야하는데, 정보를 기반으로 질문 2개하고 직군에 대해 깊게 고민해서 1개
출력형태는 template에 맞춰서 json 으로
template: [{\"질문\":\"\",\"질문 이유\":\"\"}]""",
    **parameters
)
print(f"Response from Model: {response.text}")
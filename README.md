# Text to MBTI (Zero Shot - model)
😄 재미로 만드는 MBTI 해석기 - MBTI Translator (나는 오늘 어떤 MBTI처럼 살았을까?)

아래 모델의 프로토타입을 streamlit 으로 구현하고있습니다: https://github.com/ethHong/text_mbti

## About the project & Examples
* 문장을 입력하세요! 다능하다면 '성격유형' 의 성향이 드러날만한 문장을 입력하세요. 아래와 같이 어떤 성격유형에 가까운 발화인지 출력합니다
<img width="531" alt="image" src="https://user-images.githubusercontent.com/43837843/155150705-24830c0b-91a9-4aba-a168-d099e712ca25.png">

## How it works?
* Facebook 의 Zero-shot classification 모델을 사용합니다. 
* 모델은 각 MBTI 요소들과 관련된 단어의 dictionary 통해, 문장이 각 단어들과 연관되어있을 확률을 출력합니다. 

## Model and requirements
* 사용 모델: https://huggingface.co/facebook/bart-large-mnli
* Huggingface 에 공유된 Facebook 으 Zero-shot text classification 모델을 사용합니다. 
* 아래와 같이 requirements를 설정해주세요. 단, torch의 경우 GPU를 사용하고싶다면 알맞읍 버전을 설치해주세요. 
> 02.20 update: Streamlit Sharing을 통한 데모 배포를 위해 requirement.txt만을 사용합니다

```
pip install -r requirements.txt
```
```
streamlit run app.py
```
Zero-shot model 에 대한 레퍼런스는 https://joeddav.github.io/blog/2020/05/29/ZSL.html 이 링크를 참고해주세요!

## Module Description 
Zero-shot text classification은, 텍스트르 input으로 받아, 입력된 label 들과 관련된 주제일 확률을 output합니다. 
이를 활용해, MBTI의 각 요소들과 관련된 단어들을 JSON형태로 입력해 비교한 뒤, MBTI 를 출력해줍니다. 

## Plans
* 아직은 간단히 데모만 만들어놓은 상황입니다.
* 추후 MBTI-dictionary 를 업데이트해, 정확도롸 설득력을 올리는 작업을 할 예정입니다. 
* MT (machine translation) 을 이용한 중역 및, 카카오브레인 오픈소스 zero-shot model 등을 활용해 한국어에 대한 지원을 확대해볼 예정입니다. 

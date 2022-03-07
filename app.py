import streamlit as st
from BART_utils import get_prob, judge_mbti, compute_score, mbti_translator, plot_mbti, device


st.title("MBTI 번역기")
if device == "cpu":
    processor = "🖥️"
else:
    processor = "💽"
st.subheader("Running on {}".format(device + processor))

st.header("💻나는 오늘 어떤 MBTI처럼 말하고, 살았을까?")
st.write("🤗문장을 입력하면, 이를 분석해서 MBTI를 출력해줍니다. 아직은 영어만 지원됩니다!")
st.header("🤔작동 원리는?:")
st.write("Faceook 의 Zero-Shot NLI 모델을 통해 문장과 단어의 연관성을 추론합니다.")
st.write("모델 및 프로젝트에 대해서 자세히 알고싶다면: https://github.com/ethHong/mbti_translator_demo")

user_input = st.text_input("👇👇문장을 입력하면 MBTI가 나옵니다!", "I stayed home all day")
submit = st.button("문장 생성")

if submit:
    with st.spinner("AI가 결과를 분석하는 중이에요..."):
        output_mbti, output_ratio = mbti_translator(
            user_input)

    st.success("Success")
    st.subheader("🤔참 이 MBTI같은 문장이군요🎉 : " + output_mbti)

    for result in output_ratio:
        plot_mbti(result)

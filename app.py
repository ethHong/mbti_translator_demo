import streamlit as st
from BART_utils import (
    get_prob,
    judge_mbti,
    compute_score,
    mbti_translator,
    plot_mbti,
    device,
)


st.title("MBTI translator")
if device == "cpu":
    processor = "🖥️"
else:
    processor = "💽"
st.subheader("Running on {}".format(device + processor))

st.header("💻Infer my MBTI from my langauge (What I speak)")
st.write("🤗Give any sentences: I'll try to guess your MBTI")
st.header("🤔How it works??:")
st.write(
    "Using Zero-Shot NLI model, it computes probability of sentence and MBTI keywords"
)
st.write("More about the model: https://github.com/ethHong/mbti_translator_demo")

user_input = st.text_input("👇👇Put your sentence here", "I stayed home all day")
submit = st.button("Generate")

if submit:
    with st.spinner("AI is analysing result..."):
        output_mbti, output_ratio = mbti_translator(user_input)

    st.success("Success")
    st.subheader("🤔Probable MBTI is...🎉 : " + output_mbti)

    for result in output_ratio:
        plot_mbti(result)

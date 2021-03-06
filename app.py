import streamlit as st
from BART_utils import get_prob, judge_mbti, compute_score, mbti_translator, plot_mbti, device


st.title("MBTI ë²ì­ê¸°")
if device == "cpu":
    processor = "ð¥ï¸"
else:
    processor = "ð½"
st.subheader("Running on {}".format(device + processor))

st.header("ð»ëë ì¤ë ì´ë¤ MBTIì²ë¼ ë§íê³ , ì´ììê¹?")
st.write("ð¤ë¬¸ì¥ì ìë ¥íë©´, ì´ë¥¼ ë¶ìí´ì MBTIë¥¼ ì¶ë ¥í´ì¤ëë¤. ìì§ì ìì´ë§ ì§ìë©ëë¤!")
st.header("ð¤ìë ìë¦¬ë?:")
st.write("Faceook ì Zero-Shot NLI ëª¨ë¸ì íµí´ ë¬¸ì¥ê³¼ ë¨ì´ì ì°ê´ì±ì ì¶ë¡ í©ëë¤.")
st.write("ëª¨ë¸ ë° íë¡ì í¸ì ëí´ì ìì¸í ìê³ ì¶ë¤ë©´: https://github.com/ethHong/mbti_translator_demo")

user_input = st.text_input("ððë¬¸ì¥ì ìë ¥íë©´ MBTIê° ëìµëë¤!", "I stayed home all day")
submit = st.button("ë¬¸ì¥ ìì±")

if submit:
    with st.spinner("AIê° ê²°ê³¼ë¥¼ ë¶ìíë ì¤ì´ìì..."):
        output_mbti, output_ratio = mbti_translator(
            user_input)

    st.success("Success")
    st.subheader("ð¤ì°¸ ì´ MBTIê°ì ë¬¸ì¥ì´êµ°ìð : " + output_mbti)

    for result in output_ratio:
        plot_mbti(result)

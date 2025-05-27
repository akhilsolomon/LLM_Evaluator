import streamlit as st
from feedback.user_feedback import store_feedback

st.title("LLM Answer Feedback")

answer_id = st.text_input("Answer ID")
thumbs = st.selectbox("Was this answer useful?", ["👍", "👎"])
comment = st.text_area("Comments or Suggestions")

if st.button("Submit Feedback"):
    store_feedback(answer_id, thumbs, comment)
    st.success("Thank you for your feedback!")

import streamlit as st
import re

st.title("AI Resume Matcher")
st.write("Stage 2: Text Cleaning")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

resume_text = st.text_area("Paste Resume Text")
jd_text = st.text_area("Paste Job Description Text")

if st.button("Clean Text"):
    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(jd_text)

    st.subheader("Cleaned Resume Text")
    st.write(cleaned_resume)

    st.subheader("Cleaned Job Description Text")
    st.write(cleaned_jd)

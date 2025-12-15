import streamlit as st
import re

st.title("AI Resume Matcher")
st.write("Stage 2: Text Cleaning + Stopwords Removal")

stopwords = {
    "i", "am", "is", "are", "the", "and", "or", "to", "with", "in", "for", "of", "on", "a"
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [word for word in words if word not in stopwords]
    return " ".join(words)

resume_text = st.text_area("Paste Resume Text")
jd_text = st.text_area("Paste Job Description Text")

if st.button("Process Text"):
    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(jd_text)

    st.subheader("Processed Resume Text")
    st.write(cleaned_resume)

    st.subheader("Processed Job Description Text")
    st.write(cleaned_jd)

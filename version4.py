import streamlit as st
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("AI Resume Matcher")
st.write("Stage 3: Resume Matching using TF-IDF")

stopwords = {
    "i", "am", "is", "are", "the", "and", "or", "to", "with", "in", "for", "of", "on", "a"
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [word for word in words if word not in stopwords]
    return " ".join(words)

def calculate_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return similarity[0][0]

resume_text = st.text_area("Paste Resume Text")
jd_text = st.text_area("Paste Job Description Text")

if st.button("Match Resume"):
    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(jd_text)

    score = calculate_similarity(cleaned_resume, cleaned_jd)

    st.subheader("Processed Resume Text")
    st.write(cleaned_resume)

    st.subheader("Processed Job Description Text")
    st.write(cleaned_jd)

    st.subheader("Match Score")
    st.write(f"{round(score * 100, 2)} %")

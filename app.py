import streamlit as st
import re
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Resume Matcher", layout="centered")

st.title("🤖 AI-Based Resume Matcher")
st.write("Upload a resume and compare it with a Job Description")

# ---------------- STOPWORDS ----------------
stopwords = {
    "i", "am", "is", "are", "the", "and", "or", "to", "with",
    "in", "for", "of", "on", "a", "as", "by", "an"
}

# ---------------- FUNCTIONS ----------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [word for word in words if word not in stopwords]
    return " ".join(words)

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def calculate_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return similarity[0][0]

# ---------------- UI ----------------
st.header("📄 Upload Resume (PDF)")
uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

st.header("📝 Paste Job Description")
jd_text = st.text_area("Job Description", height=200)

def extract_keywords(text):
    words = text.split()
    return set(words)


if st.button("🔍 Match Resume"):

    if uploaded_file is not None and jd_text.strip() != "":
        resume_text = extract_text_from_pdf(uploaded_file)

        cleaned_resume = clean_text(resume_text)
        cleaned_jd = clean_text(jd_text)

        score = calculate_similarity(cleaned_resume, cleaned_jd)

        st.success("✅ Matching Completed")

        st.subheader("📊 Match Score")
        st.progress(int(score * 100))
        st.write(f"**{round(score * 100, 2)} % Match**")
        resume_keywords = extract_keywords(cleaned_resume)
        jd_keywords = extract_keywords(cleaned_jd)

        matched_skills = resume_keywords.intersection(jd_keywords)
        missing_skills = jd_keywords - resume_keywords

        st.subheader("✅ Matched Skills")
        st.write(", ".join(list(matched_skills)[:15]))

        st.subheader("❌ Missing Skills")
        st.write(", ".join(list(missing_skills)[:15]))


        with st.expander("📄 Processed Resume Text"):
            st.write(cleaned_resume)

        with st.expander("📝 Processed Job Description Text"):
            st.write(cleaned_jd)

    else:
        st.warning("⚠️ Please upload a resume PDF and paste the job description.")

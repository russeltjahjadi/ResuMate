from google import genai
import streamlit as st
import PyPDF2
import io
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📄", layout="centered")

st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI and get AI-powered feedback tailored to your needs!")

GOOGLE_GEMINI_KEY = os.getenv("GEMINI_API_KEY")

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're targetting (optinal)")

analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)
        if not file_content.strip():
            st.error("File does not have any content...")
            st.stop()

        prompt = f"""
        Please analyze this resume and provide constructive feedback.
        Focus on the following aspects:
        1. Content clarify and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role if job_role else 'general job applications'}

        Resume content:
        {file_content}

        Please provide your analysis in a clear, structured format with specific recommendations. 
        """

        client = genai.Client(api_key=GOOGLE_GEMINI_KEY)
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,            
        )

        st.markdown("### Analysis Results")
        st.markdown(response.text)
    except Exception as e:
        st.error(f"An error occured: {str(e)}")
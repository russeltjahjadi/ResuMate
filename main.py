import io
import os
from dotenv import load_dotenv
from google import genai
import PyPDF2
import streamlit as st

load_dotenv()

# 1. Page Configuration
st.set_page_config(
    page_title="Resumate - AI Resume Critique",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for polished UI touches
st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 2rem;
        max-width: 950px;
    }
    .stButton > button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        border-radius: 8px;
        height: 3rem;
        font-weight: 600;
    }
    </style>
""",
    unsafe_allow_html=True,
)

GOOGLE_GEMINI_KEY = os.getenv("GEMINI_API_KEY")


def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text


def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")


# 2. Hero Header Section
st.title("⚡ Resumate")
st.caption(
    "Get instant, actionable feedback on your resume powered by Gemini AI."
)
st.divider()

# 3. Input Controls organized in Columns
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("1. Upload Resume")
    uploaded_file = st.file_uploader(
        "Supported formats: PDF, TXT",
        type=["pdf", "txt"],
        help="Upload your latest resume file here.",
    )

with col2:
    st.subheader("2. Target Role")
    job_role = st.text_input(
        "Job Title / Target Role (Optional)",
        placeholder="e.g. Senior Backend Engineer, Product Manager",
        help="Tailors the AI feedback specifically toward this job profile.",
    )

st.write("")  # Spacing

# 4. Action Button & Analysis Workflow
analyze_button = st.button("🚀 Analyze Resume", type="primary")

if analyze_button:
    if not uploaded_file:
        st.warning("⚠️ Please upload a resume before starting the analysis.")
    else:
        with st.spinner("🔍 Reading resume and generating critique..."):
            try:
                file_content = extract_text_from_file(uploaded_file)
                if not file_content.strip():
                    st.error("The uploaded file appears to be empty.")
                    st.stop()

                prompt = f"""
                You are a top-tier executive tech recruiter and resume strategist.
                Analyze the following resume and provide a structured, high-impact critique.

                Target Job Role: {job_role if job_role else 'General Applications'}

                Please format your response using standard Markdown with these specific section headers:
                
                ## Summary & Overall Impression
                Provide a 2-3 sentence overview of the resume's core strengths and first impression.

                ## 🎯 Key Strengths
                - Highlighting strong bullet points, skills, or achievements.

                ## ⚠️ High-Priority Improvements
                - Critical action items to fix right away (metrics, formatting, clarity).

                ## 🛠️ Detailed Breakdown
                ### 1. Content & Impact (Quantifiable Metrics)
                ### 2. Skills & Keywords Alignment
                ### 3. Action Verbs & Tone

                ## 💡 Tailored Advice for {job_role if job_role else 'Target Role'}
                Specific suggestions to position the candidate best for this role.

                Resume text:
                ---
                {file_content}
                ---
                """

                client = genai.Client(api_key=GOOGLE_GEMINI_KEY)

                # Fallback model execution
                models = [                    
                    "gemini-3.5-flash-lite",                    
                ]
                response_text = None

                for model in models:
                    try:
                        res = client.models.generate_content(
                            model=model,
                            contents=prompt,
                        )
                        response_text = res.text
                        break
                    except Exception as model_err:
                        if (
                            "503" in str(model_err)
                            or "UNAVAILABLE" in str(model_err)
                        ):
                            continue
                        raise model_err

                if not response_text:
                    st.error(
                        "AI servers are currently busy. Please try again in a few seconds."
                    )
                    st.stop()

                st.divider()

                # 5. Display Results cleanly
                st.subheader("📊 Analysis Results")

                # # Content preview in an expander
                # with st.expander("📄 View Extracted Resume Text"):
                #     st.text_area("Extracted Text", file_content, height=200)

                # Render the structured AI critique
                st.markdown(response_text)

            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")
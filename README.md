# 📄 ResuMate - AI Resume Critiquer

> Your personal AI-powered resume coach. Get intelligent, actionable feedback to make your resume stand out.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## ✨ Features

- 🤖 **AI-Powered Analysis** - Leverages Google's Gemini AI for intelligent resume critique
- 📤 **Easy Upload** - Support for PDF and TXT file formats
- 🎯 **Role-Specific Feedback** - Tailor analysis to your target job role
- 💡 **Constructive Insights** - Get feedback on:
  - Content clarity and impact
  - Skills presentation
  - Experience descriptions
  - Actionable improvement recommendations

## 📋 Prerequisites

- Python 3.11 or higher
- A [Google Gemini API key](https://ai.google.dev/)
- pip or uv package manager

## 🚀 Quick Start

### 1. Clone or navigate to the project

```bash
cd ResuMate
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
# or with uv:
uv sync
```

### 4. Set up your API key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the application

```bash
streamlit run main.py
```

The application will open in your default browser at `http://localhost:8501`

## 📖 How to Use

1. **Upload Your Resume** - Click the upload button and select a PDF or TXT file
2. **Enter Job Role (Optional)** - Specify the job role you're targeting for more tailored feedback
3. **Click "Analyze Resume"** - Let the AI work its magic
4. **Review Recommendations** - Get detailed, actionable feedback to improve your resume

## 🛠️ Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Modern web app framework
- **AI Model**: [Google Gemini](https://ai.google.dev/) - Advanced language model
- **PDF Processing**: [PyPDF2](https://github.com/py-pdf/PyPDF2) - Extract text from PDFs
- **Environment**: [python-dotenv](https://github.com/theskumar/python-dotenv) - Manage environment variables

## 📦 Dependencies

All dependencies are listed in `pyproject.toml`:

- google-genai >= 2.18.1
- openai >= 3.2.0
- pypdf2 >= 3.0.1
- python-dotenv >= 1.2.3
- streamlit >= 1.61.1

## ⚙️ Configuration

### Required Environment Variables

- `GEMINI_API_KEY` - Your Google Gemini API key (required for AI analysis)

### Optional Customization

You can modify the resume analysis prompt in `main.py` to adjust:

- Analysis focus areas
- Feedback style and tone
- Specific requirements for your domain

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report issues
- Submit pull requests
- Suggest improvements

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Russel Tjahjadi** - [GitHub](https://github.com/russeltjahjadi)

---

**Happy Resume Critiquing! 🎉**

# Report Customization and Standardization Tool

This repository contains the research implementation and web-based interface for Report Customization and Standardization, a master's dissertation project developed at SVNIT Surat under the guidance of Dr. Dipti Rana (Associate Professor).

This Streamlit website helps you automatically generate PowerPoint presentations from a topic and standardize existing slides to match any design template.  Whether you're a student, educator, or professional, this tool makes it easy to create polished, consistent presentations aligned with your desired formatting or branding.

Streamlit Website: https://huggingface.co/spaces/SVNIT25/PPTX_generativeai

## 🔍 Overview

This tool enables automatic segmentation and standardization of reports and presentations using NLP and machine learning. The goal is to convert unstructured academic or industry content into professionally structured formats using predefined or custom templates.

## 🚀 Features

### 🧠 ML/NLP Pipeline
- Fine-tuned **BERT** model for paragraph-level report section classification.
- **Zero-shot classification** using HuggingFace's `facebook/bart-large-mnli` for labeling unseen content.
- Custom dataset preparation with paragraph-wise `.txt` files and manual `.label` annotations.

### 💻 Streamlit Web Application
The user-friendly app supports:
1. **Generate New Presentation**
   - Enter a topic name, choose number of slides, and select a theme (predefined, custom, or upload).
   - Automatically generates a PPT using NLP content generation and theme styling.

2. **Standardize Existing Presentation**
   - Upload a raw PPT and a template.
   - Automatically maps content into template-defined layouts, applying color schemes, fonts, and headers.

### 📦 Export Options
- Download the generated or standardized presentation as `.pptx`, '.txt', '.docx'
- Works across multiple devices with an easy web interface.

## 📸 Screenshots

### 1. Presentation Generation Interface
![Screenshot 1](screenshots/generate_ppt.png)

### 2. Theme Customization
![Screenshot 2](screenshots/theme_customization.png)

### 3. Standardize Existing Presentation
![Screenshot 3](screenshots/standardize_existing.png)

## 🛠 Technologies Used

- **Python 3.10**
- **Transformers (HuggingFace)**
- **BERT, BART (Zero-shot)**
- **Scikit-learn, Pandas, NumPy**
- **Streamlit**
- **python-pptx**
- **pdfminer, docx2txt** (for document preprocessing)

## 📁 Repository Structure

```bash
├── data/                   # Paragraph-wise .txt and .label files
├── ml_pipeline/           # BERT fine-tuning and zero-shot scripts
├── streamlit_app/         # Streamlit app code (UI + Backend)
├── utils/                 # Preprocessing scripts (pdf/docx/pptx)
├── README.md
└── requirements.txt

## Research Goals
Automate report formatting across templates (IEEE, Springer, Thesis, etc.)
Train a robust classifier to identify sections like Abstract, Methodology, etc.
Provide a customizable and reusable interface for professional users.

🙌 Acknowledgments
Dr. Dipti Rana – Associate Professor, SVNIT Surat (Research Supervisor)
SLB Pune – For exposure to real-world reporting and dashboarding practices
HuggingFace, Streamlit, python-pptx – For powerful open-source tools

🔗 Connect With Me
📫 nehaapatel2001@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/neha-patel66/
📊 GitHub: https://github.com/Nehapatel6626

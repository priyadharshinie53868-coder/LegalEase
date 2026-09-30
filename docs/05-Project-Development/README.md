# Phase 5 — Project Development

## 1. Directory Structure

```text
LegalEase/
├── backend/
│   ├── __init__.py
│   ├── main.py                     # FastAPI application setup & CORS
│   ├── routes.py                   # REST endpoints (/, /health, /generate)
│   ├── schemas.py                  # Pydantic data validation models
│   ├── ai_core/
│   │   ├── __init__.py
│   │   ├── prompt_builder.py       # Adaptive legal prompt builder
│   │   └── gemini_generator.py     # Gemini client with multi-layer fallback
│   ├── services/
│   │   ├── __init__.py
│   │   └── document_service.py     # Business logic orchestrator
│   └── utils/
│       ├── __init__.py
│       ├── text_utils.py           # Text cleaner & fence stripper
│       └── validators.py           # Business logic validators
│
├── frontend/
│   ├── __init__.py
│   ├── app.py                      # Main Streamlit web application
│   └── components/
│       ├── __init__.py
│       └── document_editor.py      # Editable preview and download bar
│
├── document_generators/
│   ├── __init__.py
│   ├── txt_generator.py            # Plain text exporter
│   ├── docx_generator.py           # Word (.docx) generator with styles & footer
│   └── pdf_generator.py            # PDF generator with fpdf2 & pagination
│
├── assets/
│   └── logo.png                    # Brand logo used in DOCX & PDF
│
├── docs/                           # 8-Phase Documentation Folders
│   ├── 01-Brainstorming-Ideation/
│   ├── 02-Requirement-Analysis/
│   ├── 03-Project-Design/
│   ├── 04-Project-Planning/
│   ├── 05-Project-Development/
│   ├── 06-Project-Testing/
│   ├── 07-Project-Documentation/
│   └── 08-Project-Demonstration/
│
├── tests/
│   ├── __init__.py
│   ├── test_api.py                 # FastAPI route & validation tests
│   ├── test_prompt.py              # Prompt construction tests
│   └── test_document_generation.py # Exporter tests for TXT/DOCX/PDF
│
├── .env.example                    # Sample environment variables
├── .gitignore                      # Git ignore rules
├── requirements.txt                # Python dependencies
└── README.md                       # Main project documentation
```

## 2. Key Implementation Highlights
- **Prompt Specialization:** Each document type (NDA, Employment, Lease, etc.) triggers specific clauses and statutory headings.
- **Safety Fallbacks:** Handlers for API quota, connection loss, and missing local assets ensure zero runtime crashes.
- **Dynamic State Synchronization:** Real-time sync between the user's edits in Streamlit and the export generators.

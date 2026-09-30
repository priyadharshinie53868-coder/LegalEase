# LegalEase — AI-Powered Legal Document Generator
## Complete Project Development Specification

> **Purpose:** This document is an implementation guide for building the LegalEase project from scratch.
> It is written so that an AI coding assistant can use it as the main project specification.

---

# 1. Project Overview

## Project Name

**LegalEase — AI-Powered Legal Document Generator**

## Objective

Build a web application that allows a user to enter details such as:

- Legal document type
- Parties involved
- Terms and conditions
- Effective date
- Other relevant information

The application sends these details to a Generative AI model and generates a complete, professionally structured legal document.

The user must then be able to:

1. View the generated document.
2. Edit the generated content.
3. Download it as:
   - `.txt`
   - `.docx`
   - `.pdf`

Example document types:

- Employment Contract
- NDA
- Lease Agreement
- Service Agreement
- Freelance Contract
- Offer Letter
- General Agreement

## Important Legal Disclaimer

The application generates draft legal content using AI. It must clearly state that generated content should be reviewed by a qualified legal professional before being used as a legally binding document.

---

# 2. High-Level Application Flow

```text
                    USER
                      |
                      v
             +----------------+
             |   Streamlit    |
             |    Frontend    |
             +-------+--------+
                     |
                     | HTTP POST /generate
                     v
             +----------------+
             |    FastAPI     |
             |    Backend     |
             +-------+--------+
                     |
                     v
             +----------------+
             | Prompt Builder |
             +-------+--------+
                     |
                     v
             +----------------+
             |  Gemini API    |
             | Generative AI  |
             +-------+--------+
                     |
                     v
             +----------------+
             | Generated Text |
             +-------+--------+
                     |
             +-------+--------+
             |                |
             v                v
       Editable Preview   Formatter
                              |
                  +-----------+-----------+
                  |           |           |
                  v           v           v
                 TXT         DOCX        PDF
```

---

# 3. Technology Stack

## Backend

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

## AI

- Google Gemini API
- Current supported Gemini model available through the chosen Google Generative AI SDK/API

> Do not hard-code an obsolete model name. Store the model name in configuration so it can be changed without modifying application logic.

## Frontend

- Streamlit

## Document Generation

- `python-docx` for DOCX
- `fpdf2` or FPDF-compatible library for PDF
- Python standard library for TXT

## Supporting Libraries

- `requests`
- `python-dotenv`
- `Pillow`

## Development

- Git
- GitHub
- Python virtual environment

---

# 4. Required Knowledge

Before implementation, understand the following:

## Python

- Functions
- Classes
- Lists and dictionaries
- JSON
- Exceptions
- File handling
- Virtual environments
- Environment variables

## REST APIs

Understand:

```text
GET
POST
JSON request
JSON response
HTTP status codes
```

## FastAPI

Understand:

- FastAPI application
- Routes
- POST endpoints
- Pydantic models
- Request validation
- Response models
- CORS if required

## Streamlit

Understand:

- `st.text_input`
- `st.text_area`
- `st.selectbox`
- `st.date_input`
- `st.button`
- `st.download_button`
- `st.session_state`
- columns/layout
- displaying generated content

## Generative AI

Understand:

- API keys
- Prompt engineering
- System instructions
- Structured prompts
- Model responses
- Error handling
- Token/context limitations

---

# 5. Initial Environment Setup

## Step 1 — Install Python

Install Python 3.10 or newer.

Verify:

```bash
python --version
```

or:

```bash
py --version
```

---

# 6. Create Project Folder

```bash
mkdir LegalEase
cd LegalEase
```

---

# 7. Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then:

```powershell
venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

After activation, the terminal should show something similar to:

```text
(venv)
```

---

# 8. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

# 9. Install Dependencies

Create:

```text
requirements.txt
```

Initial dependencies:

```text
fastapi
uvicorn[standard]
streamlit
pydantic
requests
python-dotenv
python-docx
fpdf2
Pillow
google-genai
```

Install:

```bash
pip install -r requirements.txt
```

> Use the currently supported Google Gemini SDK/API. If the selected SDK differs, update the dependency and AI integration module accordingly.

---

# 10. Environment Variables

Create:

```text
.env
```

Example:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=your_supported_gemini_model
BACKEND_URL=http://127.0.0.1:8000
```

Never commit `.env` to GitHub.

Create:

```text
.gitignore
```

with:

```gitignore
venv/
.env
__pycache__/
*.pyc
.generated/
generated/
.streamlit/secrets.toml
```

---

# 11. Recommended Project Structure

Create the following structure:

```text
LegalEase/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│   │
│   ├── ai_core/
│   │   ├── __init__.py
│   │   ├── gemini_generator.py
│   │   └── prompt_builder.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── document_service.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── text_utils.py
│       └── validators.py
│
├── frontend/
│   ├── app.py
│   └── components/
│       └── document_editor.py
│
├── document_generators/
│   ├── __init__.py
│   ├── txt_generator.py
│   ├── docx_generator.py
│   └── pdf_generator.py
│
├── assets/
│   └── logo.png
│
├── tests/
│   ├── test_api.py
│   ├── test_prompt.py
│   └── test_document_generation.py
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 12. Architecture Responsibilities

## Frontend

Streamlit is responsible for:

- Collecting user input
- Calling FastAPI
- Displaying generated content
- Allowing editing
- Providing download buttons
- Showing errors/loading states
- Showing legal disclaimer

## Backend

FastAPI is responsible for:

- Receiving requests
- Validating input
- Building the generation request
- Calling Gemini
- Returning generated document content
- Handling errors

## AI Core

Responsible for:

- Prompt construction
- Gemini API call
- Response extraction
- Basic response validation

## Document Generators

Responsible for:

- TXT generation
- DOCX formatting
- PDF formatting

---

# 13. Backend Data Model

Create a Pydantic model similar to:

```python
class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    effective_date: str
    additional_details: str | None = None
```

The API should reject:

- Empty document type
- Empty parties
- Empty terms
- Invalid/missing date where required

---

# 14. FastAPI Application

Create:

```text
backend/main.py
```

Responsibilities:

1. Initialize FastAPI.
2. Add application title and description.
3. Add a root/health endpoint.
4. Include routes from `routes.py`.
5. Configure CORS if frontend/backend run on different origins.

Expected endpoints:

```text
GET  /
GET  /health
POST /generate
```

---

# 15. Health Endpoint

Example behavior:

```text
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

This is useful for checking whether the backend is running.

---

# 16. Main Generate Endpoint

Endpoint:

```text
POST /generate
```

Input:

```json
{
  "document_type": "Employment Contract",
  "parties": "ABC Technologies and Rahul Kumar",
  "terms": "Salary: ₹10 LPA; Role: Software Engineer; Notice Period: 30 days",
  "effective_date": "2026-10-01",
  "additional_details": "Full-time employment"
}
```

Processing:

```text
Request
  ↓
Pydantic validation
  ↓
Prompt builder
  ↓
Gemini generator
  ↓
Response validation
  ↓
JSON response
```

Response:

```json
{
  "success": true,
  "document_type": "Employment Contract",
  "content": "EMPLOYMENT AGREEMENT..."
}
```

---

# 17. Gemini Integration

Create:

```text
backend/ai_core/gemini_generator.py
```

This module should contain all Gemini-specific logic.

Do NOT call Gemini directly from Streamlit.

Correct:

```text
Streamlit
    ↓
FastAPI
    ↓
Gemini Generator
    ↓
Gemini API
```

Incorrect:

```text
Streamlit
    ↓
Gemini API
```

The backend should control AI requests.

---

# 18. Prompt Builder

Create:

```text
backend/ai_core/prompt_builder.py
```

The prompt should be dynamically generated from the user's inputs.

The AI should be instructed to:

- Act as a legal-document drafting assistant.
- Generate a complete draft.
- Use the requested document type.
- Use the supplied parties.
- Include supplied terms.
- Use the effective date.
- Create clear sections.
- Avoid inventing user-specific facts.
- Clearly mark information that is missing.
- Use professional formatting.
- Return only the document content when possible.
- Avoid pretending to provide jurisdiction-specific legal advice.
- Include a review disclaimer where appropriate.

---

# 19. Prompt Structure

Use a structured prompt similar to:

```text
ROLE:
You are an AI-assisted legal document drafting system.

TASK:
Generate a professional draft legal document.

DOCUMENT TYPE:
{document_type}

PARTIES:
{parties}

TERMS:
{terms}

EFFECTIVE DATE:
{effective_date}

ADDITIONAL DETAILS:
{additional_details}

REQUIREMENTS:
1. Generate a complete structured document.
2. Use clear headings.
3. Include all supplied information.
4. Do not invent important facts.
5. Identify missing information with placeholders.
6. Include appropriate sections for this document type.
7. Include signature sections where appropriate.
8. Maintain professional legal-document language.
9. The output is a draft and should be reviewed by a qualified legal professional.
```

---

# 20. Document-Type-Specific Structure

The prompt should adapt based on the document type.

## Employment Contract

Possible sections:

```text
Title
Parties
Position
Responsibilities
Compensation
Working Hours
Benefits
Confidentiality
Intellectual Property
Leave
Termination
Notice Period
Governing Law
Signatures
```

## NDA

Possible sections:

```text
Title
Parties
Purpose
Definition of Confidential Information
Obligations
Exclusions
Permitted Disclosures
Term
Return/Destruction of Information
Remedies
Governing Law
Signatures
```

## Lease Agreement

Possible sections:

```text
Title
Landlord
Tenant
Property
Lease Term
Rent
Security Deposit
Utilities
Maintenance
Restrictions
Termination
Notice
Governing Law
Signatures
```

Do not hard-code complete legal contracts into the application. Use the AI to generate the draft dynamically.

---

# 21. AI Response Validation

After receiving Gemini's response:

1. Check that content exists.
2. Check that it is not an error response.
3. Check that it is not empty.
4. Clean unnecessary markdown if required.
5. Return the content to the frontend.

If generation fails:

```json
{
  "success": false,
  "error": "Unable to generate document. Please try again."
}
```

Never expose the Gemini API key or internal exception details to the user.

---

# 22. Streamlit Frontend

Create:

```text
frontend/app.py
```

The frontend should have:

```text
LegalEase
AI-Powered Legal Document Generator
```

---

# 23. Input Section

Create fields for:

### Document Type

Use a dropdown:

```text
Employment Contract
NDA
Lease Agreement
Service Agreement
Freelance Contract
Offer Letter
General Agreement
Other
```

### Parties

Text area:

```text
Example:
ABC Technologies (Employer)
Rahul Kumar (Employee)
```

### Terms

Text area:

```text
Salary: ₹10 LPA;
Role: Software Engineer;
Notice Period: 30 days;
Working Hours: 9 AM to 6 PM
```

### Effective Date

Use:

```python
st.date_input(...)
```

### Additional Details

Optional text area.

---

# 24. Generate Button

Button:

```text
Generate Document
```

When clicked:

```text
Validate inputs
     ↓
Show spinner
     ↓
POST /generate
     ↓
Receive response
     ↓
Store generated document in session_state
     ↓
Display document
```

Use `st.session_state` so the generated content does not disappear when Streamlit reruns.

---

# 25. API Call from Streamlit

Frontend sends:

```json
{
  "document_type": "...",
  "parties": "...",
  "terms": "...",
  "effective_date": "...",
  "additional_details": "..."
}
```

to:

```text
http://127.0.0.1:8000/generate
```

Use the backend URL from `.env` or Streamlit configuration rather than hard-coding it throughout the code.

---

# 26. Generated Document Preview

After generation, show:

```text
Generated Document
------------------

[editable document content]
```

Use a Streamlit text area for editing.

Example:

```text
st.text_area(
    "Edit Document",
    value=generated_content,
    height=600
)
```

The edited version becomes the final version used for downloads.

---

# 27. Document Editing Flow

```text
Gemini Generated Content
          ↓
       Preview
          ↓
       User edits
          ↓
   Save edited content
          ↓
      Download
```

The application should always export the **latest edited content**, not the original AI output.

---

# 28. TXT Generation

Implement:

```text
document_generators/txt_generator.py
```

Input:

```text
document text
```

Output:

```text
document.txt
```

The TXT file should contain the exact edited text.

---

# 29. DOCX Generation

Implement:

```text
document_generators/docx_generator.py
```

Use `python-docx`.

The DOCX should include:

- Logo
- Document title
- Proper headings
- Paragraphs
- Terms section
- Signature section
- Footer
- Professional spacing
- Consistent font

Suggested default font:

```text
Times New Roman
```

Do not depend on the AI response having perfect formatting. The DOCX formatter should apply formatting programmatically.

---

# 30. PDF Generation

Implement:

```text
document_generators/pdf_generator.py
```

Use FPDF/FPDF2.

PDF should contain:

- Logo/header
- Document title
- Sections
- Paragraphs
- Terms
- Footer
- Page numbers if practical
- Signature section

Handle page breaks properly.

Do not allow text to overflow outside the page.

---

# 31. Logo Handling

Place:

```text
assets/logo.png
```

The document generators should check whether the logo exists before attempting to insert it.

If the logo is unavailable:

```text
Continue generation without logo.
```

Do not crash the application.

---

# 32. Text Sanitization

Create:

```text
backend/utils/text_utils.py
```

Possible responsibilities:

- Remove unwanted control characters.
- Normalize quotation marks where necessary.
- Clean excessive whitespace.
- Preserve important punctuation.
- Prevent malformed document output.

Do not aggressively modify legal text.

---

# 33. Error Handling

Handle at least:

### Invalid input

```text
Please enter the required information.
```

### Gemini API failure

```text
Unable to generate the document right now.
Please try again.
```

### Backend unavailable

```text
Unable to connect to the backend.
Please make sure FastAPI is running.
```

### Document generation failure

```text
Unable to create the requested file.
Please try again.
```

### Missing API key

```text
Gemini API key is not configured.
```

Never expose:

- API keys
- stack traces
- internal paths
- sensitive backend information

---

# 34. Security Requirements

At minimum:

- Store API key in `.env`.
- Never commit `.env`.
- Validate input.
- Limit unnecessarily large input.
- Do not log API keys.
- Do not expose raw exceptions.
- Avoid storing sensitive legal documents permanently unless required.
- Show the user that generated content requires review.

---

# 35. Frontend UI Layout

Recommended layout:

```text
-------------------------------------------------
                    LegalEase
          AI-Powered Legal Document Generator
-------------------------------------------------

Document Type
[ Employment Contract                 ]

Parties
[                                        ]
[                                        ]

Terms & Conditions
[                                        ]
[                                        ]

Effective Date
[ 01 / 10 / 2026 ]

Additional Details
[                                        ]
[                                        ]

              [ Generate Document ]

-------------------------------------------------
                 Generated Document
-------------------------------------------------

[                                        ]
[                                        ]
[              EDITABLE                 ]
[                                        ]
[                                        ]

-------------------------------------------------

[ Download TXT ] [ Download DOCX ] [ Download PDF ]

-------------------------------------------------
Draft generated using AI.
Please have the document reviewed by a qualified
legal professional before relying on it.
-------------------------------------------------
```

---

# 36. Session State

Use Streamlit session state for:

```text
generated_document
edited_document
document_type
```

Example flow:

```text
User generates
      ↓
session_state.generated_document
      ↓
User edits
      ↓
session_state.edited_document
      ↓
Download
```

This prevents accidental loss of the generated document during Streamlit reruns.

---

# 37. Running the Application Locally

## Terminal 1 — Backend

From the project root:

```bash
uvicorn backend.main:app --reload --port 8000
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
http://127.0.0.1:8000/health
```

## Terminal 2 — Frontend

```bash
streamlit run frontend/app.py
```

Streamlit normally opens:

```text
http://localhost:8501
```

---

# 38. Complete Runtime Flow

```text
1. User opens Streamlit
            ↓
2. Selects document type
            ↓
3. Enters parties
            ↓
4. Enters terms
            ↓
5. Selects effective date
            ↓
6. Clicks Generate
            ↓
7. Streamlit validates input
            ↓
8. Streamlit sends POST /generate
            ↓
9. FastAPI receives request
            ↓
10. Pydantic validates request
            ↓
11. Prompt builder creates prompt
            ↓
12. Gemini API receives prompt
            ↓
13. Gemini generates legal draft
            ↓
14. Backend validates response
            ↓
15. FastAPI returns generated text
            ↓
16. Streamlit displays document
            ↓
17. User edits document
            ↓
18. User selects download format
            ↓
19. Formatter creates file
            ↓
20. Streamlit downloads file
```

---

# 39. Testing Strategy

Testing must cover each major component.

## Backend Tests

Test:

```text
GET /
GET /health
POST /generate
```

Check:

- Valid request
- Missing fields
- Empty fields
- Very large input
- Gemini failure
- Invalid API key

---

# 40. AI Generation Tests

Test multiple document types:

```text
Employment Contract
NDA
Lease Agreement
Freelance Agreement
Offer Letter
```

Verify:

- User information is included.
- Terms are included.
- Effective date is included.
- Document has logical sections.
- AI does not invent major user-specific information.
- Output is not empty.

---

# 41. Document Generator Tests

Test:

```text
TXT
DOCX
PDF
```

Verify:

- File is created.
- File opens correctly.
- Text is present.
- Formatting is present.
- Logo works when supplied.
- Missing logo does not crash the application.
- Long documents do not break formatting.

---

# 42. End-to-End Test

Perform:

```text
Open application
      ↓
Select NDA
      ↓
Enter parties
      ↓
Enter terms
      ↓
Select date
      ↓
Generate
      ↓
Read document
      ↓
Edit one clause
      ↓
Download TXT
      ↓
Download DOCX
      ↓
Download PDF
      ↓
Open all three
      ↓
Verify edited clause exists
```

---

# 43. Important Edge Cases

Test:

- Empty input
- One party
- Multiple parties
- Very long terms
- Special characters
- Indian currency symbol `₹`
- Dates
- Newlines
- Bullet points
- Unicode text
- Missing logo
- Gemini timeout
- Gemini API quota/rate-limit error
- Backend stopped
- Very long generated document

---

# 44. GitHub Repository

Create a **public GitHub repository**.

Recommended name:

```text
LegalEase-AI-Legal-Document-Generator
```

Do NOT upload:

```text
.env
venv/
API keys
passwords
private user documents
```

---

# 45. README.md

README should contain:

```text
Project Title
Project Description
Problem Statement
Objectives
Features
Technology Stack
System Architecture
Installation
Environment Setup
How to Run
API Endpoints
Screenshots
Sample Input
Sample Output
Testing
Team Members
Future Enhancements
Disclaimer
```

---

# 46. Required 8-Phase GitHub Structure

The project must be maintained phase-wise.

Create:

```text
docs/
│
├── 01-Brainstorming-Ideation/
├── 02-Requirement-Analysis/
├── 03-Project-Design/
├── 04-Project-Planning/
├── 05-Project-Development/
├── 06-Project-Testing/
├── 07-Project-Documentation/
└── 08-Project-Demonstration/
```

---

# 47. Phase 1 — Brainstorming & Ideation

Include:

```text
Project title
Problem identification
Why the problem matters
Proposed solution
Target users
Possible features
Initial technology ideas
Expected benefits
```

For LegalEase:

```text
Problem:
Creating basic legal documents can be time-consuming for
users who do not know how to structure them.

Solution:
Use Generative AI to create customizable draft legal
documents from structured user inputs.
```

---

# 48. Phase 2 — Requirement Analysis

Create:

## Functional Requirements

```text
FR1: User can select document type.
FR2: User can enter parties.
FR3: User can enter terms.
FR4: User can specify effective date.
FR5: System generates document using AI.
FR6: User can preview document.
FR7: User can edit document.
FR8: User can download TXT.
FR9: User can download DOCX.
FR10: User can download PDF.
```

## Non-Functional Requirements

```text
NFR1: Secure API key handling.
NFR2: Responsive UI.
NFR3: Reasonable generation latency.
NFR4: Reliable document generation.
NFR5: Clear error handling.
NFR6: Maintainable architecture.
```

---

# 49. Phase 3 — Project Design

Include:

## System Architecture

```text
Streamlit
    ↓
FastAPI
    ↓
Prompt Builder
    ↓
Gemini
    ↓
Generated Document
    ↓
Document Formatter
    ↓
TXT / DOCX / PDF
```

## Use Case Diagram

Actors:

```text
User
```

Use cases:

```text
Select document
Enter information
Generate document
Preview document
Edit document
Download document
```

## Data Flow Diagram

```text
User
 ↓
Frontend
 ↓
Backend
 ↓
AI Model
 ↓
Generated Content
 ↓
Frontend
 ↓
Export
```

---

# 50. Phase 4 — Project Planning

Create a timeline such as:

```text
Task                         Status
------------------------------------------------
Environment setup            Pending
Project structure            Pending
Gemini integration           Pending
FastAPI backend              Pending
Streamlit frontend           Pending
Prompt engineering           Pending
TXT generation               Pending
DOCX generation              Pending
PDF generation               Pending
Editing functionality        Pending
Testing                      Pending
Documentation                Pending
Demo                         Pending
```

For a team, assign:

```text
Member 1 — Backend/API
Member 2 — AI/Prompt Engineering
Member 3 — Frontend
Member 4 — Document Generation/Testing
Member 5 — Documentation/Deployment
```

The exact assignment can be changed according to the team's actual work.

---

# 51. Phase 5 — Project Development

Include:

- Source code
- Screenshots
- API implementation
- Gemini integration
- Frontend implementation
- Document generation
- Feature implementation notes

Recommended Git commits:

```text
Initial project setup
Add FastAPI backend
Add Gemini integration
Add document generation
Add Streamlit frontend
Add document editing
Add DOCX export
Add PDF export
Add TXT export
Add validation
Add error handling
Add tests
```

---

# 52. Phase 6 — Project Testing

Include:

## Test Case Table

```text
Test ID | Input | Expected Result | Actual Result | Status
```

Example:

```text
TC01
Input: NDA + parties + terms
Expected: NDA generated
Actual: NDA generated
Status: PASS
```

Test:

- Backend
- AI generation
- Frontend
- Export
- Error handling
- Edge cases

---

# 53. Phase 7 — Project Documentation

Include:

```text
Project Overview
Problem Statement
Objectives
Architecture
Technology Stack
Installation
Configuration
API Documentation
Frontend Documentation
AI Prompt Flow
Document Generation
Testing
Limitations
Security
Future Scope
Conclusion
```

---

# 54. Phase 8 — Project Demonstration

Record a complete demo video.

The video should show:

1. Project name
2. Purpose
3. Benefits
4. Application execution
5. User entering data
6. AI generation
7. Generated document
8. Editing
9. TXT download
10. DOCX download
11. PDF download
12. Final output

The video should contain:

- Screen recording
- Student voice-over
- Project explanation
- Final output

Upload the video to Google Drive and ensure:

```text
Anyone with the link → Viewer
```

---

# 55. Demo Script

Use this structure:

## Introduction

```text
Hello, this is our project LegalEase,
an AI-powered legal document generation system.

The purpose of this project is to help users
generate structured draft legal documents by
providing their requirements through a simple interface.
```

## Problem

```text
Creating a structured legal document manually
can require significant time and knowledge of
document structure.
```

## Solution

```text
LegalEase allows the user to select a document type,
provide the parties, terms and effective date,
and uses Generative AI to create a structured draft.
```

## Technology

```text
The frontend is developed using Streamlit.
The backend is developed using FastAPI.
Gemini is used for AI-based document generation.
Python-docx is used for Word documents and
FPDF is used for PDF generation.
```

## Demo

```text
I will now demonstrate the complete workflow.
```

Then show:

```text
Input
→ Generate
→ Preview
→ Edit
→ Download
```

## Conclusion

```text
The final system provides an end-to-end workflow
for generating, editing and exporting AI-assisted
draft legal documents.
```

---

# 56. Deployment Preparation

For initial submission, local execution is sufficient if that is what the instructor requires.

For future deployment:

```text
Frontend → Streamlit Community Cloud
Backend  → Render / Railway / VPS / other suitable platform
```

Deployment must be evaluated separately because:

- Gemini API key must be stored securely.
- Backend URL must be configurable.
- CORS may need configuration.
- File generation must work in the deployment environment.

---

# 57. Production Configuration

Never use:

```python
API_KEY = "AIza..."
```

Use:

```text
.env
```

and environment variables.

Example:

```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL")
```

---

# 58. What NOT to Build Initially

Do not unnecessarily add:

```text
LangChain
RAG
FAISS
Vector database
Authentication
Payment gateway
Microservices
Kubernetes
Docker
Complex database
```

unless the team specifically decides they are needed.

The first objective is to make the core flow work:

```text
INPUT
  ↓
GEMINI
  ↓
COMPLETE LEGAL DRAFT
  ↓
EDIT
  ↓
TXT/DOCX/PDF
```

---

# 59. Final Definition of Done

The project is considered complete when:

- [ ] Python environment works
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Gemini API configured
- [ ] FastAPI starts successfully
- [ ] `/health` works
- [ ] `/generate` works
- [ ] Pydantic validation works
- [ ] Prompt builder works
- [ ] Gemini generates complete documents
- [ ] Streamlit frontend works
- [ ] User can select document type
- [ ] User can enter parties
- [ ] User can enter terms
- [ ] User can select date
- [ ] User can generate document
- [ ] User can edit document
- [ ] TXT download works
- [ ] DOCX download works
- [ ] PDF download works
- [ ] Logo works
- [ ] Footer works
- [ ] Error handling works
- [ ] Edge cases tested
- [ ] README completed
- [ ] 8 project phases documented
- [ ] GitHub repository is public
- [ ] Demo video recorded
- [ ] Demo video uploaded to Google Drive
- [ ] Google Drive sharing is public
- [ ] Final demonstration completed

---

# 60. AI Coding Assistant Instructions

When implementing this project, follow these rules:

1. Build the project incrementally.
2. Do not generate the entire application blindly in one step.
3. First create the folder structure and environment setup.
4. Then implement the FastAPI backend.
5. Then implement Gemini integration.
6. Test `/health`.
7. Test `/generate` independently using Swagger/Postman/curl.
8. Then implement Streamlit.
9. Connect Streamlit to FastAPI.
10. Implement editing.
11. Implement TXT export.
12. Implement DOCX export.
13. Implement PDF export.
14. Add validation and error handling.
15. Add tests.
16. Improve UI only after core functionality works.
17. Keep API keys in environment variables.
18. Do not expose secrets.
19. Keep Gemini-specific code inside the AI module.
20. Keep document-formatting logic separate from API routes.
21. Use clear, modular Python code.
22. Do not introduce unnecessary frameworks.
23. Preserve the architecture defined in this document.
24. If an implementation detail is not specified, choose the simplest maintainable solution.
25. Before changing architecture, explain why the change is necessary.

---

# 61. Final Architecture Summary

```text
                         LEGAL EASE
                             |
             +---------------+---------------+
             |                               |
             v                               v
        STREAMLIT                         FASTAPI
        FRONTEND                          BACKEND
             |                               |
             |                         Pydantic Validation
             |                               |
             |                               v
             |                         Prompt Builder
             |                               |
             |                               v
             |                         Gemini API
             |                               |
             |                               v
             |                      Generated Legal Draft
             |                               |
             +<------------------------------+
             |
             v
       Editable Preview
             |
             v
       Final Edited Text
             |
      +------+-------+
      |      |       |
      v      v       v
     TXT    DOCX    PDF
```

---

# 62. One-Line Project Explanation

**LegalEase is a Streamlit + FastAPI + Gemini application that takes structured legal requirements from a user, generates a complete AI-assisted legal document, allows the user to edit it, and exports the final content as TXT, DOCX, or PDF.**


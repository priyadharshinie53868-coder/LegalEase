# Phase 8 — Project Demonstration & Video Script

## 1. Demonstration Outline

1. **Introduction (0:00 - 0:30):**
   - Introduce project title: *LegalEase — AI-Powered Legal Document Generator*.
   - Present the problem: Standard drafting is slow, complex, and expensive.
   - Introduce the solution: An automated, customizable draft generator powered by FastAPI, Streamlit, and Google Gemini AI.

2. **Architecture & Tech Stack (0:30 - 1:00):**
   - **Frontend:** Streamlit with live reactive session state.
   - **Backend:** FastAPI with Pydantic request validation and CORS.
   - **AI Core:** Google Gemini (`gemini-2.5-flash` / `gemini-1.5-flash`).
   - **Document Generation:** `python-docx` for Word, `fpdf2` for PDF, native UTF-8 for TXT.

3. **Live Demonstration (1:00 - 3:00):**
   - Show FastAPI backend running on `http://127.0.0.1:8000/docs`.
   - Launch Streamlit frontend on `http://localhost:8501`.
   - Select a sample preset (e.g. *Employment Contract* or *Mutual NDA*).
   - Click **"🚀 Generate Document"** and observe live AI drafting.
   - Edit a clause in the live editor (e.g. modifying the notice period or salary).
   - Demonstrate downloads:
     - Download and open `.txt`.
     - Download and open `.docx` (show logo, headings, and footer).
     - Download and open `.pdf` (show clean formatting, pagination, and disclaimer).

4. **Conclusion & Legal Disclaimer (3:00 - 3:30):**
   - Highlight the safety disclaimer and future expansion roadmap.

## 2. Demonstration Video Link
- **Google Drive Link:** `[Insert Public Google Drive Link Here — Set to Anyone with the link → Viewer]`

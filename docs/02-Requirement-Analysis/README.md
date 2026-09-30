# Phase 2 — Requirement Analysis

## 1. Functional Requirements (FR)

- **FR1 (Document Selection):** The system shall allow users to select from a predefined list of legal document types (Employment Contract, NDA, Lease Agreement, Service Agreement, Freelance Contract, Offer Letter, General Agreement) or specify a custom document type.
- **FR2 (Party Specification):** The system shall collect complete information regarding the parties involved (e.g., names, roles, entity names).
- **FR3 (Terms & Covenants):** The system shall collect key terms, compensation, deliverables, notice periods, and covenants.
- **FR4 (Effective Date):** The system shall allow selection and formatting of the agreement effective date.
- **FR5 (AI Generation):** The backend shall build a structured prompt and invoke the Google Gemini API to generate a draft contract.
- **FR6 (Preview & Edit):** The frontend shall present the generated draft in an interactive, editable editor retaining modifications.
- **FR7 (Multi-Format Export):** The system shall provide one-click file generation and download for:
  - Plain Text (`.txt`)
  - Microsoft Word Document (`.docx`) with headers, footer, and styling
  - Portable Document Format (`.pdf`) with page numbers and logo
- **FR8 (Legal Disclaimer):** The system shall explicitly display a legal disclaimer on the interface and exported files.

## 2. Non-Functional Requirements (NFR)

- **NFR1 (Security & Privacy):** API keys must be securely stored in environment variables (`.env`) and never exposed in the frontend or version control.
- **NFR2 (Reliability & Fallbacks):** The AI module must handle rate limits, timeouts, and missing assets (e.g., logo) gracefully without crashing.
- **NFR3 (Performance & Latency):** AI generation requests should complete within 3–8 seconds under standard network conditions.
- **NFR4 (Usability & Responsiveness):** The UI must be modern, clean, responsive, and provide visual progress spinners during generation.
- **NFR5 (Code Maintainability):** Clean separation of concerns between API routing, AI prompt orchestration, document rendering, and user interface.

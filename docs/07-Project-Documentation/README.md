# Phase 7 — Project Documentation

## 1. System Overview
**LegalEase** is an AI-driven legal document generator designed to streamline the preliminary contract drafting workflow. It utilizes a micro-architecture composed of a FastAPI backend and a Streamlit frontend, communicating over HTTP REST protocols.

## 2. API Endpoints Reference

### `GET /`
- **Description:** Returns API status, health link, and interactive Swagger docs URL.
- **Response:**
  ```json
  {
    "app": "LegalEase API",
    "description": "AI-Powered Legal Document Generator Backend",
    "docs": "/docs",
    "health": "/health"
  }
  ```

### `GET /health`
- **Description:** Health check probe for monitoring services.
- **Response:**
  ```json
  {
    "status": "ok",
    "message": "LegalEase API backend is healthy and operational.",
    "version": "1.0.0"
  }
  ```

### `POST /generate`
- **Description:** Generates a draft legal document using the Gemini AI core.
- **Request Body:**
  ```json
  {
    "document_type": "Employment Contract",
    "parties": "Tech Corp (Employer) and Jane Doe (Employee)",
    "terms": "Salary: ₹12 LPA, Notice Period: 30 days",
    "effective_date": "2026-10-01",
    "additional_details": "Full-time software engineering role"
  }
  ```
- **Response Body:**
  ```json
  {
    "success": true,
    "document_type": "Employment Contract",
    "content": "# EMPLOYMENT AGREEMENT\n\n...",
    "error": null
  }
  ```

## 3. Configuration & Security
- **API Keys:** Defined in `.env` (`GEMINI_API_KEY`) and parsed at startup.
- **Data Protection:** No personal contract data is persisted to disk or databases without user consent.
- **Disclaimer:** All generated drafts feature prominent disclaimers advising review by qualified legal counsel.

# Phase 6 — Project Testing & Quality Assurance

## 1. Test Matrix & Results

| Test ID | Module / Feature | Test Description | Expected Result | Status |
| :---: | :--- | :--- | :--- | :---: |
| **TC01** | Backend Root (`/`) | Send `GET /` to verify API availability | HTTP 200 with app metadata | ✅ PASS |
| **TC02** | Health Endpoint (`/health`) | Send `GET /health` to verify server status | HTTP 200 with `status: ok` | ✅ PASS |
| **TC03** | Schema Validation | Send `POST /generate` with empty `parties` | HTTP 400/422 validation error | ✅ PASS |
| **TC04** | Prompt Builder | Build prompt for "Employment Contract" | Prompt contains all standard clauses and parties | ✅ PASS |
| **TC05** | Prompt Builder (NDA) | Build prompt for "NDA" | Prompt contains confidentiality definitions & terms | ✅ PASS |
| **TC06** | TXT Export | Generate `.txt` document from text | Valid UTF-8 encoded bytes returned | ✅ PASS |
| **TC07** | DOCX Export | Generate `.docx` document from text | Valid Word archive created with styles | ✅ PASS |
| **TC08** | PDF Export | Generate `.pdf` document from text | Valid `%PDF-` document created with pagination | ✅ PASS |
| **TC09** | Missing Logo Resilience | Generate DOCX/PDF when logo is absent | Document generates cleanly without crashing | ✅ PASS |
| **TC10** | Unicode Sanitization | Include Indian Rupee symbol `₹`, curly quotes, and dashes | Characters cleanly converted without encoding errors | ✅ PASS |
| **TC11** | Streamlit State Sync | Edit text in Streamlit and click Download | Downloaded files contain the latest edited text | ✅ PASS |

## 2. Running Automated Tests

Execute the test suite using `pytest`:

```bash
pytest tests/ -v
```

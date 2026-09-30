import pytest
from document_generators.txt_generator import generate_txt
from document_generators.docx_generator import generate_docx
from document_generators.pdf_generator import generate_pdf

SAMPLE_CONTRACT_TEXT = """# EMPLOYMENT AGREEMENT

This Employment Agreement is entered into on 2026-10-01 by and between Acme Corp and Jane Doe.

## 1. POSITION AND DUTIES
The Employee shall serve in the capacity of Senior Engineer and perform all duties assigned.

## 2. COMPENSATION AND BENEFITS
- Base Salary: ₹15,00,000 per annum
- Performance Bonus: Eligible for annual appraisal
- Working Hours: 40 hours per week

## 3. TERMINATION AND NOTICE
Either party may terminate this agreement with a 30-day prior written notice.

## 4. GOVERNING LAW
This agreement shall be governed by the laws of India.

IN WITNESS WHEREOF, the parties have executed this Agreement.

For Acme Corp:
______________________
Authorized Signatory

For Jane Doe:
______________________
Employee Signature
"""


def test_txt_generation():
    txt_bytes = generate_txt(SAMPLE_CONTRACT_TEXT)
    assert isinstance(txt_bytes, bytes)
    assert len(txt_bytes) > 0
    decoded = txt_bytes.decode("utf-8")
    assert "EMPLOYMENT AGREEMENT" in decoded
    assert "Acme Corp" in decoded


def test_docx_generation():
    docx_bytes = generate_docx(SAMPLE_CONTRACT_TEXT, logo_path="non_existent_logo.png")
    assert isinstance(docx_bytes, bytes)
    assert len(docx_bytes) > 1000  # A valid .docx file is a zip container and > 1KB


def test_pdf_generation():
    pdf_bytes = generate_pdf(SAMPLE_CONTRACT_TEXT, logo_path="non_existent_logo.png")
    assert isinstance(pdf_bytes, bytes)
    assert len(pdf_bytes) > 500
    assert pdf_bytes.startswith(b"%PDF-")

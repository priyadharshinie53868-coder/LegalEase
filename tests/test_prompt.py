import pytest
from backend.ai_core.prompt_builder import build_legal_prompt, DOCUMENT_SPECIFIC_INSTRUCTIONS


def test_build_legal_prompt_employment():
    prompt = build_legal_prompt(
        document_type="Employment Contract",
        parties="Tech Innovations Ltd and John Doe",
        terms="Salary: ₹12 LPA, Notice Period: 30 Days",
        effective_date="2026-10-01",
        additional_details="Standard IP assignment"
    )
    assert "Tech Innovations Ltd and John Doe" in prompt
    assert "Employment Contract" in prompt
    assert "Salary: ₹12 LPA" in prompt
    assert "2026-10-01" in prompt
    assert "Standard IP assignment" in prompt
    assert "COMPENSATION" in prompt


def test_build_legal_prompt_nda():
    prompt = build_legal_prompt(
        document_type="NDA",
        parties="Company A and Company B",
        terms="Duration: 2 years, Mutual confidentiality",
        effective_date="2026-11-01"
    )
    assert "Company A and Company B" in prompt
    assert "DEFINITION OF CONFIDENTIAL INFORMATION" in prompt
    assert "2026-11-01" in prompt


def test_all_standard_document_types_have_instructions():
    expected_types = [
        "Employment Contract",
        "NDA",
        "Lease Agreement",
        "Service Agreement",
        "Freelance Contract",
        "Offer Letter",
        "General Agreement",
    ]
    for doc_type in expected_types:
        assert doc_type in DOCUMENT_SPECIFIC_INSTRUCTIONS

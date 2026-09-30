import pytest
from backend.utils.history_manager import (
    save_document_to_history,
    get_all_history,
    get_history_by_id,
    delete_history_by_id,
    clear_all_history
)
from backend.utils.summary_utils import extract_executive_summary


def test_save_and_retrieve_history():
    clear_all_history()
    doc = save_document_to_history(
        document_type="NDA",
        parties="Alpha Corp and Beta LLC",
        terms="Mutual confidentiality for 2 years",
        dates="2026-10-01",
        content="# NON DISCLOSURE AGREEMENT\n\nThis agreement is governed by the laws of California."
    )
    assert doc is not None
    assert doc["document_type"] == "NDA"
    assert doc["id"] is not None

    all_docs = get_all_history()
    assert len(all_docs) >= 1
    assert all_docs[0]["id"] == doc["id"]

    fetched = get_history_by_id(doc["id"])
    assert fetched is not None
    assert fetched["parties"] == "Alpha Corp and Beta LLC"

    # Test delete
    deleted = delete_history_by_id(doc["id"])
    assert deleted is True
    assert get_history_by_id(doc["id"]) is None


def test_executive_summary_extraction():
    sample_text = """
# FREELANCE AGREEMENT
This agreement is governed by the laws of India.
Either party may terminate with 30 days written notice.
Please deposit to account [Insert Bank Details].
"""
    summary = extract_executive_summary(
        sample_text,
        doc_type="Freelance Contract",
        parties="Jane Doe and TechNova",
        dates="April 15, 2025"
    )
    assert summary["document_type"] == "Freelance Contract"
    assert "India" in summary["governing_law"]
    assert "30 days" in summary["notice_period"]
    assert any("[Insert Bank Details]" in cp for cp in summary["review_checkpoints"])

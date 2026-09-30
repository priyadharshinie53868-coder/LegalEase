from typing import Tuple
from backend.schemas import DocumentRequest


def validate_document_request(req: DocumentRequest) -> Tuple[bool, str]:
    """
    Validates the DocumentRequest data.
    Returns (is_valid, error_message).
    """
    if not req.document_type or not req.document_type.strip():
        return False, "Document type is required."

    if not req.parties or not req.parties.strip():
        return False, "Parties involved are required."

    if len(req.parties.strip()) < 3:
        return False, "Please provide complete details of the parties involved."

    if not req.terms or not req.terms.strip():
        return False, "Document terms and conditions are required."

    if len(req.terms.strip()) < 5:
        return False, "Terms description is too brief. Please provide key clauses or terms."

    date_str = req.effective_date or req.dates
    if not date_str or not date_str.strip():
        return False, "Effective date is required."

    return True, ""

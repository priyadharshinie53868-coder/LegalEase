import re
from typing import Dict, List


def extract_executive_summary(content: str, doc_type: str, parties: str, dates: str) -> Dict:
    """
    Extracts high-level executive insights, governance, and review checkpoints from the generated draft.
    """
    summary = {
        "document_type": doc_type,
        "parties": parties,
        "effective_date": dates,
        "governing_law": "Standard Legal Jurisdiction",
        "notice_period": "Not specified / Discretionary",
        "review_checkpoints": []
    }

    # Extract Governing Law
    gov_match = re.search(r"governed by.*?laws of\s+([A-Za-z\s,\[\]]+)(?:\.|\;|\n)", content, re.IGNORECASE)
    if gov_match:
        summary["governing_law"] = gov_match.group(1).strip()

    # Extract Notice Period
    notice_match = re.search(r"(\d+[\s-]*(?:days?|weeks?|months?)\s+(?:prior\s+)?written\s+notice)", content, re.IGNORECASE)
    if notice_match:
        summary["notice_period"] = notice_match.group(1).strip()

    # Find bracketed placeholders needing attention [Insert ...]
    placeholders = re.findall(r"(\[[A-Za-z0-9\s,/\.\-_]+\])", content)
    unique_placeholders = list(dict.fromkeys(placeholders))[:8]  # top 8 distinct

    checkpoints = []
    if unique_placeholders:
        for ph in unique_placeholders:
            checkpoints.append(f"Fill in missing detail: `{ph}`")
    else:
        checkpoints.append("All primary placeholders populated.")

    checkpoints.append("Verify dispute resolution jurisdiction matches both parties' agreed venue.")
    checkpoints.append("Have legal counsel confirm statutory compliance with local labor/contract laws.")

    summary["review_checkpoints"] = checkpoints
    return summary

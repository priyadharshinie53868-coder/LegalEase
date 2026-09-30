import os
import json
import uuid
import datetime
from typing import List, Dict, Optional

HISTORY_DIR = "data"
HISTORY_FILE = os.path.join(HISTORY_DIR, "history.json")


def _ensure_history_file():
    os.makedirs(HISTORY_DIR, exist_ok=True)
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)


def save_document_to_history(
    document_type: str,
    parties: str,
    terms: str,
    dates: str,
    content: str,
    additional_details: Optional[str] = None
) -> Dict:
    """
    Saves a generated legal document draft to the local history archive.
    """
    _ensure_history_file()

    words = len(content.split())
    chars = len(content)

    doc_record = {
        "id": str(uuid.uuid4())[:8],
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "document_type": document_type,
        "parties": parties,
        "terms": terms,
        "dates": dates,
        "additional_details": additional_details or "",
        "content": content,
        "word_count": words,
        "char_count": chars,
    }

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
    except Exception:
        history = []

    # Prepend newest record
    history.insert(0, doc_record)

    # Keep maximum 50 records
    history = history[:50]

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

    return doc_record


def get_all_history() -> List[Dict]:
    """Returns all saved document drafts sorted by newest first."""
    _ensure_history_file()
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def get_history_by_id(doc_id: str) -> Optional[Dict]:
    """Retrieves a specific document from history by ID."""
    history = get_all_history()
    for item in history:
        if item.get("id") == doc_id:
            return item
    return None


def delete_history_by_id(doc_id: str) -> bool:
    """Deletes a document from history by ID."""
    _ensure_history_file()
    history = get_all_history()
    initial_len = len(history)
    history = [item for item in history if item.get("id") != doc_id]

    if len(history) < initial_len:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
        return True
    return False


def clear_all_history() -> bool:
    """Clears all stored history."""
    _ensure_history_file()
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)
    return True

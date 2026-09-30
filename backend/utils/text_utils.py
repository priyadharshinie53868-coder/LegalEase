import re


def clean_markdown_fences(text: str) -> str:
    """
    Strips markdown code block markers (e.g., ```markdown ... ``` or ```text ... ```)
    if the AI returned the document wrapped in a code fence.
    """
    if not text:
        return ""

    stripped = text.strip()
    pattern = r"^```(?:markdown|text|plain)?\s*\n([\s\S]*?)\n```$"
    match = re.match(pattern, stripped, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    if stripped.startswith("```markdown") or stripped.startswith("```text") or stripped.startswith("```"):
        stripped = re.sub(r"^```[a-zA-Z]*\n?", "", stripped)
    if stripped.endswith("```"):
        stripped = re.sub(r"\n?```$", "", stripped)

    return stripped.strip()


def strip_html_tags(text: str) -> str:
    """
    Converts HTML tags (like <br>, <p>, <b>, <center>) into clean text/newlines.
    Prevents HTML tags from leaking into PDF, DOCX, and TXT files.
    """
    if not text:
        return ""
    # Convert breaks and paragraph closings to newlines
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'</p\s*>', '\n', text, flags=re.IGNORECASE)
    # Strip any other tags (e.g. <b>, </b>, <center>, </center>, <div>, etc.)
    text = re.sub(r'<[^>]+>', '', text)
    return text


def sanitize_document_text(text: str) -> str:
    """
    Cleans raw document text: strips code fences, strips HTML tags,
    normalizes line breaks, and handles special control characters.
    """
    if not text:
        return ""

    cleaned = clean_markdown_fences(text)
    cleaned = strip_html_tags(cleaned)

    # Normalize Windows CRLF to standard LF
    cleaned = cleaned.replace("\r\n", "\n").replace("\r", "\n")
    # Replace non-breaking spaces
    cleaned = cleaned.replace("\u00a0", " ")
    # Replace special typographic single/double quotes
    cleaned = cleaned.replace("“", '"').replace("”", '"')
    cleaned = cleaned.replace("‘", "'").replace("’", "'")
    # Remove null bytes or non-printable ASCII
    cleaned = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", cleaned)

    return cleaned.strip()

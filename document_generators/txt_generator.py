import io


def generate_txt(content: str) -> bytes:
    """
    Generates plain text bytes for the legal document.
    """
    if not content:
        content = ""
    return content.encode("utf-8")


def generate_txt_buffer(content: str) -> io.BytesIO:
    """
    Returns an in-memory BytesIO buffer containing the UTF-8 text document.
    """
    return io.BytesIO(generate_txt(content))

import os
import sys
import re
import datetime

# Ensure project root is in sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st

try:
    from document_generators.txt_generator import generate_txt
    from document_generators.docx_generator import format_docx
    from document_generators.pdf_generator import format_pdf
except ImportError:
    from txt_generator import generate_txt
    from docx_generator import format_docx
    from pdf_generator import format_pdf


def sanitize_filename(name: str) -> str:
    """Creates a clean, safe filename."""
    clean = re.sub(r"[^\w\-_]", "_", name.strip().lower())
    return clean or "legal_document"


def format_html_preview(text: str) -> str:
    """Converts output to styled HTML blocks for inline display in dark mode matching reference PDF."""
    escaped_text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    formatted_html = escaped_text.replace("\n", "<br>")
    return f"""
    <div style="background-color: #0f172a; color: #e2e8f0; padding: 24px; border-radius: 8px; border: 1px solid #334155; font-family: 'Times New Roman', serif; font-size: 1.05rem; line-height: 1.7; max-height: 520px; overflow-y: auto;">
        {formatted_html}
    </div>
    """


def render_document_editor():
    """
    Renders the generated document preview, 'Click to Edit Document' inline editor,
    and download buttons exactly as specified in the reference PDF (pages 20-23).
    """
    if "generated_document" not in st.session_state or not st.session_state.generated_document:
        return

    doc_type = st.session_state.get("document_type", "Legal Document")
    base_filename = sanitize_filename(doc_type)

    st.markdown("---")
    
    # 1. Dark Theme Preview Box (Pages 20-21)
    st.markdown("### Document Generated")
    preview_html = format_html_preview(st.session_state.get("edited_document", st.session_state.generated_document))
    st.markdown(preview_html, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. 'Click to Edit Document' Toggle & Inline Editor (Pages 20-21)
    show_edit = st.checkbox("🖊️ Click to Edit Document", value=st.session_state.get("show_edit", False))
    st.session_state.show_edit = show_edit

    if show_edit:
        st.markdown("#### Edit Document Below:")
        edited_text = st.text_area(
            "Edit Document Below:",
            value=st.session_state.get("edited_document", st.session_state.generated_document),
            height=320,
            label_visibility="collapsed",
            help="Directly modify any section or clause. The latest edits are exported in all downloads."
        )
        st.session_state.edited_document = edited_text

    final_content = st.session_state.get("edited_document", st.session_state.generated_document)

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. Download Buttons (Pages 21-23)
    st.markdown("### Downloading / Saving the Generated Document")
    col1, col2, col3 = st.columns(3)

    # 1. TXT Export
    with col1:
        txt_bytes = generate_txt(final_content)
        st.download_button(
            label="📄 Download as .TXT",
            data=txt_bytes,
            file_name=f"{base_filename}.txt",
            mime="text/plain",
            use_container_width=True
        )

    # 2. DOCX Export
    with col2:
        try:
            docx_bytes = format_docx(final_content, doc_type=doc_type, logo_path="assets/logo.png")
            st.download_button(
                label="📘 Download as .DOCX",
                data=docx_bytes,
                file_name=f"{base_filename}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"DOCX Error: {e}")

    # 3. PDF Export
    with col3:
        try:
            pdf_bytes = format_pdf(final_content, doc_type=doc_type, logo_path="assets/logo.png")
            st.download_button(
                label="📕 Download as .PDF",
                data=pdf_bytes,
                file_name=f"{base_filename}.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"PDF Error: {e}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.info(
        "⚖️ **Legal Disclaimer:** This draft document was generated using AI. "
        "Please have the document reviewed by a qualified legal professional before relying on it."
    )

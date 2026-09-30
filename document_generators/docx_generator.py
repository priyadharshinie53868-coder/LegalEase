import os
import io
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH


def format_docx(content: str, doc_type: str = "Legal Document", logo_path: str = "assets/logo.png") -> bytes:
    """
    Formats and generates a professional Word (.docx) document from legal text.
    Matches Milestone 2 & 4 specifications from the LegalEase guide.
    """
    doc = Document()

    # Configure Margins (1 inch all around)
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
        
        # Add footer matching reference PDF
        footer = section.footer
        f_p = footer.paragraphs[0]
        f_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        f_run = f_p.add_run("LegalEase Inc. | contact@legalease.com | All Rights Reserved. (Draft - Subject to Legal Review)")
        f_run.font.name = "Times New Roman"
        f_run.font.size = Pt(8.5)
        f_run.font.italic = True
        f_run.font.color.rgb = RGBColor(128, 128, 128)

    # Base styling
    normal_style = doc.styles["Normal"]
    normal_font = normal_style.font
    normal_font.name = "Times New Roman"
    normal_font.size = Pt(11)
    normal_font.color.rgb = RGBColor(30, 30, 30)

    # 1. Insert Logo if available
    if logo_path and os.path.exists(logo_path):
        try:
            logo_p = doc.add_paragraph()
            logo_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            logo_p.paragraph_format.space_after = Pt(12)
            logo_run = logo_p.add_run()
            logo_run.add_picture(logo_path, width=Inches(1.8))
        except Exception:
            pass

    # 2. Parse and format document lines
    # Strip HTML tags
    cleaned_content = re.sub(r'<br\s*/?>', '\n', content, flags=re.IGNORECASE)
    cleaned_content = re.sub(r'</p\s*>', '\n', cleaned_content, flags=re.IGNORECASE)
    cleaned_content = re.sub(r'<[^>]+>', '', cleaned_content)

    lines = cleaned_content.split("\n")
    is_first_heading = True

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Detect Main Title / Heading 1
        if stripped.startswith("# ") or (is_first_heading and (stripped.isupper() or len(stripped) < 60 and ("AGREEMENT" in stripped or "CONTRACT" in stripped or "LETTER" in stripped))):
            clean_title = stripped.lstrip("#").strip()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(14)
            run = p.add_run(clean_title)
            run.font.name = "Times New Roman"
            run.font.size = Pt(15)
            run.font.bold = True
            run.font.color.rgb = RGBColor(15, 23, 42)
            is_first_heading = False

        # Detect Section Heading (e.g. ## Heading or "1. DEFINITIONS", "SECTION 1", etc.)
        elif stripped.startswith("## ") or re.match(r"^(\d+\.|\bSECTION\b|\bARTICLE\b|\bCLAUSE\b)\s+[A-Z]", stripped, re.IGNORECASE):
            clean_h = stripped.lstrip("#").strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            run = p.add_run(clean_h)
            run.font.name = "Times New Roman"
            run.font.size = Pt(12)
            run.font.bold = True
            run.font.color.rgb = RGBColor(30, 41, 59)

        # Detect Subheadings (### Subheading)
        elif stripped.startswith("### "):
            clean_sub = stripped.lstrip("#").strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            run = p.add_run(clean_sub)
            run.font.name = "Times New Roman"
            run.font.size = Pt(11)
            run.font.bold = True

        # Detect Bullet points
        elif stripped.startswith("- ") or stripped.startswith("* ") or stripped.startswith("• "):
            clean_bullet = stripped[2:].strip()
            p = doc.add_paragraph(style="List Bullet")
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            run = p.add_run(clean_bullet)
            run.font.name = "Times New Roman"
            run.font.size = Pt(11)

        # Standard Paragraph
        else:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.line_spacing = 1.15
            run = p.add_run(stripped)
            run.font.name = "Times New Roman"
            run.font.size = Pt(11)

    # Save to buffer
    doc_buffer = io.BytesIO()
    doc.save(doc_buffer)
    doc_buffer.seek(0)
    return doc_buffer.getvalue()


def generate_docx(content: str, logo_path: str = "assets/logo.png", title: str = "LEGAL AGREEMENT") -> bytes:
    return format_docx(content, title, logo_path)


def generate_docx_buffer(content: str, logo_path: str = "assets/logo.png", title: str = "LEGAL AGREEMENT") -> io.BytesIO:
    return io.BytesIO(format_docx(content, title, logo_path))

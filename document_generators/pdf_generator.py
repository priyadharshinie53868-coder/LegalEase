import os
import io
import re
from fpdf import FPDF


class LegalPDF(FPDF):
    def __init__(self, logo_path: str = "assets/logo.png", title_text: str = "LEGAL DOCUMENT"):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.logo_path = logo_path
        self.title_text = title_text
        self.set_auto_page_break(auto=True, margin=22)
        self.set_margins(left=20, top=18, right=20)

    def header(self):
        if self.page_no() == 1:
            # First page letterhead logo
            if self.logo_path and os.path.exists(self.logo_path):
                try:
                    # Centered logo: page width is 210mm; logo width is 56mm -> x = (210 - 56) / 2 = 77mm
                    self.image(self.logo_path, x=77, y=14, w=56)
                    self.set_y(34)
                except Exception:
                    self.ln(6)
            else:
                self.ln(6)
        else:
            # Subsequent pages running header
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 6, "LegalEase - AI-Generated Legal Document Draft", align="R", ln=True)
            self.set_draw_color(210, 215, 225)
            self.line(20, 16, 190, 16)
            self.ln(4)

    def footer(self):
        self.set_y(-14)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        footer_text = f"LegalEase Inc. | contact@legalease.com | All Rights Reserved. | Page {self.page_no()}/{{nb}}"
        self.cell(0, 10, clean_pdf_text(footer_text), align="C")


def clean_pdf_text(text: str) -> str:
    """
    Sanitizes text for standard PDF encoding.
    Strips raw HTML tags and converts markdown formatting to clean plain text.
    """
    if not text:
        return ""

    # Strip HTML tags
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'</p\s*>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text)

    # Strip markdown bold/italic asterisks for clean PDF rendering
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)

    replacements = {
        "₹": "Rs. ",
        "–": "-",
        "—": " - ",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "•": "-",
        "·": "-",
        "…": "...",
        "\u2022": "-",
        "\u2013": "-",
        "\u2014": " - ",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u200b": "",
        "\u00a0": " ",
    }
    for char, rep in replacements.items():
        text = text.replace(char, rep)

    return text.encode("latin-1", "replace").decode("latin-1")



def format_pdf(content: str, doc_type: str = "Legal Document", logo_path: str = "assets/logo.png") -> bytes:
    """
    Formats and generates a professional PDF byte stream.
    Places the logo at the top center of page 1 as a formal letterhead.
    """
    pdf = LegalPDF(logo_path=logo_path, title_text=doc_type)
    pdf.alias_nb_pages()
    pdf.add_page()

    lines = content.split("\n")
    is_first_heading = True

    for line in lines:
        raw_line = line.strip()
        if not raw_line:
            pdf.ln(3)
            continue

        clean_line = clean_pdf_text(raw_line)

        # Main Title (e.g. # TITLE)
        if raw_line.startswith("# ") or (is_first_heading and (raw_line.isupper() or ("AGREEMENT" in raw_line or "CONTRACT" in raw_line or "LETTER" in raw_line))):
            h_text = clean_pdf_text(raw_line.lstrip("#").strip())
            pdf.set_font("Helvetica", "B", 13.5)
            pdf.set_text_color(15, 23, 42)
            pdf.ln(2)
            pdf.multi_cell(0, 6.5, h_text, align="C")
            pdf.ln(4)
            is_first_heading = False

        # Section Heading (## Section or 1. DEFINITIONS)
        elif raw_line.startswith("## ") or re.match(r"^(\d+\.|\bSECTION\b|\bARTICLE\b|\bCLAUSE\b)\s+[A-Z]", raw_line, re.IGNORECASE):
            h_text = clean_pdf_text(raw_line.lstrip("#").strip())
            pdf.set_font("Helvetica", "B", 10.5)
            pdf.set_text_color(30, 41, 59)
            pdf.ln(2.5)
            pdf.multi_cell(0, 5.5, h_text, align="L")
            pdf.ln(1)

        # Subheading (### Subheading)
        elif raw_line.startswith("### "):
            sub_text = clean_pdf_text(raw_line.lstrip("#").strip())
            pdf.set_font("Helvetica", "B", 9.5)
            pdf.set_text_color(51, 65, 85)
            pdf.ln(1.5)
            pdf.multi_cell(0, 5, sub_text, align="L")
            pdf.ln(1)

        # Bullet point
        elif raw_line.startswith("- ") or raw_line.startswith("* ") or raw_line.startswith("• "):
            bullet_body = clean_pdf_text(raw_line[2:].strip())
            bullet_text = f"  -  {bullet_body}"
            pdf.set_font("Helvetica", "", 9.5)
            pdf.set_text_color(30, 30, 30)
            pdf.multi_cell(0, 5, bullet_text, align="L")
            pdf.ln(1)

        # Regular paragraph text
        else:
            pdf.set_font("Helvetica", "", 9.5)
            pdf.set_text_color(30, 30, 30)
            pdf.multi_cell(0, 5, clean_line, align="J")
            pdf.ln(1.5)

    return bytes(pdf.output())


def generate_pdf(content: str, logo_path: str = "assets/logo.png") -> bytes:
    return format_pdf(content, "Legal Document", logo_path)


def generate_pdf_buffer(content: str, logo_path: str = "assets/logo.png") -> io.BytesIO:
    return io.BytesIO(format_pdf(content, "Legal Document", logo_path))

#!/usr/bin/env python3
"""
Script to generate professional PDF documentation for DC² (Développement par Contraintes Convergentes)
Generates both French and English versions with professional formatting.
"""

import os
import re
from datetime import datetime
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph,
    Spacer, PageBreak, KeepTogether, PageTemplate, Frame
)
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import textwrap


class NumberedCanvas(canvas.Canvas):
    """Canvas class that adds page numbers and footer information."""

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_state = None

    def showPage(self):
        self._saved_state = dict(self.__dict__)
        self._onPage()
        canvas.Canvas.showPage(self)

    def save(self):
        num_pages = self._pageNumber
        if self._saved_state is None:
            self._onPage()
        else:
            self.__dict__.update(self._saved_state)
        canvas.Canvas.save(self)

    def _onPage(self):
        self.saveState()

        # Page number at bottom
        page_num = self.getPageNumber()
        x = 7.5 * inch
        y = 0.5 * inch
        self.setFont("Helvetica", 9)
        self.setFillColor(HexColor("#666666"))
        self.drawString(x, y, str(page_num))

        self.restoreState()


def clean_markdown_content(text):
    """Clean markdown content for PDF."""
    # Remove front matter
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2]

    # Remove HTML components and JSX
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\{\{.*?\}\}', '', text)
    text = re.sub(r'<details>.*?</details>', '', text, flags=re.DOTALL)
    text = re.sub(r'```mermaid.*?```', '[Diagram]', text, flags=re.DOTALL)

    # Replace markdown links
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', text)

    # Clean extra whitespace
    text = re.sub(r'\n\n\n+', '\n\n', text)

    return text.strip()


def read_markdown_files(language='fr'):
    """Read all markdown documentation files in order."""
    base_path = Path('/home/eric/Projects/DocDriven/doc-driven_v1/src/content/docs')
    lang_path = base_path / language

    # Define reading order by sidebar_position
    files_order = [
        ('intro.md', 'Introduction'),
        ('fondements-theoriques.md', 'Fondements Théoriques'),
        ('phase1-architecture-strategique.md', 'Phase 1: Architecture Stratégique'),
        ('phase2-planification-tactique.md', 'Phase 2: Planification Tactique'),
        ('phase3-tdd-red.md', 'Phase 3: TDD RED'),
        ('phase4-tdd-green.md', 'Phase 4: TDD GREEN'),
        ('phase5-tdd-refactor.md', 'Phase 5: Refactoring'),
        ('phase6-triple-inspection.md', 'Phase 6: Triple Inspection'),
        ('roles-et-responsabilites.md', 'Rôles et Responsabilités'),
        ('licence.md', 'Licence'),
    ]

    sections = []
    for filename, title in files_order:
        filepath = lang_path / filename
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                clean_content = clean_markdown_content(content)
                sections.append({
                    'title': title,
                    'content': clean_content,
                    'filename': filename
                })

    return sections


def create_pdf(language='fr', output_filename='DC2-Documentation.pdf'):
    """Create a professional PDF document."""

    # Read content
    sections = read_markdown_files(language)

    if language == 'en':
        title_main = "DC² - Convergent Constraints Development"
        subtitle = "Structured LLM-Assisted Software Development Methodology"
        author = "Eric Gauthier"
        toc_title = "Table of Contents"
        page_title = "Page"
    else:  # fr
        title_main = "DC² - Développement par Contraintes Convergentes"
        subtitle = "Méthodologie Structurée du Développement Logiciel Assisté par LLM"
        author = "Eric Gauthier"
        toc_title = "Table des Matières"
        page_title = "Page"

    # Create PDF
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=A4,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=1*inch,
        bottomMargin=1*inch
    )

    doc.build([], canvasmaker=NumberedCanvas)

    # Rebuild with content
    styles = getSampleStyleSheet()

    # Custom styles
    cover_title = ParagraphStyle(
        'CoverTitle',
        parent=styles['Heading1'],
        fontSize=42,
        textColor=HexColor("#1A2332"),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    cover_subtitle = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontSize=18,
        textColor=HexColor("#2E86AB"),
        spaceAfter=24,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )

    cover_author = ParagraphStyle(
        'CoverAuthor',
        parent=styles['Normal'],
        fontSize=14,
        textColor=HexColor("#666666"),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )

    heading1 = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor("#1A2332"),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )

    heading2 = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=HexColor("#2E86AB"),
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )

    normal = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        alignment=TA_JUSTIFY,
        spaceAfter=10,
        textColor=HexColor("#2C3E50")
    )

    # Build story
    story = []

    # === COVER PAGE ===
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph(title_main, cover_title))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(subtitle, cover_subtitle))
    story.append(Spacer(1, 1.5*inch))

    today = datetime.now().strftime("%d %B %Y" if language == 'en' else "%d %B %Y")
    story.append(Paragraph(f"<b>Auteur:</b> {author}", cover_author))
    story.append(Paragraph(f"<b>Date:</b> {today}", cover_author))
    story.append(Paragraph("<b>Licence:</b> CC BY-SA 4.0", cover_author))
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph(
        "Version 1.0 - Professional Documentation",
        ParagraphStyle('Footer', fontSize=10, textColor=HexColor("#999999"), alignment=TA_CENTER)
    ))
    story.append(PageBreak())

    # === TABLE OF CONTENTS ===
    story.append(Paragraph(toc_title, heading1))
    story.append(Spacer(1, 0.3*inch))

    toc_items = []
    for i, section in enumerate(sections, 1):
        toc_items.append(f"<b>{section['title']}</b>")

    toc_text = "<br/>".join(toc_items)
    story.append(Paragraph(toc_text, normal))
    story.append(Spacer(1, 0.5*inch))
    story.append(PageBreak())

    # === CONTENT SECTIONS ===
    for section in sections:
        story.append(Paragraph(section['title'], heading1))

        # Split content into paragraphs for better formatting
        paragraphs = section['content'].split('\n\n')

        for para_text in paragraphs:
            if not para_text.strip():
                continue

            # Handle nested headers (marked with ## or ###)
            if para_text.startswith('###'):
                text = para_text.replace('###', '').strip()
                story.append(Spacer(1, 0.1*inch))
                story.append(Paragraph(text, styles['Heading3']))
                story.append(Spacer(1, 0.1*inch))
            elif para_text.startswith('##'):
                text = para_text.replace('##', '').strip()
                story.append(Spacer(1, 0.15*inch))
                story.append(Paragraph(text, heading2))
                story.append(Spacer(1, 0.1*inch))
            elif para_text.startswith('#'):
                text = para_text.replace('#', '').strip()
                story.append(Spacer(1, 0.15*inch))
                story.append(Paragraph(text, heading1))
                story.append(Spacer(1, 0.1*inch))
            else:
                # Regular paragraph
                text = para_text.strip()
                if text:
                    # Truncate very long lines for readability
                    story.append(Paragraph(text[:2000], normal))
                    story.append(Spacer(1, 0.1*inch))

        story.append(PageBreak())

    # Build PDF
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=A4,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=1*inch,
        bottomMargin=1*inch,
    )

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"✓ Generated: {output_filename}")


if __name__ == "__main__":
    # Generate French PDF
    create_pdf(
        language='fr',
        output_filename='/home/eric/Projects/DocDriven/doc-driven_v1/DC2-Developpement-par-Contraintes-Convergentes-FR.pdf'
    )

    # Generate English PDF
    create_pdf(
        language='en',
        output_filename='/home/eric/Projects/DocDriven/doc-driven_v1/DC2-Convergent-Constraints-Development-EN.pdf'
    )

    print("\n✓ Both PDFs generated successfully!")

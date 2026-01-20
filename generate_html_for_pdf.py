#!/usr/bin/env python3
"""
Generate professional HTML documentation files for DC²
These can be converted to PDF using LibreOffice
"""

import os
import re
from datetime import datetime
from pathlib import Path


def clean_markdown_content(text):
    """Clean markdown content for HTML."""
    # Remove front matter
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2]

    # Remove HTML components and JSX
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\{\{.*?\}\}', '', text)

    # Remove details/summary blocks but keep content
    text = re.sub(r'<details>.*?<summary>(.*?)</summary>', '', text, flags=re.DOTALL)
    text = re.sub(r'</details>', '', text)

    # Remove Mermaid diagrams
    text = re.sub(r'```mermaid.*?```', '', text, flags=re.DOTALL)

    # Remove anchor links like {#pourquoi-dc2}
    text = re.sub(r'\s*\{#[^}]+\}', '', text)

    # Replace markdown links - only keep the text, remove URL
    text = re.sub(r'\[(.*?)\]\([^)]*\)', r'\1', text)

    # Remove HTML entities that might not render
    text = text.replace('→', '→')  # Keep arrow

    # Handle code blocks BEFORE processing other markdown
    # Preserve code blocks with proper formatting
    code_blocks = []
    def preserve_code(match):
        code_blocks.append(match.group(1))
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"

    text = re.sub(r'```[a-z]*\n(.*?)\n```', preserve_code, text, flags=re.DOTALL)

    # Convert markdown headers
    text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)

    # Convert bold/italic
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*(.*?)(?!\*)\*', r'<em>\1</em>', text)
    text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)

    # Convert lists - handle both - and * for unordered lists
    lines = text.split('\n')
    in_ul = False
    in_ol = False
    result = []

    for line in lines:
        # Check for unordered lists
        if re.match(r'^\s*[-*]\s', line):
            if not in_ul:
                result.append('<ul>')
                in_ul = True
            item_text = re.sub(r'^\s*[-*]\s+', '', line).strip()
            result.append(f'<li>{item_text}</li>')
        # Check for ordered lists
        elif re.match(r'^\s*\d+\.\s', line):
            if not in_ol:
                result.append('<ol>')
                in_ol = True
            item_text = re.sub(r'^\s*\d+\.\s+', '', line).strip()
            result.append(f'<li>{item_text}</li>')
        else:
            if in_ul:
                result.append('</ul>')
                in_ul = False
            if in_ol:
                result.append('</ol>')
                in_ol = False
            result.append(line)

    if in_ul:
        result.append('</ul>')
    if in_ol:
        result.append('</ol>')

    text = '\n'.join(result)

    # Restore code blocks with proper formatting
    for i, code in enumerate(code_blocks):
        # Escape HTML in code
        code_escaped = (code
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
        )
        code_html = f'<pre><code>{code_escaped}</code></pre>'
        text = text.replace(f'__CODE_BLOCK_{i}__', code_html)

    # Convert blockquotes
    text = re.sub(r'^\> (.*?)$', r'<blockquote>\1</blockquote>', text, flags=re.MULTILINE)

    # Clean extra whitespace but preserve structure
    text = re.sub(r'\n\n\n+', '\n\n', text)

    # Remove empty paragraphs
    text = re.sub(r'<p>\s*</p>', '', text)

    return text.strip()


def read_markdown_files(language='fr'):
    """Read all markdown documentation files in order."""
    base_path = Path('/home/eric/Projects/DocDriven/doc-driven_v1/src/content/docs')
    lang_path = base_path / language

    files_order = [
        ('intro.md', 'Introduction'),
        ('fondements-theoriques.md', 'Fondements Théoriques'),
        ('phase1-architecture-strategique.md', 'Phase 1 : Architecture Stratégique'),
        ('phase2-planification-tactique.md', 'Phase 2 : Planification Tactique'),
        ('phase3-tdd-red.md', 'Phase 3 : TDD RED'),
        ('phase4-tdd-green.md', 'Phase 4 : TDD GREEN'),
        ('phase5-tdd-refactor.md', 'Phase 5 : Refactoring'),
        ('phase6-triple-inspection.md', 'Phase 6 : Triple Inspection'),
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


def create_html(language='fr', output_filename='documentation.html'):
    """Create a professional HTML document."""

    sections = read_markdown_files(language)

    if language == 'en':
        title_main = "DC² - Convergent Constraints Development"
        subtitle = "Structured LLM-Assisted Software Development Methodology"
        author = "Eric Gauthier"
        toc_title = "Table of Contents"
        license_text = "License: CC BY-SA 4.0"
        version = "Version 1.0"
    else:
        title_main = "DC² - Développement par Contraintes Convergentes"
        subtitle = "Méthodologie Structurée du Développement Logiciel Assisté par LLM"
        author = "Eric Gauthier"
        toc_title = "Table des Matières"
        license_text = "Licence : CC BY-SA 4.0"
        version = "Version 1.0"

    today = datetime.now().strftime("%d %B %Y")

    # HTML template with improved styling
    html_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html lang="{language}">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title_main}</title>
    <style type="text/css">
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        html, body {{
            font-family: 'Liberation Serif', 'Times New Roman', serif;
            line-height: 1.6;
            color: #2C3E50;
            font-size: 11pt;
        }}

        /* Cover page */
        .cover {{
            page-break-after: always;
            padding: 60pt 40pt;
            text-align: center;
            margin-top: 100pt;
        }}

        .cover h1 {{
            font-size: 36pt;
            color: #1A2332;
            margin-bottom: 20pt;
            font-weight: bold;
            line-height: 1.3;
        }}

        .cover h2 {{
            font-size: 16pt;
            color: #2E86AB;
            margin-bottom: 60pt;
            font-weight: normal;
            line-height: 1.5;
        }}

        .cover-meta {{
            margin-top: 80pt;
            font-size: 12pt;
            color: #666;
        }}

        .cover-meta p {{
            margin: 10pt 0;
        }}

        .cover-meta strong {{
            color: #1A2332;
        }}

        /* Table of contents */
        .toc {{
            page-break-after: always;
            padding: 40pt;
        }}

        .toc h2 {{
            font-size: 24pt;
            color: #1A2332;
            margin-bottom: 30pt;
            border-bottom: 2pt solid #2E86AB;
            padding-bottom: 10pt;
        }}

        .toc-entry {{
            margin: 12pt 0;
            padding-left: 20pt;
            font-size: 11pt;
            line-height: 1.5;
        }}

        /* Content */
        .section {{
            page-break-after: always;
            margin-bottom: 40pt;
            padding: 0 40pt;
        }}

        h1 {{
            font-size: 20pt;
            color: #1A2332;
            margin: 24pt 0 12pt 0;
            border-bottom: 2pt solid #2E86AB;
            padding-bottom: 8pt;
            font-weight: bold;
        }}

        h2 {{
            font-size: 14pt;
            color: #2E86AB;
            margin: 18pt 0 10pt 0;
            font-weight: bold;
        }}

        h3 {{
            font-size: 12pt;
            color: #06A77D;
            margin: 12pt 0 8pt 0;
            font-weight: bold;
        }}

        p {{
            margin: 10pt 0;
            text-align: justify;
            line-height: 1.6;
        }}

        ul {{
            margin: 12pt 0 12pt 30pt;
            padding-left: 0;
        }}

        ol {{
            margin: 12pt 0 12pt 30pt;
            padding-left: 0;
        }}

        li {{
            margin: 6pt 0;
            line-height: 1.5;
        }}

        pre {{
            background: #f5f5f5;
            padding: 10pt;
            margin: 12pt 0;
            border-left: 3pt solid #2E86AB;
            font-family: 'Courier New', monospace;
            font-size: 9pt;
            line-height: 1.4;
            overflow-x: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}

        code {{
            font-family: 'Courier New', monospace;
            font-size: 9pt;
        }}

        pre code {{
            background: none;
            padding: 0;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 12pt 0;
            font-size: 10pt;
        }}

        table th {{
            background: #f0f4f8;
            padding: 8pt;
            text-align: left;
            border: 1pt solid #ccc;
            font-weight: bold;
            color: #1A2332;
        }}

        table td {{
            padding: 8pt;
            border: 1pt solid #ddd;
        }}

        table tr:nth-child(even) {{
            background: #f9f9f9;
        }}

        blockquote {{
            border-left: 3pt solid #2E86AB;
            padding-left: 15pt;
            margin: 12pt 0;
            font-style: italic;
            color: #666;
            line-height: 1.6;
        }}

        strong {{
            font-weight: bold;
        }}

        em {{
            font-style: italic;
        }}

        /* Footer */
        .footer {{
            page-break-before: always;
            margin-top: 40pt;
            padding: 20pt 40pt;
            border-top: 1pt solid #ccc;
            text-align: center;
            font-size: 10pt;
            color: #999;
        }}
    </style>
</head>
<body>
    <!-- COVER PAGE -->
    <div class="cover">
        <h1>{title_main}</h1>
        <h2>{subtitle}</h2>
        <div class="cover-meta">
            <p><strong>Auteur :</strong> {author}</p>
            <p><strong>Date :</strong> {today}</p>
            <p><strong>{license_text}</strong></p>
            <p style="margin-top: 20pt; font-size: 10pt;">{version}</p>
        </div>
    </div>

    <!-- TABLE OF CONTENTS -->
    <div class="toc">
        <h2>{toc_title}</h2>
"""

    # Add TOC entries
    for i, section in enumerate(sections, 1):
        html_content += f'        <div class="toc-entry">{i}. {section["title"]}</div>\n'

    html_content += """    </div>

    <!-- CONTENT -->
"""

    # Add sections
    for section in sections:
        html_content += f"""    <div class="section">
        <h1>{section['title']}</h1>
        {section['content']}
    </div>

"""

    html_content += """    <!-- FOOTER -->
    <div class="footer">
        <p>© Eric Gauthier - CC BY-SA 4.0</p>
    </div>

</body>
</html>
"""

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✓ Generated HTML: {output_filename}")
    return output_filename


if __name__ == "__main__":
    # Generate French HTML
    fr_html = create_html(
        language='fr',
        output_filename='/home/eric/Projects/DocDriven/doc-driven_v1/DC2-FR.html'
    )

    # Generate English HTML
    en_html = create_html(
        language='en',
        output_filename='/home/eric/Projects/DocDriven/doc-driven_v1/DC2-EN.html'
    )

    print("\n✓ Both HTML files generated!")
    print(f"\nFrench: {fr_html}")
    print(f"English: {en_html}")

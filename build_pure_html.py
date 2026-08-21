#!/usr/bin/env python3
"""
Pure HTML site builder for Amazon PPC Student Wiki
Converts markdown files to HTML with ppc-tools-for-va theme
"""
import os
import re
import json
from pathlib import Path

# Try to import markdown, install if needed
try:
    import markdown
except ImportError:
    import subprocess
    subprocess.check_call(['pip', 'install', '-q', 'markdown'])
    import markdown

MD = markdown.Markdown(extensions=['tables', 'toc', 'fenced_code', 'codehilite'])

# Configuration
SITE_DIR = Path(__file__).parent / 'site_pure'
DOCS_DIR = Path(__file__).parent / 'docs'
TEMPLATE_FILE = Path(__file__).parent / 'template.html'

# Color scheme from ppc-tools-for-va
COLORS = {
    'ink': '#101820',
    'muted': '#65707a',
    'paper': '#f5f4ef',
    'white': '#fff',
    'amber': '#ffb21c',
    'gold': '#d98400',
    'navy': '#14232f',
    'line': '#d9dcda',
}

# Navigation structure from mkdocs.yml
NAV = [
    ('Home', 'index.html'),
    ('Complete Guide', 'complete-data-filled-guide.html'),
    ('Discover & Explore', 'discover.html'),
    ('PPC Strategy Hub', 'strategies.html'),
    ('Pro Tips & Tactics', 'tips.html'),
    ('Tools & Automation', 'tools.html'),
    ('Automation & Rules', 'automation.html'),
    ('VA Resources', 'va-resources.html'),
    ('Online Resources', 'online-resources.html'),
    ('Interview Questions', 'interview-hub.html'),
    ('Glossary', 'glossary.html'),
    ('Formulas & Calculators', 'appendix/formulas-calculators.html'),
]

def get_nav_html(current_page):
    """Generate navigation HTML"""
    nav_items = []
    for title, href in NAV:
        active = ' class="active"' if current_page == href else ''
        nav_items.append(f'<a href="{href}"{active}>{title}</a>')
    return '\n'.join(nav_items)

def get_sidebar():
    """Generate sidebar with sections"""
    sections = [
        ('1. Foundations & Fundamentals', [
            ('What is Amazon PPC', 'sections/01-1-foundations-and-fundamentals/1-1-1-1-what-is-amazon-ppc.html'),
            ('Amazon Advertising Ecosystem', 'sections/01-1-foundations-and-fundamentals/1-2-1-2-the-amazon-advertising-ecosystem.html'),
            ('Core Terminology Primer', 'sections/01-1-foundations-and-fundamentals/1-3-1-3-core-terminology-primer.html'),
            ('Eligibility & Prerequisites', 'sections/01-1-foundations-and-fundamentals/1-4-1-4-eligibility-and-prerequisites.html'),
        ]),
        ('2. Account & Campaign Architecture', [
            ('Account Structure Philosophy', 'sections/02-2-account-and-campaign-architecture/2-1-2-1-account-structure-philosophy.html'),
            ('Campaign Structuring Models', 'sections/02-2-account-and-campaign-architecture/2-2-2-2-campaign-structuring-models.html'),
            ('Ad Group Best Practices', 'sections/02-2-account-and-campaign-architecture/2-3-2-3-ad-group-best-practices.html'),
            ('Portfolio & Budget Grouping', 'sections/02-2-account-and-campaign-architecture/2-4-2-4-portfolio-and-budget-grouping.html'),
        ]),
        ('3. Campaign Types', [
            ('Sponsored Products', 'sections/03-3-campaign-types/3-1-3-1-sponsored-products-sp.html'),
            ('Sponsored Brands', 'sections/03-3-campaign-types/3-2-3-2-sponsored-brands-sb.html'),
            ('Sponsored Display', 'sections/03-3-campaign-types/3-3-3-3-sponsored-display-sd.html'),
            ('Sponsored TV', 'sections/03-3-campaign-types/3-4-3-4-sponsored-tv-streaming-tv-ads.html'),
            ('Amazon DSP', 'sections/03-3-campaign-types/3-5-3-5-amazon-dsp.html'),
        ]),
        ('4. Targeting & Match Types', [
            ('Keyword Match Types', 'sections/04-4-targeting-and-match-types/4-1-4-1-keyword-match-types.html'),
            ('Product Targeting', 'sections/04-4-targeting-and-match-types/4-2-4-2-product-targeting.html'),
            ('Audience Targeting', 'sections/04-4-targeting-and-match-types/4-3-4-3-audience-targeting.html'),
            ('Auto-Targeting Categories', 'sections/04-4-targeting-and-match-types/4-4-4-4-auto-targeting-categories.html'),
        ]),
        ('5. Keyword Research', [
            ('Research Methodology', 'sections/05-5-keyword-research-and-search-term-mining/5-1-5-1-research-methodology.html'),
            ('Keyword Research Tools', 'sections/05-5-keyword-research-and-search-term-mining/5-2-5-2-keyword-research-tools.html'),
            ('Search Term Harvesting', 'sections/05-5-keyword-research-and-search-term-mining/5-3-5-3-search-term-harvesting-workflow.html'),
            ('Long-Tail vs Head Terms', 'sections/05-5-keyword-research-and-search-term-mining/5-4-5-4-long-tail-vs-head-term-strategy.html'),
        ]),
        ('6. Bidding Strategies', [
            ('Manual Bidding', 'sections/06-6-bidding-strategies-and-bid-management/6-1-6-1-manual-bidding-fundamentals.html'),
            ('Dynamic Bidding', 'sections/06-6-bidding-strategies-and-bid-management/6-2-6-2-dynamic-and-rule-based-bidding.html'),
            ('Bid Adjustment Cadence', 'sections/06-6-bidding-strategies-and-bid-management/6-3-6-3-bid-adjustment-cadence.html'),
            ('Placement Bid Modifiers', 'sections/06-6-bidding-strategies-and-bid-management/6-4-6-4-placement-bid-modifiers.html'),
        ]),
    ]

    html = '<nav class="sidebar">\n'
    for section_title, links in sections:
        html += f'<div class="sidebar-section"><h3>{section_title}</h3><ul>\n'
        for title, href in links:
            html += f'<li><a href="{href}">{title}</a></li>\n'
        html += '</ul></div>\n'
    html += '</nav>'
    return html

def get_template():
    """Get the HTML template"""
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#14232f">
  <meta name="description" content="Amazon PPC Student Wiki - Beginner-friendly knowledge base for Amazon PPC training">
  <title>{{TITLE}} | Amazon PPC Wiki</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
:root{
  --ink:#101820;
  --muted:#65707a;
  --paper:#f5f4ef;
  --white:#fff;
  --amber:#ffb21c;
  --gold:#d98400;
  --navy:#14232f;
  --line:#d9dcda;
  --shadow:0 22px 70px #1018201c;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font:400 16px/1.55 "DM Sans",sans-serif}
a{color:inherit;text-decoration:none}
h1,h2,h3,h4{font-family:Manrope,sans-serif;line-height:1.08;margin:0}
h1{font-size:clamp(36px,4vw,56px);letter-spacing:-.03em;margin-bottom:24px}
h2{font-size:clamp(28px,3vw,38px);margin:32px 0 16px}
h3{font-size:22px;margin:24px 0 12px}
p{max-width:720px;margin:0 0 16px;color:var(--muted)}
ul,ol{margin:0 0 20px;padding-left:24px}
li{margin-bottom:8px}
code{background:#e8ebe9;padding:2px 6px;border-radius:4px;font-family:monospace;font-size:14px}
pre{background:var(--navy);color:#fff;padding:20px;border-radius:12px;overflow-x:auto;margin:20px 0}
pre code{background:none;padding:0}
table{width:100%;border-collapse:collapse;margin:20px 0}
th,td{padding:12px 16px;text-align:left;border-bottom:1px solid var(--line)}
th{background:var(--navy);color:white;font-weight:600}
tr:hover{background:#f8f7f4}
blockquote{border-left:4px solid var(--amber);margin:20px 0;padding:16px 24px;background:#fff;border-radius:0 12px 12px 0}
blockquote p{color:var(--ink);margin:0}
.skip{position:fixed;top:-60px;left:20px;background:var(--ink);color:white;padding:12px;z-index:300}
.skip:focus{top:12px}
header{height:70px;padding:0 max(24px,calc((100% - 1200px)/2));display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100;background:#f5f4efed;backdrop-filter:blur(13px);border-bottom:1px solid #10182012}
.brand{display:flex;align-items:center;gap:11px;text-decoration:none;font:800 20px/1 Manrope}
.brand>i{width:34px;height:34px;background:var(--ink);border-radius:9px;padding:8px;display:flex;align-items:end;gap:3px}
.brand>i b{width:5px;background:var(--amber);border-radius:2px}
.brand>i b:first-child{height:45%}
.brand>i b:nth-child(2){height:72%}
.brand>i b:last-child{height:100%}
.brand em{font-style:normal;color:var(--gold)}
.brand small{display:block;font:500 8px "DM Sans";letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-top:5px}
nav.main-nav{display:flex;gap:20px;align-items:center;flex-wrap:wrap}
nav.main-nav a{font-size:13px;font-weight:600;padding:8px 12px;border-radius:6px;transition:all .2s}
nav.main-nav a:hover,nav.main-nav a.active{background:var(--amber);color:var(--ink)}
nav .git{background:var(--ink);color:white}
nav .git:hover{background:#263744;color:white}
.layout{display:grid;grid-template-columns:240px 1fr;min-height:calc(100vh - 70px)}
.sidebar{background:white;border-right:1px solid var(--line);padding:24px 0;overflow-y:auto}
.sidebar-section{margin-bottom:24px}
.sidebar-section h3{font-size:11px;text-transform:uppercase;letter-spacing:.12em;color:var(--muted);padding:0 20px;margin-bottom:12px}
.sidebar-section ul{list-style:none;padding:0;margin:0}
.sidebar-section li a{display:block;padding:8px 20px;font-size:14px;color:var(--muted);border-left:3px solid transparent}
.sidebar-section li a:hover{background:var(--paper);color:var(--ink);border-left-color:var(--amber)}
.content{padding:40px max(24px,calc((100% - 900px)/2)) 80px;max-width:100%}
.hero-section{background:radial-gradient(circle at 90% 25%,#ffb21c29,transparent 28%);padding:60px max(24px,calc((100% - 900px)/2));border-bottom:1px solid var(--line)}
.hero-section h1{margin-bottom:16px}
.hero-section p{font-size:18px}
.breadcrumb{padding:12px max(24px,calc((100% - 900px)/2));background:white;border-bottom:1px solid var(--line);font-size:13px;color:var(--muted)}
.breadcrumb a{color:var(--amber);font-weight:600}
.stats{display:flex;gap:40px;padding:30px 0;border-top:1px solid var(--line);margin-top:40px}
.stats>div{display:flex;align-items:center;gap:12px}
.stats b{font:800 28px Manrope;color:var(--gold)}
.stats span{font-size:13px;color:var(--muted)}
.alert{background:#fff8e6;border:1px solid var(--amber);padding:16px 20px;border-radius:12px;margin:20px 0}
.alert-info{background:#e8f4fc;border-color:#2562a7;color:#2562a7}
.alert-success{background:#e2f3ec;border-color:#08745a;color:#08745a}
.card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px;margin:30px 0}
.card{background:white;border:1px solid var(--line);border-radius:16px;padding:24px;transition:.2s}
.card:hover{transform:translateY(-3px);box-shadow:var(--shadow)}
.card h3{margin-top:0}
.card a{color:var(--amber);font-weight:600;display:inline-flex;align-items:center;gap:6px}
.card a:hover{color:var(--gold)}
footer{background:var(--navy);color:#bdc5ca;padding:50px max(24px,calc((100% - 1200px)/2)) 24px}
footer a{color:var(--amber)}
.foot-top{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:20px;padding-bottom:30px;border-bottom:1px solid #34424b}
.foot-top .brand{color:white}
.foot-bottom{padding-top:20px;font-size:12px;color:#738089}
@media(max-width:900px){
  .layout{grid-template-columns:1fr}
  .sidebar{display:none}
  nav.main-nav{display:none}
}
@media(max-width:600px){
  .hero-section{padding:40px 20px}
  .content{padding:30px 20px}
  h1{font-size:32px}
}
  </style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header>
  <a class="brand" href="index.html">
    <i><b></b><b></b><b></b></i>
    <span>PPC <em>Wiki</em><small>Student Edition</small>
  </a>
  <nav class="main-nav">
    {{NAV}}
  </nav>
</header>

{{CONTENT}}

<footer>
  <div class="foot-top">
    <a class="brand" href="index.html">
      <i><b></b><b></b><b></b></i>
      <span>PPC <em>Wiki</em><small>Student Edition</small>
    </a>
    <p>Beginner-friendly Amazon PPC knowledge base</p>
    <a href="https://github.com/projectamazonph/Amazon-PPC-Student-Wiki">View on GitHub</a>
  </div>
  <div class="foot-bottom">
    <span>&copy; 2026 ProjectAmazonPH. MIT licensed.</span>
  </div>
</footer>
</body>
</html>'''

def convert_markdown(content):
    """Convert markdown to HTML"""
    # Reset markdown processor
    MD.reset()
    html = MD.convert(content)
    # Fix relative links
    html = html.replace('href="/', 'href="')
    html = html.replace('src="/', 'src="')
    return html

def process_markdown_file(md_path, output_dir):
    """Convert a single markdown file to HTML"""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title from first heading or frontmatter
    title = 'Untitled'
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm = parts[1]
            for line in fm.split('\n'):
                if line.startswith('title:'):
                    title = line.split(':', 1)[1].strip().strip('"').strip("'")
            content = parts[2]

    # Find first heading for title
    first_heading = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if first_heading:
        title = first_heading.group(1).strip()

    # Convert markdown to HTML
    html_content = convert_markdown(content)

    # Wrap in template
    nav = get_nav_html('')
    template = get_template()

    # Create breadcrumb - preserve directory structure
    rel_path = md_path.relative_to(DOCS_DIR)
    parts = list(rel_path.parts)
    if parts[-1] == 'index.md':
        parts = parts[:-1]
    breadcrumb = ' &rsaquo; '.join(['<a href="index.html">Home</a>'] + [f'<span>{p.replace("-", " ").title()}</span>' for p in parts])

    # Build the full HTML
    full_html = template.replace('{{TITLE}}', title)
    full_html = full_html.replace('{{NAV}}', nav)

    # Add content with hero section
    content_wrapper = f'''
<div class="hero-section">
  <h1>{title}</h1>
  <p>Learn Amazon PPC from scratch with this beginner-friendly knowledge base.</p>
</div>
<div class="breadcrumb">{breadcrumb}</div>
<main class="content" id="main">
  {html_content}
  <div class="stats">
    <div><b>25+</b><span>Sections</span></div>
    <div><b>120+</b><span>Pages</span></div>
    <div><b>100%</b><span>Free</span></div>
  </div>
</main>
'''
    full_html = full_html.replace('{{CONTENT}}', content_wrapper)

    # Determine output path - preserve directory structure
    # Convert .md to .html and keep folder structure
    output_parts = list(rel_path.parts[:-1])  # All folders
    filename = rel_path.stem  # filename without extension

    # Use folder name if file is index.md
    if filename == 'index':
        if len(rel_path.parts) > 1:
            # Use parent folder name
            output_parts = list(rel_path.parts[:-1])
            filename = 'index'

    output_subdir = output_dir
    for part in output_parts:
        output_subdir = output_subdir / part

    output_subdir.mkdir(parents=True, exist_ok=True)
    output_path = output_subdir / f'{filename}.html'

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

    return output_path

def build_site():
    """Build the entire site"""
    # Clean and create output directory
    if SITE_DIR.exists():
        import shutil
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir(parents=True)

    print(f"Building site to {SITE_DIR}...")

    # Process all markdown files
    md_files = list(DOCS_DIR.rglob('*.md'))
    print(f"Found {len(md_files)} markdown files")

    for md_file in md_files:
        # Skip certain files
        if md_file.name.startswith('.'):
            continue

        try:
            output_file = process_markdown_file(md_file, SITE_DIR)
            print(f"  Created: {output_file.relative_to(SITE_DIR)}")
        except Exception as e:
            print(f"  Error processing {md_file}: {e}")

    print(f"\nSite built successfully!")
    print(f"Output directory: {SITE_DIR}")

if __name__ == '__main__':
    build_site()

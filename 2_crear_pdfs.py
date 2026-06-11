import pandas as pd
import pdfkit
import os

# Critical configuration for Windows environment
wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

df = pd.read_csv("source_data.csv")
os.makedirs("generated_pdfs", exist_ok=True)

html_template = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
    body {{ font-family: 'Helvetica', 'Arial', sans-serif; margin: 0; padding: 30px; color: #333; line-height: 1.4; }}
    .header {{ text-align: center; border-bottom: 3px solid #1f77b4; padding-bottom: 12px; margin-bottom: 25px; }}
    .header h1 {{ margin: 0; color: #111; font-size: 28px; }}
    .header h3 {{ margin: 5px 0 0 0; color: #555; font-size: 16px; font-weight: normal; text-transform: uppercase; }}
    .container {{ display: table; width: 100%; }}
    .col-left {{ display: table-cell; width: 35%; border-right: 1px solid #ddd; padding-right: 25px; vertical-align: top; }}
    .col-right {{ display: table-cell; width: 65%; padding-left: 25px; vertical-align: top; }}
    .title {{ color: #1f77b4; font-size: 14px; font-weight: bold; margin-top: 20px; margin-bottom: 8px; border-bottom: 1px solid #1f77b4; text-transform: uppercase; }}
    p {{ margin: 0 0 10px 0; font-size: 13px; color: #444; }}
</style>
</head>
<body>
    <div class="header">
        <h1>{name}</h1>
        <h3>{role}</h3>
    </div>
    <div class="container">
        <div class="col-left">
            <div class="title">Technical Skills</div>
            <p>{skills}</p>
            <div class="title">Education & Credentials</div>
            <p>{education}</p>
        </div>
        <div class="col-right">
            <div class="title">Executive Summary</div>
            <p>{summary}</p>
            <div class="title">Latest Professional Experience</div>
            <p><strong>{role}</strong> at {current_company}</p>
            <p>Duration: {experience_years} years of proven track record.</p>
        </div>
    </div>
</body>
</html>
"""

print("⏳ Rendering a controlled sample of 20 physical PDFs for visual validation...")

# Render only the first 20 profiles to optimize disk usage and rendering times
for index, row in df.head(20).iterrows():
    html_rendered = html_template.format(
        name=row['name'], role=row['role'], skills=row['skills'],
        education=row['education'], summary=row['summary'],
        current_company=row['current_company'], experience_years=row['experience_years']
    )
    output_pdf_path = f"generated_pdfs/{row['id']}.pdf"
    pdfkit.from_string(html_rendered, output_pdf_path, configuration=config)

print("✅ Step 2 completed! Sample PDFs created in 'generated_pdfs'. Full set ready for analytical audit.")

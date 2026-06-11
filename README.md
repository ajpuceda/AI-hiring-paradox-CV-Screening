# AI-hiring-paradox-CV-Screening
A local Python lab simulating automated recruitment pipelines for 1,000 resumes. Analysing the AI hiring paradox, cloud unit economics, and strategic talent data loss in modern 2-column layout formats.

# The AI Hiring Paradox Lab 🚀

This repository contains the local Python lab environment used to simulate an automated recruitment pipeline screening 1,000 applications. It analyzes the direct unit economics (Cloud API pricing benchmarks) against the strategic cost of opportunity caused by text-parsing data loss in non-linear vector formats (like modern 2-column resume designs).

## 🔬 Lab Architecture
The project is decoupled into three sequential micro-steps for absolute modularity:
1. `1_generate_data.py`: Programmatically synthesizes an ethically compliant dataset of 1,000 technology applicants using `pandas` and `Faker` (with locked seed states for exact scientific replication).
2. `2_create_pdfs.py`: Renders structured rows into a visual, modern 2-column HTML layout converted into standard PDFs via `pdfkit` and `wkhtmltopdf` to challenge standard text-parsers.
3. `3_simulate_audit.py`: Computes linear horizontal text extraction, evaluates semantic token degradation, and processes strategic false-negative metrics at corporate scale.

## 📊 Consolidated Metrics (N=1,000)
* **Application Funnel Volume:** 1,000 resumes
* **Cloud Cost (Flat Text Ingestion):** $0.150 USD
* **Cloud Cost (Visual Matrix Ingestion):** $1.800 USD
* **Target Executive Profiles (EMBA):** 351 candidates
* **Algorithmic False Negatives (Talent Lost):** 48 Star Managers
* **Strategic Talent Destruction Rate:** 13.7%

## 🛠️ Installation & Execution
1. Install system dependency: [wkhtmltopdf](https://wkhtmltopdf.org)
2. Clone the repository and install core dependencies:
   ```bash
   pip install pandas faker pdfkit openpyxl
   ```
3. Run the complete pipeline sequentially:
   ```bash
   python 1_generate_data.py
   python 2_create_pdfs.py
   python 3_simulate_audit.py
   ```


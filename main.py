from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)  # Stop page from auto breaking

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font("Times", "B",24) # Need to set font first, or else you get an error
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

    # Set footer for main page
    pdf.ln(265)  # 265 breaklines or 265 mm
    pdf.set_font("Times", "I",8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for page in range(row["Pages"] - 1):  # one page already added with header
        pdf.add_page()

        # Set footer for page
        pdf.ln(277)  # 277 breaklines or 277 mm
        pdf.set_font("Times", "I", 8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
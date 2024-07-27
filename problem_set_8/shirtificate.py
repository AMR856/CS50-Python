#!/usr/bin/python3
from fpdf import FPDF

INPUT_STR = 'Name: '
if __name__ == "__main__":
    full_name = input(INPUT_STR)
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font("Helvetica", size=40)
    pdf.set_y(0)
    pdf.cell(w=0, h=40, txt="CS50 Shirtificate", border=0, ln=1, align='C')
    pdf.image('shirtificate.png', x=0, y=35)
    pdf.set_font("Helvetica", size=30)
    pdf.set_text_color(r= 255, g=255, b=255)
    pdf.set_y(75)
    pdf.cell(w=0, h=40, txt=f'{full_name} took CS50', border=0, ln=1, align='C')
    pdf.output('shirtificate.pdf')

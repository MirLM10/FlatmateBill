import webbrowser
from fpdf import FPDF
import os
from filestack import Client


class PdfReport:
    """
    Object to generate a PDF file/report which shows
    the amount to be paid by each of the flatmates,
    also showing the period for which it has to be paid
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF()
        pdf.add_page()

        # Adding the logo
        pdf.image('files/logo.png', w=20, h=20)

        # Adding the heading and time period
        pdf.set_font(family='Times', style='B', size=30)
        pdf.cell(w=0, h=50, txt='FLAT BILL', ln=1, align='C')
        pdf.set_font(family='Times', style='', size=20)
        pdf.cell(w=25, h=35, txt='Period:')
        pdf.cell(w=60, h=35, txt=bill.period, ln=1)

        # Adding details of 1st flatmate
        pdf.set_font(family='Times', style='', size=15)
        pdf.cell(w=100, h=10, txt=flatmate1.name)
        pdf.cell(w=50, h=10, txt='Rs. ' + str(round(flatmate1.pays(bill, flatmate2), 2)), ln=1)

        # Adding details of 2nd flatmate
        pdf.cell(w=100, h=10, txt=flatmate2.name)
        pdf.cell(w=50, h=10, txt='Rs. ' + str(round(flatmate2.pays(bill, flatmate1), 2)), ln=1)

        # create the pdf file of the bill in files
        os.chdir('files')
        pdf.output(name=self.filename)

        # open the pdf file
        webbrowser.open(self.filename)


class FileSharer:
    """
    Object to create the link of the pdf file to
    open the file in production environment
    """

    def __init__(self, path, apiKey='Acf4rLiCaSxCYBQnMt0n9z'):
        self.apiKey = apiKey
        self.path = path

    def share(self):
        client = Client(self.apiKey)
        fileLink = client.upload(filepath=self.path)
        return fileLink.url

__author__ = 'tiirz'

from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from sys import stdin

for i in range(114):
    packet = StringIO.StringIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica-Oblique", 20)
    university = stdin.readline()[0:-1]
    team = stdin.readline()[0:-1]
    participant = stdin.readline()[0:-1]
    x = 480
    if len(university) < 40:
        can.drawCentredString(x, 405, university)
    else:
        j = 39;
        while j >= 0:
            if university[j] == ' ':
                break
            j -= 1
        can.drawCentredString(x, 420, university[0:j])
        can.drawCentredString(x, 395, university[j:len(university)])

    can.drawCentredString(x, 360, team)
    can.setFont("Helvetica-BoldOblique", 25)
    can.drawCentredString(x, 300, participant)

    can.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    existing_pdf = PdfFileReader(file("tmp.pdf", "rb"))
    output = PdfFileWriter()
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    outputStream = file("pdf/" + team + str(i % 3) + ".pdf", "wb")
    output.write(outputStream)
    outputStream.close()

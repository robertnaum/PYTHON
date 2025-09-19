from reportlab.pdfgen import canvas


pdf_file = canvas.Canvas("texts\clcodingpdff.pdf")
pdf_file.drawString(72,720,"Hello,World")
pdf_file.drawString(72,700,"Free PDF Document")



pdf_file.save()

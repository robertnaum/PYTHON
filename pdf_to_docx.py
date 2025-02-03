from pdf2docx import Converter
pdf_file = "Quadratic.pdf"
docx_file = "Quadratic.docx"
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
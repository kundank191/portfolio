import PyPDF2
from io import BytesIO

def crop_pdf(file_in_memory, left, top, width, height):
    file_in_memory.seek(0)
    reader = PyPDF2.PdfFileReader(file_in_memory)
    writer = PyPDF2.PdfFileWriter()

    for page_num in range(reader.getNumPages()):
        page = reader.getPage(page_num)
        page.mediaBox.lowerLeft = (left, top)
        page.mediaBox.upperRight = (left + width, top + height)
        writer.addPage(page)

    cropped_pdf = BytesIO()
    writer.write(cropped_pdf)
    cropped_pdf.seek(0)
    
    return cropped_pdf

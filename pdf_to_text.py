import io

import PyPDF2


def pdf_to_text(pdf_bytes: io.BytesIO):
    # Create a PyPDF2 reader object
    pdf = PyPDF2.PdfReader(pdf_bytes)
    return ("––– NEXT PAGE –––").join(page.extract_text() for page in pdf.pages)

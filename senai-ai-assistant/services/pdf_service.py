# services/pdf_service.py
from pypdf import PdfReader
def extract_text(file):
    reader = PdfReader(file)
    conteudo = ""
    for page in reader.pages:
        conteudo += page.extract_text()
    return conteudo
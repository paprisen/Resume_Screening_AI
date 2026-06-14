import PyPDF2

def extract_text(pdf_path):
    text = ""

    with open(pdf_path, "rb") as file:
        pdf = PyPDF2.PdfReader(file)

        for page in pdf.pages:
            text += page.extract_text()

    return text

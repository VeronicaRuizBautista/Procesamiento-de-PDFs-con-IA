from pdfminer.high_level import extract_text

def texto(pdf):
    text = extract_text(pdf)
    return text
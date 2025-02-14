import pdfplumber

def extraer_texto_y_tablas(pdf):
    with pdfplumber.open(pdf) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            
            tables= page.extract_tables()
            for table in tables:
                for row in table:
                    rows = [row]               
                    return text, rows

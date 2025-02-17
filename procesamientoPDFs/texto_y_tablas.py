import pdfplumber

def texto_y_tablas(pdf):
    texto_completo = ""
    tablas = []
    with pdfplumber.open(pdf) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                texto_completo += f"Página {i + 1} \n{text}"
                        
            tables= page.extract_tables() or []
            for j, table in enumerate(tables):
                formatted_table = [["" if cell is None else cell for cell in row] for row in table]
                for row in table:
                    formatted_table.append(row)
                tablas.append(formatted_table)          
        return texto_completo, tablas

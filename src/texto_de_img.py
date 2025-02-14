import pytesseract
from pdf2image import conver_from_path
from PIL import Image

def texto_de_img(pdf):
    images = conver_from_path(pdf, 300)
    texto_completo = ''
    for i, page in enumerate(images):
        text = pytesseract.image_to_string(page)
        texto_completo += f"\n--- Página {i+1} ---\n {text}"
        return texto_completo
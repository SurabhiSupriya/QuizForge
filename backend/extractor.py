import pdfplumber
import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image

def extract_text_from_pdf_file(file_obj):
    """
    Extracts text from a file-like PDF object.
    Tries text-based extraction first, then OCR if needed.
    """
    # 1. Try extracting text with pdfplumber
    try:
        with pdfplumber.open(file_obj) as pdf:
            text_pages = [page.extract_text() for page in pdf.pages if page.extract_text()]
            if text_pages:
                return "\n".join(text_pages)
    except Exception as e:
        print(f"[!] Text extraction failed: {e}")

    # 2. Fall back to OCR using images converted from bytes
    try:
        file_obj.seek(0)  # Reset pointer
        images = convert_from_bytes(file_obj.read())
        ocr_text = [pytesseract.image_to_string(img) for img in images]
        return "\n".join(ocr_text)
    except Exception as e:
        print(f"[!] OCR failed: {e}")
        return ""

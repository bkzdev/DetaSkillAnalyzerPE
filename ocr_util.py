try:
    import pytesseract
    from PIL import Image
except ImportError:
    pytesseract = None

def perform_ocr(image_path):
    if pytesseract is None:
        print("pytesseractがインストールされていません。OCRは実行されません。")
        return ""
    return pytesseract.image_to_string(Image.open(image_path), lang="jpn")
import pytesseract
from PIL import Image

def main():
    file_path = input('put file: ')
    img = Image.open(file_path)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(img, lang="rus")
    print(text)

if __name__ == '__main__':
    main()


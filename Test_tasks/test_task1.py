import cv2
from matplotlib import pyplot as pl
import pytesseract

def main():
    img = cv2.imread('0.jpeg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pl.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
    pl.show()
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    print(pytesseract.image_to_string(img, lang="rus"))

if __name__ == '__main__':
    main()

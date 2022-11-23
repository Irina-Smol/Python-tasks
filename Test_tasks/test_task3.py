import cv2
import pytesseract

def main():
    file_path = input('put file: ')
    img = cv2.imread(file_path)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    print(pytesseract.image_to_string(img, lang="rus"))
    cv2.imshow("0", img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
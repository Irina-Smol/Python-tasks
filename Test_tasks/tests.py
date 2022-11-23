import cv2
import pytesseract

#for 2 picture
img = cv2.imread("1.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

data = pytesseract.image_to_data(img)
for i, el in enumerate(data.splitlines()):
    if i == 0:
        continue
    el = el.split()
    try:
        x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
        cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
        cv2.putText(img, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)
    except IndexError:
        print('exit')
new_img = cv2.imshow("0", img[230:570, 230:570])
cv2.waitKey(0)

#for 1 picture
img2 = cv2.imread("0.jpeg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
config = r'--oem 3 --psm 6'
data = pytesseract.image_to_data(img2, config=config)
for i, el in enumerate(data.splitlines()):
    if i == 0:
        continue
    el = el.split()
    try:
        x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
        cv2.rectangle(img2, (x, y), (w + x, h + y), (0, 0, 255), 1)
        cv2.putText(img2, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)
    except IndexError:
        print('exit')
new_img2 = cv2.imshow("2", img2[200:450, 200:450])
cv2.waitKey(0)

#for 3 picture
img3 = cv2.imread("2.jpeg")
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

data = pytesseract.image_to_data(img3)
for i, el in enumerate(data.splitlines()):
    if i == 0:
        continue
    el = el.split()
    try:
        x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
        cv2.rectangle(img3, (x, y), (w + x, h + y), (0, 0, 255), 1)
        cv2.putText(img3, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)
    except IndexError:
        print('exit')
new_img3 = cv2.imshow("3", img3[270:580, 270:580])
cv2.waitKey(0)

#for 4 picture



import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

config = r'--oem 3 --psm 6'

data = pytesseract.image_to_data(img, config=config)

for i, el in enumerate(data.splitlines()):
    if i == 0:
        continue

    el = el.split()

    try:

        x,y,w,h = int(el[6]),int(el[7]),int(el[8]),int(el[9])
        cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
        cv2.putText(img, el[11], (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 1)
    except IndexError:
        print("tra vrov") 


cv2.imshow('Result', img)
cv2.waitKey(0)
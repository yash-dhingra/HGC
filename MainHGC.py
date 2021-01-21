import cv2
import numpy as np
from pynput.keyboard import Key, Controller
import time

cap = cv2.VideoCapture(1)
handcascade = cv2.CascadeClassifier(r'C:\Users\yashd\Documents\Python\OpenCV\Hand.xml')
keyboard = Controller()
time.sleep(7)
while True:
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hands = handcascade.detectMultiScale(gray,1.3,5)
    cv2.line(img, (200, 0), (200, 700), (0, 255, 0), 2)
    cv2.line(img, (410, 0), (410, 700), (0, 255, 0), 2)
    cv2.line(img, (0, 200), (700, 200), (0, 255, 0), 2)
    cv2.putText(img, "Copyright: Yash Dh", (340, 470), cv2.QT_FONT_NORMAL, 1, (255, 0, 0), 2)
    #keyboard.press('p')
    for (x,y,w,h) in hands:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img,"Active",(30,30),cv2.QT_FONT_NORMAL,1,(0,0,255),2)
        print(x,y,x+w,y+h)
        #keyboard.release(('p'))
        if x<100:
            print("Right Arrow Key")
            #keyboard.press(Key.right)
        if x>400:
            print("Left Arrow Key")
            #keyboard.press(Key.left)
        if y<190:
            print("Up Arrow Key")
            #keyboard.press(Key.up)


    cv2.imshow("Image",img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
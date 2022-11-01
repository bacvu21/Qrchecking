

from sre_constants import SUCCESS
import cv2 
import numpy as np 
from pyzbar.pyzbar import decode 
from controller import runRelay_on,runRelay_off




cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

with open ('D:\projectlinhtinh\python\Qrcheck\output1.txt') as f:
    output1 = f.read().splitlines()
print(output1)




while True:
    SUCCESS,img = cap.read()
    for barcode in decode (img):
        myData = barcode.data.decode ('utf-8')
        print(myData)
        if myData in output1:
            out_Put = "Ok!"
            myColor = (0,255,0)
            runRelay_on()
        else :
            out_Put ="Sai Qr_code ! xin dung ma khac !"
            myColor =(0,0,255)
            runRelay_off()
        pts =np.array([barcode.polygon],np.int32)
        pts =pts.reshape((-1,1,2))
        pts2 =barcode.rect
        
        cv2.polylines(img,[pts],True,(225,0,225),5)
        cv2.putText(img,out_Put,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.9,myColor,2)



    cv2.imshow('Result',img)
    if cv2.waitKey(1)==ord('q'):
            break;
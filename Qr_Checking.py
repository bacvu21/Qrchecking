

#các thư viện được sử dụng trong python 
from sre_constants import SUCCESS

import cv2 #Thư viện mã nguồn mở opencv 

import numpy as np   #thư viện thuật toán  cho phép phân tích hình ảnh thành ma trận số
from pyzbar.pyzbar import decode #thư viện đọc dữ liệu và biên dịch mã Qr
from controller import runRelay_on1,runRelay_on2,runRelay_on3,runRelay_on4,runRelay_off,runRelay_off1,runRelay_off2,runRelay_off3,runRelay_off4,delay#mở file controller 



#cho phép sử dụng camera của máy tính 
cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)
#cài đặt khung hình 


#cho phép lưu dữ liệu tại file output
with open ('D:\projectlinhtinh\python\Qrcheck\output1.txt') as f:
    output1 = f.read().splitlines()
    print(output1)

   
    

#đọc dữ liệu tại mã Qr và kiểm tra 
while True:
    SUCCESS,img = cap.read()
    for barcode in decode (img):
        myData = barcode.data.decode ('utf-8')
        print(myData)
        
        datafromfile=np.loadtxt("output1.txt",dtype="str")
    

        if myData == datafromfile[0]: 
            out_Put = "Ok1"
            myColor = (0,255,0)
            runRelay_on1()
            runRelay_off2()
            runRelay_off3()
            runRelay_off4()
            delay(3 )
        elif myData == datafromfile[1]:
             out_Put = "Ok2"
             myColor = (0,255,0)
             runRelay_on2()
             runRelay_off1()
             runRelay_off3()
             runRelay_off4()
             delay(3)
        elif myData == datafromfile[2]:
             out_Put = "Ok3"
             myColor = (0,255,0)
             runRelay_on3()
             runRelay_off1()
             runRelay_off4()
             runRelay_off2()
             delay(3)
        elif myData == datafromfile[3]:
             out_Put = "Ok4"
             myColor = (0,255,0)
             runRelay_on4()
             runRelay_off1()
             runRelay_off2()
             runRelay_off3()
             delay(3)
        else :
            out_Put ="Sai Qr_code ! xin dung ma khac !"
            myColor =(0,0,255)
            runRelay_off()
        pts =np.array([barcode.polygon],np.int32)
        pts =pts.reshape((-1,1,2))
        pts2 =barcode.rect
#vẽ khung viền và trả về kết quả 
        cv2.polylines(img,[pts],True,(225,0,225),5)
        cv2.putText(img,out_Put,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.9,myColor,2)



    cv2.imshow('Result',img)
    if cv2.waitKey(1)==ord('q'):
            break;
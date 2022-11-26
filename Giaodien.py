
from cProfile import label
import tkinter as tk 
from tkinter import  filedialog ,Text
import os
from tkinter import font 
from PIL import Image,ImageDraw,ImageFont
from PIL import ImageTk
from matplotlib import image


root = tk.Tk()
apps =[]


if os.path.isfile('D:\projectlinhtinh\python\Qrcheck\save.txt'):
        with open('D:\projectlinhtinh\python\Qrcheck\save.txt','r') as f:
                TempApps = f.read()
                TempApps = TempApps.split(',')
                apps = [x for x in TempApps if x.strip()]

def add_App():
    for widget in frame.winfo_children():
        widget.destroy()

    fileName =filedialog.askopenfilename(initialdir ="/",title ="Select file",
                                         filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(fileName) 
      
    print(fileName)
 #   for app in apps:
 #       label = tk.Label(frame, text = app, bg ="gray")
 #       label.pack()
    

def runApps():
        for app in apps:
            os.startfile(app)
            
            
            
canvas = tk.Canvas(root ,height= 500 , width= 700 , bg ="#263D45")
canvas.pack(side ='top')
canvas.create_text(360,50,  font = ("Arial", 20, "bold"), text = "Chương Trình quét mã Qr" ,fill = 'red')
canvas.create_text(370,20,  font = ("Arial", 20, "bold"), text = "Đại Học Sư Phạm Kỹ Thuật Hưng Yên" ,fill = 'red')
canvas.create_text(220,150, font=("Arial", 10, "bold"), text = "GIÁO VIÊN HƯỚNG DẪN :" ,fill = 'white')
canvas.create_text(400,150, font=("Arial", 10, "bold"), text = "TH.s TRỊNH THANH NGA " ,fill = 'red')
canvas.create_text(210,220, font=("Arial", 10, "bold"), text = "Sinh Viên Thực Hiện :" ,fill = 'white')
canvas.create_text(390,220, font=("Arial", 10, "bold"), text = "Đỗ Hồng Quân      -lớp 110194" ,fill = 'white')
canvas.create_text(390,240, font=("Arial", 10, "bold"), text = "Nguyễn ĐỨc Thảo -lớp 110194" ,fill = 'white')
canvas.create_text(165,180, font=("Arial", 10, "bold"), text = "Đề Tài:" ,fill = 'white')
canvas.create_text(360,180, font=("Arial", 10, "bold"), text = "Quét mã QR điều khiển đóng ngắt rơ-le " ,fill = 'red')






pilImage = Image.open("D:\projectlinhtinh\python\Qrcheck\logo.jfif")   
pilImage = pilImage.resize((100, 100), Image.ANTIALIAS)
logo= ImageTk.PhotoImage(pilImage) 
label1 = tk.Label(image = logo)
label1.image = logo
label1.place(x=0, y=0)      








openFile = tk.Button(root , text ="mở tập tin",padx =10,pady =5,
                     fg="white",bg="#263D42" ,command=add_App)
openFile.pack()




runApps = tk.Button(root , text ="Chạy chương trình ",padx =10,pady =5,fg="white",bg="#263D42" ,command = runApps)
runApps.pack()

frame =tk.Frame(canvas)


for app in apps:
        label =tk.Label(frame, text =app)
        label.pack()

root.mainloop()


with open ('D:\projectlinhtinh\python\Qrcheck\save.txt','w') as f:
        for app in apps:
                f.write(app+',')


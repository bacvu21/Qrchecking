import tkinter as tk 
from tkinter import  filedialog ,Text
import os 


root = tk.Tk()
apps =[]

def add_App():
    for widget in frame.winfo_children():
            widget.destroy()

    fileName =filedialog.askopenfilename(initialdir ="/",title ="select file",
                                         filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(fileName)   
    print(fileName)
    
    for app in apps:
        label = tk.Label(frame,text = app,bg ="gray")
        label.pack()
    

def runApps():
        for app in apps:
            os.startfile(app)
            
            
canvas = tk.Canvas(root ,height= 500 , width= 700 , bg ="#263D42")
canvas.pack(side ='top')
canvas.create_text(350,30, font=("Arial", 20, "bold"), text = "Chương trình phát hiện mã Qr" ,fill = 'red')


frame = tk.Frame(root , bg ="white")
frame.place (relwidth= 0.8 ,relheight=0.8,relx=0.1,rely=0.1)

openFile = tk.Button(root , text ="mở tập tin",padx =10,pady =5,
                     fg="white",bg="#263D42" ,command=add_App)
openFile.pack()




runApps = tk.Button(root , text ="Chạy chương trình ",padx =10,pady =5,fg="white",bg="#263D42" ,command = runApps)
runApps.pack()

frame =tk.Frame(canvas)

root.mainloop()





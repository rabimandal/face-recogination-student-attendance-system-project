from tkinter import *    
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import tkinter
import os
from student import Student 
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from train import Train

 
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recogonition_System")
        
# This part is image labels setting start 
        # first header image          
        img=Image.open(r"college_images\attendance2.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        # set image as lable        
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open(r"college_images\attendance1.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
         
        f_lb1 = Label(self.root,image=self.photoimg1)
        f_lb1.place(x=500,y=0,width=500,height=130)
        
        
        #third image
        img2=Image.open(r"college_images\attendance3.png")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
               
        f_lb1 = Label(self.root,image=self.photoimg2)
        f_lb1.place(x=1000,y=0,width=550,height=130)
        
        
        ## backgorund image 
        img3=Image.open(r"college_images\background.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
               
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        #title section
        title_lb1 = Label(bg_img,text="Attendance Managment System Using Facial Recognition",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)
        
        #=========time===========
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
            
        lbl = Label(title_lb1,font=("times new roman",14,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()
            
        
        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        img4=Image.open(r"college_images\std1.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,height=220)
        
        b1_1 = Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        # Detect Face  button 2
        img5=Image.open(r"college_images\det1.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,height=220)
        
        b1_1 = Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        # Attendance System  button 3
        img6=Image.open(r"college_images\att.png")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,height=220)
        
        b1_1 = Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attendance_data,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        # Help  Support  button 4
        img7=Image.open(r"college_images\help.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,height=220)
        
        b1_1 = Button(bg_img,text="HELP DESK",cursor="hand2",command=self.help_data,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        #Train face button 5
        img8=Image.open(r"college_images\tra1.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,height=220)
        
        b1_1 = Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        b1_1.place(x=200,y=580,width=220,height=40)
        
        #photo button 6
        img9=Image.open(r"college_images\dataset.png")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,height=220)
        
        b1_1 = Button(bg_img,text="DATA SET",cursor="hand2",command=self.open_img,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        b1_1.place(x=500,y=580,width=220,height=40)
        
        # Developers   button 7
        img10=Image.open(r"college_images\develop.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,height=220)
        
        b1_1 = Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.developer_data,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        #exit   button 8
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iEXit)
        b1.place(x=1100,y=380,height=220)
        
        b1_1 = Button(bg_img,text="EXIT",cursor="hand2",command=self.iEXit,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        b1_1.place(x=1100,y=580,width=220,height=40)
        
    # ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data") 
        
    def iEXit(self):
        self.iEXit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)  
        if self.iEXit >0:
           self.root.destroy()
        else:
            return
            
          
        
        
    # ==================Functions Buttons=====================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)  
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)  
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)                   
          
    
        
      
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()        
 
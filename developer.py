from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recogonition_System")
        
        
        #title section
        title_lb1 = Label(self.root,text="DEVELOPER",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)
        
        #back button
        b1=Button(title_lb1,text="back",command=self.back,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        b1.place(x=1400,y=2,width=110,height=35)
        
        #first image
        img_top=Image.open(r"college_images\devp.jpg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
               
        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1530,height=720)
        
        # Frame 
        main_frame = Frame(f_lb1,bd=2,bg="white") #bd mean border 
        main_frame.place(x=1000,y=0,width=500,height=600)
        
        img_top1=Image.open(r"college_images\develop.jpg")
        img_top1=img_top1.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
               
        f_lb1 = Label(main_frame,image=self.photoimg_top1)
        f_lb1.place(x=300,y=0,width=200,height=200)
        
        
        #Developer info
        dep_label=Label(main_frame,text="hello my name is,Rabi",font=("verdana",15,"bold"),bg="white",fg="navyblue")
        dep_label.place(x=0,y=5)
        
        dep_label=Label(main_frame,text="...",font=("verdana",15,"bold"),bg="white",fg="navyblue")
        dep_label.place(x=0,y=40)
        
        img2=Image.open(r"college_images\developers.jpg")
        img2=img2.resize((500,390),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
               
        f_lb1 = Label(main_frame,image=self.photoimg2)
        f_lb1.place(x=0,y=210,width=500,height=390)
        
    def back(self):
        self.root.destroy()     
        
        
if __name__ == "__main__":
     root=Tk()
     obj=Developer(root)
     root.mainloop()        
         
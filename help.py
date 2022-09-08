from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recogonition_System")
        
        
        #title section
        title_lb1 = Label(self.root,text="HELP DESK",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)
        
        #back button
        b1=Button(title_lb1,text="back",command=self.back,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        b1.place(x=1400,y=2,width=110,height=35)
        
        #first image
        img_top=Image.open(r"college_images\tec.jpg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
               
        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1530,height=720)
        
        dep_label=Label(f_lb1,text="Email: hellorabi.mandal@gmail.com",font=("verdana",15,"bold"),bg="white",fg="navyblue")
        dep_label.place(x=500,y=300)
        
    def back(self):
        self.root.destroy()    
        
        
if __name__ == "__main__":
     root=Tk()
     obj=Help(root)
     root.mainloop()           
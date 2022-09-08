from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import cv2
import os
import numpy as np
from tkinter import messagebox


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recogonition_System")
        
        
        #title section
        title_lb1 = Label(self.root,text="TRAIN DATA SET",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)
        
        #back button
        b1=Button(title_lb1,text="back",command=self.back,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        b1.place(x=1400,y=2,width=110,height=35) 
        
        #first image
        img_top=Image.open(r"college_images\train1.jpg")
        img_top=img_top.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
               
        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1530,height=325)
        
        #button
        b1_1 = Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("tahoma",30,"bold"),bg="navyblue",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)
        
        
        #second image
        img_bottom=Image.open(r"college_images\train2.jpg")
        img_bottom= img_bottom.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage( img_bottom)
               
        f_lb1 = Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x=0,y=440,width=1530,height=325)
        
    # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # convert in gray scale  image
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids) 
        
        #=================Train Classifier=============
        clf =cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)
   
    def back(self):
        self.root.destroy()     
       
        
        
        
        
        
if __name__ == "__main__":
     root=Tk()
     obj=Train(root)
     root.mainloop()        
        
        
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
#from cv2 import ROTATE_90_CLOCKWISE
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

#Global variable for importCsv Function 
mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recogonition_System")
        
        #-----------Variables-------------------
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        
        
        
        # first  image        
        img=Image.open(r"college_images\fr1.jpg")
        img=img.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        # set image as lable        
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=800,height=200)
        
        #second image
        img1=Image.open(r"college_images\temp.jpg")
        img1=img1.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
           
        f_lb1 = Label(self.root,image=self.photoimg1)
        f_lb1.place(x=800,y=0,width=800,height=200)
        
        ## backgorund image 
        img3=Image.open(r"college_images\bg2.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
               
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)
        
        #title section
        title_lb1 = Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)
        
        #back button
        b1=Button(title_lb1,text="back",command=self.back,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        b1.place(x=1400,y=2,width=110,height=35)
        
         
        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=10,y=55,width=1500,height=600)
        
        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=740,height=580)
        
        #inside image
        img_left=Image.open(r"college_images\attendance3.png")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
                
        f_lb1 = Label(left_frame,image=self.photoimg_left)
        f_lb1.place(x=5,y=0,width=720,height=130)
        
        #inside frame
        left_inside_frame = Frame(left_frame,relief=RIDGE,bd=2,bg="white")  
        left_inside_frame.place(x=0,y=135,width=720,height=370)
        
        #Label and entry
        #Student id
        attendanceID_label = Label(left_inside_frame,text="AttendanceID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_id,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #Roll
        rollLabel = Label(left_inside_frame,text="Roll:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        rollLabel.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        atten_roll = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_roll,font=("verdana",12,"bold"))
        atten_roll.grid(row=0,column=3,pady=8)
        
        #Name
        nameLabel = Label(left_inside_frame,text="Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        nameLabel.grid(row=1,column=0)

        atten_name = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_name,font=("verdana",12,"bold"))
        atten_name.grid(row=1,column=1,pady=8)
        
        #Department
        depLabel = Label(left_inside_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        depLabel.grid(row=1,column=2)

        atten_dep = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_dep,font=("verdana",12,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)
        
        #time
        depLabel = Label(left_inside_frame,text="Time:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        depLabel.grid(row=2,column=0)

        atten_dep = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_time,font=("verdana",12,"bold"))
        atten_dep.grid(row=2,column=1,pady=8)
        
        #Date
        depLabel = Label(left_inside_frame,text="Date:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        depLabel.grid(row=2,column=2)

        atten_dep = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_date,font=("verdana",12,"bold"))
        atten_dep.grid(row=2,column=3,pady=8)
        
        #Attendance
        depLabel = Label(left_inside_frame,text="Attendance:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        depLabel.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("verdana",12,"bold"),state="readonly")
        self.atten_status["values"]=("status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        #Button Frame
        btn_frame = Frame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=290,width=715,height=35)

        #import button
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=15,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0)

        #export button
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=15,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1)

        #update button
        del_btn=Button(btn_frame,text="Update",width=15,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3)
        
       
        
        
        #----------------------------------------------------------------------
        # Right Label Frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
        Right_frame.place(x=755,y=10,width=720,height=580)
        
        table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=700,height=455)
        
        #========scroll bar table======= 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
       
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    # =========Fetch Data Import data===========    
    def fetchData(self,rows):
      #  global mydata
      #  mydata = rows
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
         #   print(i)
        
    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)  
        
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found To Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 
                
                
    #=============Cursur Function for CSV========================
    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows= content["values"]

        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4]) 
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6]) 
        
        
    #============================Reset Data======================
    def reset_data(self): 
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("") 
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
                    
    def back(self):
        self.root.destroy()            
                   
   
        
        
        
if __name__ == "__main__":
     root=Tk()
     obj=Attendance(root)
     root.mainloop()        
         
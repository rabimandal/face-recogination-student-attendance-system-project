from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")
        
        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_Q=StringVar()
        self.var_security_A=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        
        
        
        #background image
        self.bg=ImageTk.PhotoImage(file=r"college_images\loginBg1.jpg")
               
        lb1_bg = Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        
        frame= Frame(self.root,bg="#F2F2F2")
        frame.place(x=100,y=80,width=900,height=580)
        
        register_lbl = Label(frame,text="Registration",font=("times new roman",30,"bold"),fg="#002B53",bg="#F2F2F2")
        register_lbl.place(x=350,y=130)
        
        #label1 
        fname =lb1= Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=100,y=200)


        #entry1 
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=103,y=225,width=270)
        

        #label2 
        l_name =lb1= Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        l_name.place(x=100,y=270)

        #entry2 
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=103,y=295,width=270)
        
         # ==================== section 2 -------- 2nd Columan===================

        #label1 
        contact=lb1= Label(frame,text="Contact No:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        contact.place(x=530,y=200)

        #entry1 
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=533,y=225,width=270)


        #label2 
        email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=530,y=270)

        #entry2 
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=533,y=295,width=270)
        
        
        # ========================= Section 3 --- 1 Columan=================

        #label1 
        security_Q =lb1= Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        security_Q.place(x=100,y=350)

        #Combo Box1
        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_security_Q,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=103,y=375,width=270)


        #label2 
        security_A =lb1= Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        security_A.place(x=100,y=420)

        #entry2 
        self.txt_security=ttk.Entry(frame,textvariable=self.var_security_A,font=("times new roman",15,"bold"))
        self.txt_security.place(x=103,y=445,width=270)
        
          # ========================= Section 4-----Column 2=============================

        #label1 
        pswd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pswd.place(x=530,y=350)

        #entry1 
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=533,y=375,width=270)


        #label2 
        confirm_pswd =lb1= Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        confirm_pswd.place(x=530,y=420)

        #entry2 
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=533,y=445,width=270)
        
        
        # Checkbutton
        self.checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"))
        self.checkbtn.place(x=100,y=480,width=270)


        # Creating Button Register
        b1=Button(frame,command=self.register_data,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        b1.place(x=103,y=510,width=270,height=35)

        # Creating Button Login
        b1=Button(frame,text="Login",command=self.return_login,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        b1.place(x=533,y=510,width=270,height=35)
        
    def register_data(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_security_Q.get()=="Select" ):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_pass.get() != self.var_confpass.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
        else:
            conn = mysql.connector.connect(host='localhost',username='root', password='4609',database='mydata')
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                self.var_fname.get(),
                self.var_lname.get(),
                self.var_contact.get(),
                self.var_email.get(),
                self.var_security_Q.get(),
                self.var_security_A.get(),
                self.var_pass.get()
                ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
        #except Exception as es:
               # messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 
            
    def return_login(self):
        self.root.destroy()
    

        
        

        
     

        
        
    
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()        
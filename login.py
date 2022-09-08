from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
from main import Face_Recognition_System


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        #variables
        self.var_email=StringVar()
        self.var_pass=StringVar()
        
      
        self.bg=ImageTk.PhotoImage(file=r"college_images\loginBg1.jpg")
               
        lb1_bg = Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame= Frame(self.root,bg="#002B53")
        frame.place(x=610,y=170,width=340,height=450)
        
        img=Image.open(r"college_images\log1.png")
        img=img.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
                
        f_lb1 = Label(self.root,image=self.photoimg,bg="#002B53",borderwidth=0)
        f_lb1.place(x=730,y=175,width=100,height=100)
        
        get_str = Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=95,y=100)
        
        #label1 
        username =lb1= Label(frame,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        username.place(x=40,y=155)

        #entry1 
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        #label2
        password =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        password.place(x=40,y=225)

        #entry2
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        
        # Creating Button Login
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=110,y=300,width=120,height=35)


        # Creating Button Registration
        registerbtn=Button(frame,text=" New User Register",command=self.register_window,font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        registerbtn.place(x=15,y=350,width=160)


        # Creating Button Forget
        forgetbtn=Button(frame,text="Forget Password",command=self.forget_password_window,font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        forgetbtn.place(x=10,y=370,width=160)
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
        
        
    def login(self):
        if (self.txtuser.get()=="" or self.txtpass.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="admin":
             messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            conn = mysql.connector.connect(host='localhost',username='root', password='4609',database='mydata')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                
                                                                               ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            
 #=======================Reset Passowrd Function=============================           
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.txt_security.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.txt_newpass.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(host='localhost',username='root', password='4609',database='mydata')
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                self.root2.destroy()
        
            
            
            
            
            
            
            
   
# =====================Forget window=========================================
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(host='localhost',username='root', password='4609',database='mydata')
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                    messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                
                 # -------------------fields-------------------
                #label1 
                security_Q= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                security_Q.place(x=50,y=80)

                #Combo Box1
                self.combo_security_Q = ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=50,y=110,width=270)
                
                #label2 
                security_A= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                security_A.place(x=50,y=150)

                #entry2 
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                #label2 
                new_password =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_password.place(x=50,y=220)

                #entry2 
                self.txt_newpass=ttk.Entry(self.root2,textvariable=self.var_pass,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)
                
                # Creating Button New Password
                btn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                btn.place(x=100,y=290)


            
        
        
        
        
        
     


if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()
    
    
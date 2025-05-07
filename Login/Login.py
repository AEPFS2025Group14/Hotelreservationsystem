from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
    ##900x500

        self.bg=ImageTk.PhotoImage(file=r"D:\bilder\caption-2.jpg")

        lbl_bh=Label(self.root,image=self.bg)
        lbl_bh.place(x=0, y=0,relwidth=1, relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"D:\bilder\e56b841924ac729935e858cb59535fb7.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=170,width=100,height=100)

        get_str=Label(frame,text= "Get Started", font=("arial",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="Username", font=("arial",15,"bold"),fg="white",bg="black")
        username.place(x=37,y=155)
        self.txtuser=ttk.Entry(frame, font=("arial",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password = lbl = Label(frame, text="Password", font=("arial", 15, "bold"), fg="white", bg="black")
        password.place(x=37, y=225)
        self.txtpass = ttk.Entry(frame, font=("arial", 15, "bold"))
        self.txtpass.place(x=40 , y=250, width=270  )

        #LoginButton
        loginbtn=Button(frame, command=self.login,text="Login",font=("arial",15,"bold"), bd=3,relief= RIDGE,fg="white",bg="red", activeforeground="white",activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        #RegisterButton
        Registerbtn = Button(frame, text="New User Register",font=("arial", 10, "bold"), borderwidth=0, relief=RIDGE, fg="white", bg="black",activeforeground="white", activebackground="black")
        Registerbtn.place(x=15, y=350, width=160)

        # ForgotPosswortButton
        loginbtn = Button(frame, text="Forgot Password", font=("arial", 10, "bold"), borderwidth=0, fg="white", bg="black",activeforeground="white", activebackground="black")
        loginbtn.place(x=10, y=370, width=160)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","Please enter your username and password")
        elif self.txtuser.get()=="Username" and self.txtpass.get()=="Password":
            messagebox.showinfo("Success")
        else:
            messagebox.showerror("Error","Wrong username and password")



if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
from tkinter import *
import time
from sqlite3 import *
import random
from tkinter import messagebox

class Pizza:
    cartlist=[]
    amount=0

    

#--  Main Page------
    def main(root):
        try:
            root.scr.destroy()
            root.scr=Tk()
        except:
            try:
                root.scr=Tk()
            except:
                pass
            
        root.setFrame()
        root.scr.title("Mighty's Pizza")
        # Login Button
        root.btn_login=Button(root.win_main,text="Login",cursor="hand2",command=lambda:root.Login(),fg="white",bg="#0b1335",font=("algerian",20),bd=4)
        # Login Button placement
        root.btn_login.place(x=570,y=375)

        # Guest login button
        root.btn_login_guest=Button(root.win_main,text="Continue as guest",cursor="hand2",command=lambda:root.pizmain(),fg="white",bg="#0b1335",font=("algerian",20),bd=4)
        # Guest login button placement
        root.btn_login_guest.place(x=150,y=375)
        # Guest login button is disabled because pizmain() is not setup yet
        root.btn_login_guest["state"] = "disabled"
        

        # Set lbl_mighty label text to "Welcome to Mighty Pizza,"
        root.lbl_mighty=Label(root.win_main,text="Welcome to Mighty Pizza,",font=("algerian",22))
        # Placement of lbl_mighty
        root.lbl_mighty.place(x=0,y=200)
        # Set lbl_mighty2 label text to "To continue, either login or click the guest option."
        root.lbl_mighty2=Label(root.win_main,text="To continue, either login or click the guest option.",font=("algerian",22))
        root.lbl_mighty2.place(x=0,y=250)

        root.win_main.pack(fill=BOTH,expand=1)
        root.scr.mainloop()
        #root.Login()
        root.scr.mainloop()

#------ Login page ------
    def Login(root):
        root.setFrame()
        root.scr.title("Mighty's Pizza")
        root.btn_home=Button(root.win_main,text="Home",command=lambda:root.main(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_home.place(x=720,y=0)

        root.log=Label(root.win_main,text="LOGIN",fg="white",bg="#0b1335",width=26,font=("algerian",27))
        root.log.place(x=100,y=175)
        root.lab1=Label(root.win_main,text="UserName",bg="#d3ede6",font=("algerian",22))
        root.lab1.place(x=100,y=250)
        root.user=Entry(root.win_main,bg="white",font=("algerian",22),bd=6 ,justify='left')
        root.user.place(x=320,y=250)
        root.lab2=Label(root.win_main,text="Password",bg="#d3ede6",font=("algerian",22))
        root.lab2.place(x=105,y=325)
        root.pasd=Entry(root.win_main,bg="white",font=("algerian",22),bd=6 ,justify='left')
        root.pasd.place(x=320,y=325)
        root.lg=Button(root.win_main,text="Login",cursor="hand2",command=lambda:root.errMsg(),fg="white",bg="#0b1335",font=("algerian",20),bd=4)
        root.lg.place(x=570,y=375)
        def clear(root):
            root.user.delete(0,END)
            root.pasd.delete(0,END)
        root.cl=Button(root.win_main,text="Clear",cursor="hand2",command=lambda:clear(root),fg="white",bg="#0b1335",font=("algerian",20),bd=4)
        root.cl.place(x=450,y=375)


        root.win_main.pack(fill=BOTH,expand=1)
        root.scr.mainloop()
    def resultlog(root):
        root.loguser=root.user.get()
        root.logpass=root.pasd.get()
        return root.loguser,root.logpass

    def errMsg(root):
        root.scr1=Tk()
        root.L=Label(root.scr1,text="Coming soon")
        root.L.pack()
        root.scr1.mainloop()
    def about(root):
        root.scr1=Tk()
        # Set lbl_mighty to "Mighty Pizza"
        root.lbl_about_app=Label(root.scr1,text="App Name: ",font=("times",12))
        # Place lbl_mighty at x=160,y=10
        root.lbl_about_app.place(x=5,y=10)
        # Set lbl_mighty to "Mighty Pizza"
        root.lbl_about_app2=Label(root.scr1,text="Mighty Pizza ",font=("times",12))
        # Place lbl_mighty at x=160,y=10
        root.lbl_about_app2.place(x=125,y=10)
        # Set lbl_mighty to "Mighty Pizza"
        root.lbl_version=Label(root.scr1,text="App Version: ",font=("times",12))
        # Place lbl_mighty at x=160,y=10
        root.lbl_version.place(x=5,y=50)
        # Set lbl_mighty to "Mighty Pizza"
        root.lbl_version2=Label(root.scr1,text="0.1",font=("times",12))
        # Place lbl_mighty at x=160,y=10
        root.lbl_version2.place(x=125,y=50)
    
        root.scr1.mainloop()
        
    def setFrame(root):
        root.cartlist=[]
        root.amount=0
        root.scr.destroy()
        root.scr=Tk()
        
        # Window Size
        root.scr.geometry("800x600")
        # Set window resizable to false
        root.scr.resizable(False, False)
        # Set the frame size
        root.win_main=Frame(root.scr,height=800,width=600)
        # Open banner image
        root.imgpizzabanner=PhotoImage(file="res/pizzabanner.png")
        # Set "imgpizzabanner" image in label "lbl_banner"
        root.lbl_banner=Label(root.win_main,image=root.imgpizzabanner,height=150,width=800).place(x=0,y=0)
        # Open logo image
        root.imgLogo=PhotoImage(file="res/logo.png")
        # Set "imgLogo" image in label "lbl_logo"
        root.lbl_logo=Label(root.win_main,image=root.imgLogo,height=150,width=150).place(x=0,y=0)
        # Set lbl_mighty to "Mighty Pizza"
        root.lbl_mighty=Label(root.win_main,text="Mighty Pizza",font=("algerian",22))
        # Place lbl_mighty at x=160,y=10
        root.lbl_mighty.place(x=160,y=10)

        # Admin login button
        root.btn_adminLog=Button(root.win_main,text="Administrator Login",command=lambda:root.Adminlogin(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_adminLog.place(x=550,y=100)

        # Admin button is disabled because AdminLogin is not setup yet
        root.btn_adminLog["state"] = "disabled"

        # About button
        root.btn_about=Button(root.win_main,text="About Us",bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("algerian",16))
        root.btn_about.config(command=lambda:root.about())
        # About button placement
        root.btn_about.place(x=675,y=50)

        # Top pizza banner 
        root.imgpizzabanner2=PhotoImage(file="res/bgpizza.png")
        # Top pizza banner placement
        root.lbl_banner2=Label(root.win_main,image=root.imgpizzabanner2,height=600,width=800).place(x=0,y=150)


x=Pizza()
x.main()

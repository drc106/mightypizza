"""
    App Name:       Mighty Pizza
    Writen by:      D Cravens
    Date created:   11-17-2022
    Revised date:   12-18-2022
    Description :   The pizza delivery app Mighty Pizza makes it easy to get your pizza fix without leaving the house.

"""
from tkinter import *
from sqlite3 import *
from tkinter import messagebox
import CustomerClass
import VaidInput

user = CustomerClass.Customer()

# Pizza Class
class Pizza:
    # Variables
    cartlist=[] 
    # amount 
    amount=0
    deliveryMethod:str = "Carry-Out Or Delivery" # Set the variable deliveryMethod 
    deliveryFee: float = 2.50 # deliveryFee is a float that holds the delivery fee of 2.50
    taxRate: float = 0.07 # taxRate is a float that holds the tax rate of 0.07 
    vInput = VaidInput.VaidInput() # Set the value of vInput to  VaidInput.VaidInput()
    rtitle = "" # Holds current window title

    # createNewWindow is an function to create a new frame
    def createNewWindow(self, title: str, changeTitle: bool = True):
        
        self.scr.geometry("800x600") # Window Size
        
        self.scr.resizable(False, False) # Set window resizable to false
         
        self.setFrame() # Set tkinter frame
        if changeTitle == True: # Check the changeTile variable to see if it True. If true change the window title.
            
            self.scr.title(title + "(" + self.deliveryMethod + ")")# Set window title
        else:
           
            self.scr.title(title) # Set window title
        
        self.rtitle = str(title)# Set current window title

#--  Main Start------
    def main(root):
        
        try:
            root.scr.destroy()
            root.scr=Tk()
        except:
            try:
                root.scr=Tk()
            except:
                pass
        root.Login()

#------ Login Screen ------
    def Login(root):
        root.setFrame()# Set frame
        root.scr.title("Mighty's Pizza - Login")# Set window tilte
        root.lbl_login=Label(root.win_main,text="LOGIN",fg="white",bg="#0b1335",width=26,font=("algerian",27))# Create a label and have the text of "LOGIN"
        root.lbl_login.place(x=100,y=175)# Set LOGIN label placement
        root.lbl_username=Label(root.win_main,text="Username",bg="#d3ede6",font=("algerian",22))# Create a label and have a text of "Username"
        root.lbl_username.place(x=100,y=250)# Set Username label placement
        root.user=Entry(root.win_main,bg="white",font=("algerian",22),bd=6 ,justify='left')# Create a input for username, this will allow users to input their username in a textbox
        root.user.place(x=320,y=250)# Set username textbox placement
        root.lab2=Label(root.win_main,text="Password",bg="#d3ede6",font=("algerian",22))# Create a lebal for Password
        root.lab2.place(x=105,y=325)# Set Password label placement
        root.pasd=Entry(root.win_main,bg="white", show="*", font=("algerian",22),bd=6 ,justify='left')# Create a textbox for Password, this will allow users to input their password into a textbox
        root.pasd.place(x=320,y=325)# Set Password textbox placement
        root.lg=Button(root.win_main,text="Login",cursor="hand2",command=lambda:root.usr_login(root.user.get(), root.pasd.get()),fg="white",bg="#0b1335",font=("algerian",20),bd=4)# Create a button and name it "Login", this button will call the Function usr_login
        root.lg.place(x=570,y=375)# Set the Login button placement
        root.btn_login_guest=Button(root.win_main,text="Continue as guest",cursor="hand2",command=lambda:root.guest_login(),fg="white",bg="#0b1335",font=("algerian",20),bd=4)# Create a Guest login button
        root.btn_login_guest.place(x=150,y=375)# Guest login button placement
        def clear(root): # clear is a Function that clears username and password textboxs
            root.user.delete(0,END)# Makes username text empty
            root.pasd.delete(0,END) # Makes password textbox empty
        root.cl=Button(root.win_main,text="Clear",cursor="hand2",command=lambda:clear(root),fg="white",bg="#0b1335",font=("algerian",20),bd=4)# Create a button and name it Clear, this button will call the Function clear()
        # Set the placement for the clear button
        root.cl.place(x=450,y=375)
        root.win_main.pack(fill=BOTH,expand=1)
        root.scr.mainloop()
    def resultlog(root):
        root.loguser=root.user.get()
        root.logpass=root.pasd.get()
        return root.loguser,root.logpass

    def errMsg(root):
        messagebox.showinfo("Info","This part is not finished coming soon.")
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
        # About button
        root.btn_about=Button(root.win_main,text="About Us",bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("algerian",16))
        root.btn_about.config(command=lambda:root.about())
        # About button placement
        root.btn_about.place(x=485,y=105)
        # Exit button
        root.btn_exit=Button(root.win_main,text="Exit",bg="Red",cursor="hand2",bd=4,fg="white",font=("algerian",16))
        root.btn_exit.config(command=lambda:root.exit_app())
        # Exit button placement
        root.btn_exit.place(x=720,y=105)
        # Logout button
        root.btn_logout=Button(root.win_main,text="Logout",command=lambda:root.Logout(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_logout.place(x=250,y=105)
        # Disable cart button 
        root.btn_logout["state"] = "disabled"
        # Back button
        root.btn_back=Button(root.win_main,text="Back",command=lambda:root.pizmain(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_back.place(x=160,y=105)
        # Disable cart button 
        root.btn_back["state"] = "disabled"
        # Cart button
        root.btn_cart=Button(root.win_main,text="My Cart",command=lambda:root.Orderde(root.x),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_cart.place(x=365,y=105)
         # Disable cart button 
        root.btn_cart["state"] = "disabled"

        # Top pizza banner 
        root.imgpizzabanner2=PhotoImage(file="res/bgpizza.png")
        # Top pizza banner placement
        root.lbl_banner2=Label(root.win_main,image=root.imgpizzabanner2,height=600,width=800).place(x=0,y=150)

#--  Pizza main Screen------
    def pizmain(root):
        root.scr.destroy()
        root.scr=Tk()
        root.rtitle = str(root.scr.title())
        root.scr.geometry("800x600")
        root.scr.resizable(False, False)
        root.createNewWindow("Mighty's Pizza - Delivery Method", False)

        root.pizf1=Frame(root.scr,height=150,width=600)
        root.c=Canvas(root.pizf1,height=150,width=600)
        root.c.pack()

         # Open banner image
        root.imgpizzabanner=PhotoImage(file="res/pizzabanner.png")
        # Set "imgpizzabanner" image in label "lbl_banner"
        root.lbl_banner=Label(root.pizf1,image=root.imgpizzabanner,height=150,width=800).place(x=0,y=0)
        # Open logo image
        root.imgLogo=PhotoImage(file="res/logo.png")
        # Set "imgLogo" image in label "lbl_logo"
        root.lbl_logo=Label(root.pizf1,image=root.imgLogo,height=150,width=150).place(x=0,y=0)
        # Set lbl_mighty to "Mighty Pizza"
        root.lbl_mighty=Label(root.pizf1,text="Mighty Pizza",font=("algerian",22))
        # Place lbl_mighty at x=160,y=10
        root.lbl_mighty.place(x=160,y=10)
        # Set lbl_welcome to "Welcome, (user first name)"
        root.lbl_welcome=Label(root.pizf1,text="Welcome, " + user.get_username(),font=("algerian",22))
        # Place lbl_mighty at x=160,y=10
        root.lbl_welcome.place(x=160,y=50)
        # About button
        root.btn_about=Button(root.pizf1,text="About Us",bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("algerian",16))
        root.btn_about.config(command=lambda:root.about())
        # About button placement
        root.btn_about.place(x=485,y=105)
        # Exit button
        root.btn_exit=Button(root.pizf1,text="Exit",bg="Red",cursor="hand2",bd=4,fg="white",font=("algerian",16))
        root.btn_exit.config(command=lambda:root.exit_app())
        # Exit button placement
        root.btn_exit.place(x=720,y=105)
        # Logout button
        root.btn_logout=Button(root.pizf1,text="Logout",command=lambda:root.Logout(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_logout.place(x=250,y=105)
        # Back button
        root.btn_back=Button(root.pizf1,text="Back",command=lambda:root.pizmain(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_back.place(x=160,y=105)
        # Disable back button
        root.btn_back["state"] = "disabled"
        # Cart button
        root.btn_cart=Button(root.pizf1,text="My Cart",command=lambda:root.Orderde(root.x),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_cart.place(x=365,y=105)
        if not root.cartlist:
            root.btn_cart["state"] = "disabled"

        root.pizf1.pack(fill=BOTH,expand=1)

        root.pizf2=Frame(root.scr,height=618,width=1366)
        root.c=Canvas(root.pizf2,height=618,width=1366)
        root.c.pack()
        root.logo1=PhotoImage(file="res/bgpizza.png")
        root.c.create_image(400,309,image=root.logo1)
        root.deli=PhotoImage(file="res/delivery.png")
        root.c.create_image(250,175,image=root.deli)
        root.pic=PhotoImage(file="res/pickup.png")
        root.c.create_image(550,175,image=root.pic)
        root.de=Button(root.pizf2,text="Delivery",cursor="hand2",fg="white",command=lambda:root.menulist("deli"),bg="#0b1335",font=("default",20),bd=5)
        root.de.place(x=175,y=325)
        root.pu=Button(root.pizf2,text="Pick Up",cursor="hand2",fg="white",command=lambda:root.menulist("pick"),bg="#0b1335",font=("default",20),bd=5)
        root.pu.place(x=490,y=325)
       
        
  
        root.pizf2.pack(fill=BOTH,expand=1)
        root.scr.mainloop()
#--  Menu list Screen------        
    def menulist(root,x):
        
        root.x=x
        root.scr.destroy()
        root.scr=Tk()
        
        if x == "deli":
            root.deliveryMethod = "Delivery"
        else:
            root.deliveryMethod = "Pick-Up"
        root.createNewWindow("Mighty's Pizza - Menu")
        root.menuf1=Frame(root.scr,height=150,width=1366)
        root.c=Canvas(root.menuf1,height=150,width=1366)
        root.c.pack()
        # Open banner image
        root.imgpizzabanner=PhotoImage(file="res/pizzabanner.png")
        # Set "imgpizzabanner" image in label "lbl_banner"
        root.lbl_banner=Label(root.menuf1,image=root.imgpizzabanner,height=150,width=800).place(x=0,y=0)
        # Open logo image
        root.imgLogo=PhotoImage(file="res/logo.png")
        # Set "imgLogo" image in label "lbl_logo"
        root.lbl_logo=Label(root.menuf1,image=root.imgLogo,height=150,width=150).place(x=0,y=0)
        # Set lbl_mighty to "Mighty Pizza"
        root.lbl_mighty=Label(root.menuf1,text="Mighty Pizza",font=("algerian",22))
        # Place lbl_mighty at x=160,y=10
        root.lbl_mighty.place(x=160,y=10)
        # About button
        root.btn_about=Button(root.menuf1,text="About Us",bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("algerian",16))
        root.btn_about.config(command=lambda:root.about())
        # About button placement
        root.btn_about.place(x=485,y=105)
        # Exit button
        root.btn_exit=Button(root.menuf1,text="Exit",bg="Red",cursor="hand2",bd=4,fg="white",font=("algerian",16))
        root.btn_exit.config(command=lambda:root.exit_app())
        # Exit button placement
        root.btn_exit.place(x=720,y=105)
        # Logout button
        root.btn_logout=Button(root.menuf1,text="Logout",command=lambda:root.Logout(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_logout.place(x=250,y=105)
        # Back button
        root.btn_back=Button(root.menuf1,text="Back",command=lambda:root.pizmain(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_back.place(x=160,y=105)
        # Cart button
        root.btn_cart=Button(root.menuf1,text="My Cart",command=lambda:root.Orderde(root.x),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_cart.place(x=365,y=105)
         # Disable cart button if its empty
        if not root.cartlist:
            root.btn_cart["state"] = "disabled"
        root.lbl_deliver=Label(root.menuf1,text="Delivery method: ",font=("times",12))
        root.lbl_deliver.place(x=580,y=5)
        #Set the Menu initially
        root.menu= StringVar()
        root.menu.set(root.deliveryMethod)
        
        root.drop= OptionMenu(root.menuf1, root.menu,"Delivery","Carry-out",command=root.delivery_method)
        root.drop.place(x=700,y=5)

        root.menuf1.pack(fill=BOTH,expand=1)

        root.menuf2=Frame(root.scr,height=618,width=1366)
        root.c=Canvas(root.menuf2,height=618,width=1366)
        root.c.pack()
        root.logo1=PhotoImage(file="res/bgpizza.png")
        root.c.create_image(600,309,image=root.logo1)
        root.veg=PhotoImage(file="res/veg.png")
        root.c.create_image(150,100,image=root.veg)
        root.vegbut=Button(root.menuf2,text="Veg Pizza",cursor="hand2",fg="white",command=lambda:root.vegpizza(root.x),bg="#0b1335",bd=5,font=("default",18,'bold'))
        root.vegbut.place(x=140,y=150)
        root.nonveg=PhotoImage(file="res/non-veg.png")
        root.c.create_image(150,325,image=root.nonveg)
        root.nonvegbut=Button(root.menuf2,text="Non-Veg Pizza",cursor="hand2",fg="white",command=lambda:root.nonvegpizza(root.x),bg="#0b1335",bd=5,font=("default",18,'bold'))
        root.nonvegbut.place(x=80,y=375)
        root.chi=PhotoImage(file="res/wings.png")
        root.c.create_image(650,100,image=root.chi)
        root.chibut=Button(root.menuf2,text="Special Chicken",cursor="hand2",fg="white",command=lambda:root.errMsg(),bg="#0b1335",bd=5,font=("default",18,'bold'))
        root.chibut.place(x=565,y=150)
        root.side=PhotoImage(file="res/extra.png")
        root.c.create_image(650,325,image=root.side)
        root.sidebut=Button(root.menuf2,text="Sides and Beverages",cursor="hand2",fg="white",command=lambda:root.errMsg(),bg="#0b1335",bd=5,font=("default",18,'bold'))
        root.sidebut.place(x=515,y=375)
        root.menuf2.pack(fill=BOTH,expand=1)
        root.scr.mainloop()
        
    # veg pizza screen
    def vegpizza(root,x):
        
        root.x=x
        root.scr.destroy()
        root.scr=Tk()
        root.createNewWindow("Mighty's Pizza - Veg Pizzas", True)
        root.scr.geometry("800x640")
        #root.scr.resizable(False, False)
        root.vegf1=Frame(root.scr,height=150,width=1366)
        root.c=Canvas(root.vegf1,height=150,width=1366)
        root.c.pack()
        
        root.logo=PhotoImage(file="res/pizzabanner.png")
        root.c.create_image(180,0,image=root.logo)
        # Open logo image
        root.imgLogo=PhotoImage(file="res/logo.png")
        # Set "imgLogo" image in label "lbl_logo"
        root.lbl_logo=Label(root.vegf1,image=root.imgLogo,height=150,width=150).place(x=0,y=0)
        root.btn_logout=Button(root.vegf1,text="Log Out",command=lambda:root.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        root.btn_logout.place(x=1000,y=90)
        
        # Set lbl_mighty to "Mighty Pizza"
        root.lbl_mighty=Label(root.vegf1,text="Mighty Pizza",font=("algerian",22))
        
        # Place lbl_mighty at x=160,y=10
        root.lbl_mighty.place(x=160,y=10)
        # Set lbl_welcome to "Welcome, (user first name)"
        root.lbl_welcome=Label(root.vegf1,text="Welcome, " + user.get_username(),font=("algerian",22))
        # Place lbl_mighty at x=160,y=10
        root.lbl_welcome.place(x=160,y=50)
        # About button
        root.btn_about=Button(root.vegf1,text="About Us",bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("algerian",16))
        root.btn_about.config(command=lambda:root.about())
        # About button placement
        root.btn_about.place(x=485,y=105)
        # Exit button
        root.btn_exit=Button(root.vegf1,text="Exit",bg="Red",cursor="hand2",bd=4,fg="white",font=("algerian",16))
        root.btn_exit.config(command=lambda:root.exit_app())
        # Exit button placement
        root.btn_exit.place(x=720,y=105)
        # Logout button
        root.btn_logout=Button(root.vegf1,text="Logout",command=lambda:root.Logout(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_logout.place(x=250,y=105)
        # Back button
        root.btn_back=Button(root.vegf1,text="Back",command=lambda:root.menulist(root.x),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_back.place(x=160,y=105)
        # Cart button
        root.btn_cart=Button(root.vegf1,text="My Cart",command=lambda:root.Orderde(root.x),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_cart.place(x=365,y=105)
        # Disable cart button if its empty
        if not root.cartlist:
            root.btn_cart["state"] = "disabled"
        # Set lbl_welcome to "Welcome, (user first name)"
        root.lbl_deliver=Label(root.vegf1,text="Delivery method: ",font=("times",12))
        root.lbl_deliver.place(x=580,y=5)
        #Set the Menu initially
        root.menu= StringVar()
        root.menu.set(root.deliveryMethod)
        
        root.drop= OptionMenu(root.vegf1, root.menu,"Delivery","Carry-out",command=root.delivery_method)
        root.drop.place(x=700,y=5)

        root.vegf1.pack(fill=BOTH,expand=1)

        root.vegf2=Frame(root.scr,height=618,width=1366)
        
        root.c=Canvas(root.vegf2,height=618,width=1366)
        root.c.pack()
        root.logo1=PhotoImage(file="res/pizzamain.png")
        root.c.create_image(683,309,image=root.logo1)
        root.log=Label(root.vegf2,text="VEG PIZZA",bg="#9db1f2",font=("algerian",22))
        root.log.place(x=625,y=10)
        root.c.create_rectangle(80, 15, 575, 470,fill="#d3ede6",outline="black",width=6)
        root.q1=StringVar()
        root.q2=StringVar()
        root.q3=StringVar()
        root.q4=StringVar()
        root.q1.set("0")
        root.q2.set("0")
        root.q3.set("0")
        root.q4.set("0")
        # pizza 1
        root.delu=PhotoImage(file="res/deluxe.png")
        root.c.create_image(150,75,image=root.delu)
        root.c.create_text(310,35,text="Deluxe Veggie",fill="#000000",font=("algerian",20))
        root.c.create_text(290,70,text="$7.99",fill="#ff3838",font=("default",12,'bold'))
        #ch1=root.check(root.vegf2,100)
        root.v1=IntVar()
        root.C11=Radiobutton(root.vegf2,text = "Small",background="#d3ede6",value=10,variable=root.v1)
        root.C11.place(x=210,y=60)
        root.C12 = Radiobutton(root.vegf2, text = "Medium",background="#d3ede6", value = 20, variable =root.v1)
        root.C12.place(x=325,y=60)
        root.c.create_text(420,70,text="$8.99",fill="#ff3838",font=("default",12,'bold'))
        root.C13 = Radiobutton(root.vegf2, text = "Large",background="#d3ede6",value = 30, variable =root.v1)
        root.C13.place(x=450,y=60)
        root.c.create_text(535,70,text="$10.99",fill="#ff3838",font=("default",12,'bold'))
        root.C11.select()
        root.C11.deselect()    
        root.C11.invoke()
        root.c.create_text(245,115,text="Quantity : ",fill="#000000",font=("default",12))
        root.qty1=Entry(root.vegf2,textvariable=root.q1,bg="#aae2d7",font=("default",12),width=4,)
        root.qty1.place(x=290,y=105)
        root.add1=Button(root.vegf2,text="Add to cart",command=lambda:addch1(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        root.add1.place(x=460,y=90)
        def addch1():
            
            if root.v1.get()==10:
                ch1="Small"
                pric1=7.99
            elif root.v1.get()==20:
                ch1="Medium"
                pric1=8.99
            else:
                ch1="Large"
                pric1=10.99
            root.addlist(["Deluxe Veggie",ch1,root.q1.get(),pric1])
            
        #pizza 2
        root.vag=PhotoImage(file="res/extravaganza.png")
        root.c.create_image(150,185,image=root.vag)
        root.c.create_text(300,150,text="Veg Vaganza",fill="#000000",font=("algerian",20))
        root.v2=IntVar()
        root.C21=Radiobutton(root.vegf2,text = "Small",background="#d3ede6",value=10,variable=root.v2)
        root.C21.place(x=205,y=175)
        root.c.create_text(285,185,text="$7.99",fill="#ff3838",font=("default",12,'bold'))
        root.C22 = Radiobutton(root.vegf2, text = "Medium",background="#d3ede6",value = 20, variable =root.v2)
        root.C22.place(x=325,y=175)
        root.c.create_text(420,185,text="$8.99",fill="#ff3838",font=("default",12,'bold'))
        root.C23 = Radiobutton(root.vegf2, text = "Large",background="#d3ede6",value = 30, variable =root.v2)
        root.C23.place(x=455,y=175)
        root.c.create_text(535,185,text="$10.99",fill="#ff3838",font=("default",12,'bold'))
        root.C21.select()
        root.C21.deselect()    
        root.C21.invoke()
        root.c.create_text(245,225,text="Quantity : ",fill="#000000",font=("default",12))
        root.qty2=Entry(root.vegf2,textvariable=root.q2,bg="#aae2d7",font=("default",12),width=4,)
        root.qty2.place(x=295,y=215)
        root.add2=Button(root.vegf2,text="Add to cart",command=lambda:addch2(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        root.add2.place(x=460,y=205)
        def addch2():
            if root.v2.get()==10:
                ch2="Small"
                pric2=7.99
            elif root.v2.get()==20:
                ch2="Medium"
                pric2=8.99
            else:
                ch2="Large"
                pric2=10.99

            root.addlist(["Veg Vaganza",ch2,root.q2.get(),pric2])
        #pizza 3
        root.pep=PhotoImage(file="res/5-pepper-veg-pizza.png")
        root.c.create_image(150,295,image=root.pep)
        root.c.create_text(265,260,text="5 Pepper",fill="#000000",font=("algerian",20))
        #ch3=root.check(root.vegf2,340)
        root.v3=IntVar()
        root.C31=Radiobutton(root.vegf2,text = "Small",background="#d3ede6",value=10,variable=root.v3)
        root.C31.place(x=205,y=280)
        root.c.create_text(290,290,text="$7.99",fill="#ff3838",font=("default",12,'bold'))
        root.C32 = Radiobutton(root.vegf2, text = "Medium",background="#d3ede6",value = 20, variable =root.v3)
        root.C32.place(x=330,y=280)
        root.c.create_text(425,290,text="$8.99",fill="#ff3838",font=("default",12,'bold'))
        root.C33 = Radiobutton(root.vegf2, text = "Large",background="#d3ede6",value = 30, variable =root.v3)
        root.C33.place(x=460,y=280)
        root.c.create_text(540,290,text="$10.99",fill="#ff3838",font=("default",12,'bold'))
        root.C31.select()
        root.C31.deselect()    
        root.C31.invoke()

        root.c.create_text(245,330,text="Quantity : ",fill="#000000",font=("default",12))
        root.qty3=Entry(root.vegf2,textvariable=root.q3,bg="#aae2d7",font=("default",12),width=4,)
        root.qty3.place(x=290,y=320)

        root.add3=Button(root.vegf2,text="Add to cart",command=lambda:addch3(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        root.add3.place(x=465,y=310)
        def addch3():
            if root.v3.get()==10:
                ch3="Small"
                pric3=7.99
            elif root.v3.get()==20:
                ch3="Medium"
                pric3=8.99
            else:
                ch3="Large"
                pric3=10.99
            root.addlist(["5 Pepper     ",ch3,root.q3.get(),pric3])
            
        #pizza 4
        root.mag=PhotoImage(file="res/Margherit.png")
        root.c.create_image(150,405,image=root.mag)
        root.c.create_text(295,370,text="Margherita",fill="#000000",font=("algerian",20))
        #ch4=root.check(root.vegf2,460)
        root.v4=IntVar()
        root.C41=Radiobutton(root.vegf2,text = "Small",background="#d3ede6",value=10,variable=root.v4)
        root.C41.place(x=210,y=395)
        root.c.create_text(295,405 ,text="$7.99",fill="#ff3838",font=("default",12,'bold'))
        root.C42 = Radiobutton(root.vegf2, text = "Medium",background="#d3ede6",value = 20, variable =root.v4)
        root.C42.place(x=335,y=395)
        root.c.create_text(430,405 ,text="$8.99",fill="#ff3838",font=("default",12,'bold'))
        root.C43 = Radiobutton(root.vegf2, text = "Large",background="#d3ede6",value = 30, variable =root.v4)
        root.C43.place(x=460,y=395)
        root.c.create_text(540,405,text="$10.99",fill="#ff3838",font=("default",12,'bold'))
        root.C41.select()
        root.C41.deselect()    
        root.C41.invoke()
        
        root.c.create_text(245,445,text="Quantity : ",fill="#000000",font=("default",12))
        root.qty4=Entry(root.vegf2,textvariable=root.q4,bg="#aae2d7",font=("default",12),width=4,)
        root.qty4.place(x=290,y=435)
        
        root.add4=Button(root.vegf2,text="Add to cart",command=lambda:addch4(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        root.add4.place(x=465,y=425)
        def addch4():
            if root.v4.get()==10:
                ch4="Small"
                pric4=7.99
            elif root.v4.get()==20:
                ch4="Medium"
                pric4=8.99
            else:
                ch4="Large"
                pric4=10.99
            root.addlist(["Margherita  ",ch4,root.q4.get(),pric4])

        root.more=Button(root.vegf2,text="Add More..",command=lambda:root.menulist(root.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        root.more.place(x=625,y=50)
        root.vegf2.pack(fill=BOTH,expand=1)
        root.scr.mainloop()
 # non-veg pizza screen
    def nonvegpizza(root,x):
        root.x=x
        root.scr.destroy()
        root.scr=Tk()
        root.createNewWindow("Mighty's Pizza - Non Veg Pizzas")
        root.scr.geometry("800x640")
        #root.scr.resizable(False, False)
        root.nonvegf1=Frame(root.scr,height=150,width=1366)
        root.c=Canvas(root.nonvegf1,height=150,width=1366)
        root.c.pack()
        
        root.logo=PhotoImage(file="res/pizzabanner.png")
        root.c.create_image(180,0,image=root.logo)
        # Open logo image
        root.imgLogo=PhotoImage(file="res/logo.png")
        # Set "imgLogo" image in label "lbl_logo"
        root.lbl_logo=Label(root.nonvegf1,image=root.imgLogo,height=150,width=150).place(x=0,y=0)
        root.btn_logou=Button(root.nonvegf1,text="Log Out",command=lambda:root.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        root.btn_logout.place(x=1000,y=90)

        # Set lbl_mighty to "Mighty Pizza"
        root.lbl_mighty=Label(root.nonvegf1,text="Mighty PizzLogina",font=("algerian",22))
        # Place lbl_mighty at x=160,y=10
        root.lbl_mighty.place(x=160,y=10)
        # Set lbl_welcome to "Welcome, (user first name)"
        root.lbl_welcome=Label(root.nonvegf1,text="Welcome, " + user.get_username(),font=("algerian",22))
        # Place lbl_mighty at x=160,y=10
        root.lbl_welcome.place(x=160,y=50)
        # About button
        root.btn_about=Button(root.nonvegf1,text="About Us",bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("algerian",16))
        root.btn_about.config(command=lambda:root.about())
        # About button placement
        root.btn_about.place(x=485,y=105)
        # Exit button
        root.btn_exit=Button(root.nonvegf1,text="Exit",bg="Red",cursor="hand2",bd=4,fg="white",font=("algerian",16))
        root.btn_exit.config(command=lambda:root.exit_app())
        # Exit button placement
        root.btn_exit.place(x=720,y=105)
        # Logout button
        root.btn_logout=Button(root.nonvegf1,text="Logout",command=lambda:root.Logout(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_logout.place(x=250,y=105)
        # Back button
        root.btn_back=Button(root.nonvegf1,text="Back",command=lambda:root.menulist(root.x),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_back.place(x=160,y=105)
        # Cart button
        root.btn_cart=Button(root.nonvegf1,text="My Cart",command=lambda:root.Orderde(root.x),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("algerian",16))
        root.btn_cart.place(x=365,y=105)
        # Disable cart button if its empty
        if not root.cartlist:
            root.btn_cart["state"] = "disabled"
        # Set lbl_welcome to "Welcome, (user first name)"
        root.lbl_deliver=Label(root.nonvegf1,text="Delivery method: ",font=("times",12))
        root.lbl_deliver.place(x=580,y=5)
        #Set the Menu initially
        root.menu= StringVar()
        root.menu.set(root.deliveryMethod)
        
        root.drop= OptionMenu(root.nonvegf1, root.menu,"Delivery","Carry-out",command=root.delivery_method)
        root.drop.place(x=700,y=5)

        root.nonvegf1.pack(fill=BOTH,expand=1)

        root.nonvegf2=Frame(root.scr,height=618,width=1366)
        
        root.c=Canvas(root.nonvegf2,height=618,width=1366)
        root.c.pack()
        root.logo1=PhotoImage(file="res/pizzamain.png")
        root.c.create_image(683,309,image=root.logo1)
        root.log=Label(root.nonvegf2,text="NON-VEG PIZZA",bg="#9db1f2",font=("algerian",22))
        root.log.place(x=625,y=10)
        root.c.create_rectangle(80, 15, 575, 470,fill="#d3ede6",outline="black",width=6)
        root.q5=StringVar()
        root.q6=StringVar()
        root.q7=StringVar()
        root.q8=StringVar()
        root.q5.set("0")
        root.q6.set("0")
        root.q7.set("0")
        root.q8.set("0")
        # pizza 1
        root.delu=PhotoImage(file="res/Non-Veg_Supreme.png")
        root.c.create_image(150,75,image=root.delu)
        root.c.create_text(310,35,text="Non-Veg Supreme",fill="#000000",font=("algerian",20))
        root.c.create_text(290,70,text="$7.99",fill="#ff3838",font=("default",12,'bold'))
        #ch1=root.check(root.nonvegf2,100)
        root.v5=IntVar()
        root.C11=Radiobutton(root.nonvegf2,text = "Small",background="#d3ede6",value=10,variable=root.v5)
        root.C11.place(x=210,y=60)
        root.C12 = Radiobutton(root.nonvegf2, text = "Medium",background="#d3ede6", value = 20, variable =root.v5)
        root.C12.place(x=325,y=60)
        root.c.create_text(420,70,text="$8.99",fill="#ff3838",font=("default",12,'bold'))
        root.C13 = Radiobutton(root.nonvegf2, text = "Large",background="#d3ede6",value = 30, variable =root.v5)
        root.C13.place(x=450,y=60)
        root.c.create_text(535,70,text="$10.99",fill="#ff3838",font=("default",12,'bold'))
        root.C11.select()
        root.C11.deselect()    
        root.C11.invoke()
        root.c.create_text(245,115,text="Quantity : ",fill="#000000",font=("default",12))
        root.qty1=Entry(root.nonvegf2,textvariable=root.q5,bg="#aae2d7",font=("default",12),width=4,)
        root.qty1.place(x=290,y=105)
        root.add1=Button(root.nonvegf2,text="Add to cart",command=lambda:addch5(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        root.add1.place(x=460,y=90)
        def addch5():
            
            if root.v5.get()==10:
                ch5="Small"
                pric1=7.99
            elif root.v5.get()==20:
                ch5="Medium"
                pric1=8.99
            else:
                ch5="Large"
                pric1=10.99
            root.addlist(["Non-Veg Supreme ",ch5,root.q5.get(),pric1])
            
        #pizza 2
        root.vag=PhotoImage(file="res/non-Chicken_Sausage.png")
        root.c.create_image(150,185,image=root.vag)
        root.c.create_text(300,150,text="Chicken Sausage",fill="#000000",font=("algerian",20))
        root.v7=IntVar()
        root.C21=Radiobutton(root.nonvegf2,text = "Small",background="#d3ede6",value=10,variable=root.v7)
        root.C21.place(x=205,y=175)
        root.c.create_text(285,185,text="$7.99",fill="#ff3838",font=("default",12,'bold'))
        root.C22 = Radiobutton(root.nonvegf2, text = "Medium",background="#d3ede6",value = 20, variable =root.v7)
        root.C22.place(x=325,y=175)
        root.c.create_text(420,185,text="$8.99",fill="#ff3838",font=("default",12,'bold'))
        root.C23 = Radiobutton(root.nonvegf2, text = "Large",background="#d3ede6",value = 30, variable =root.v7)
        root.C23.place(x=455,y=175)
        root.c.create_text(535,185,text="$10.99",fill="#ff3838",font=("default",12,'bold'))
        root.C21.select()
        root.C21.deselect()    
        root.C21.invoke()
        root.c.create_text(245,225,text="Quantity : ",fill="#000000",font=("default",12))
        root.qty2=Entry(root.nonvegf2,textvariable=root.q7,bg="#aae2d7",font=("default",12),width=4,)
        root.qty2.place(x=295,y=215)
        root.add2=Button(root.nonvegf2,text="Add to cart",command=lambda:addch7(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        root.add2.place(x=460,y=205)
        def addch7():
            if root.v7.get()==10:
                ch7="Small"
                pric7=7.99
            elif root.v7.get()==20:
                ch7="Medium"
                pric7=8.99
            else:
                ch7="Large"
                pric7=10.99

            root.addlist(["Chicken Tikka ",ch7,root.q7.get(),pric7])
       
        root.nonvegf2.pack(fill=BOTH,expand=1)
        root.scr.mainloop()
    #--  page 14------
    def Orderde(root,x):

        root.x=x
        root.scr.destroy()
        root.scr=Tk()
        root.scr.title("Mighty's Pizza - My Cart")
        root.rtitle = str(root.scr.title)
        root.scr.geometry("800x600")
        root.scr.resizable(False, False)
        root.ordf1=Frame(root.scr,height=800,width=600)
        root.c=Canvas(root.ordf1,height=800,width=800)
        root.c.pack()
        root.log=Label(root.ordf1,text="YOUR ORDER",bg="#9db1f2",font=("algerian",22))
        root.log.place(x=15,y=4)
        root.c.create_rectangle(15, 50, 790, 480,fill="#d3ede6",outline="black",width=6)
        # Exit button
        root.btn_exit=Button(root.ordf1,text="Exit",bg="Red",cursor="hand2",bd=4,fg="white",font=("algerian",16))
        root.btn_exit.config(command=lambda:root.exit_app())
        # Exit button placement
        root.btn_exit.place(x=720,y=5)
        # Check to see if shopping cart is empty
        if not root.cartlist:
            root.amt = 0
        else:
            if root.deliveryMethod == "Delivery":
                root.amt=root.amount + root.deliveryFee 
                root.amt=root.calculate_totals(root.amt)

                # Label for Delivery Fee
                root.lbl_fee=Label(root.ordf1,text="Delivery Fee: $" + str(root.deliveryFee),bg="#f2da9d",width=16,font=("times",16))
                root.lbl_fee.place(x=575,y=125)
    
            else:
                # Get the total amount of order
                root.amt=root.calculate_totals(root.amount)
                # Label for Carry-out
                root.lbl_carry=Label(root.ordf1,text="Carry-Out" ,bg="#f2da9d",width=16,font=("times",16))
                root.lbl_carry.place(x=575,y=125)

        
        
        # Label for Sub-Total
        root.text="Sub-Total: $"+str(format(root.amount, ".2f"))
        root.lbl_sub=Label(root.ordf1,text=root.text,bg="#f2da9d",width=16,font=("times",16))
        root.lbl_sub.place(x=575,y=100)
        # Label for Tax
        root.lbl_tax=Label(root.ordf1,text="Tax: $" + str(format(root.amount * root.taxRate, ".2f")),bg="#f2da9d",width=16,font=("times",16))
        root.lbl_tax.place(x=575,y=150)
        # Label for a line
        root.lbl_line=Label(root.ordf1,text="-----------------------",bg="#f2da9d",width=16,font=("times",16))
        root.lbl_line.place(x=575,y=175)
        # Label for Total
        root.text="Total: $"+str(root.amt)
        root.tot=Label(root.ordf1,text=root.text,bg="#f2da9d",width=16,font=("times",16))
        root.tot.place(x=575,y=200)
        root.btn_order=Button(root.ordf1,text="Place order",command=lambda:root.place_order(x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        root.btn_order.place(x=600,y=395)
        root.btn_add_more=Button(root.ordf1,text="Add more",command=lambda:root.menulist(root.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        root.btn_add_more.place(x=600,y=275)
        root.btn_clear_cart=Button(root.ordf1,text="Clear Cart",command=lambda:root.clear_cart(x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        root.btn_clear_cart.place(x=600,y=335)
        root.c.create_text(75,80,text="Items",font=("algerian",18))
        root.c.create_text(250,80,text="Size ",font=("algerian",18))
        root.c.create_text(350,80,text="Qty",font=("algerian",18))
        root.c.create_text(450,80,text="Price",font=("algerian",18))
        root.c.create_text(275,90,text="_______________________________________",font=("algerian",18))
        y=100
        for i in root.cartlist:
            y+=30
            root.c.create_text(105,y,text=i[0],font=("times",14))
            root.c.create_text(250,y,text=i[1],font=("times",14))
            root.c.create_text(350,y,text=i[2],font=("times",14))
            root.c.create_text(450,y,text=i[3],font=("times",14))
            
        root.ordf1.pack(fill=BOTH,expand=1)
        root.scr.mainloop()

        
        
    #functions
    def place_order(root, x):
            messagebox.showinfo('Ordering', 'Your order has been received, thank you.')
            root.cartlist = []
            root.menulist(x)

    def clear_cart(root,x): # Clears the current cart
            msg_box = messagebox.askquestion('Clear Cart?', 'Are you sure you want clear your cart? Everything in your cart will be deleted',
                                        icon='warning')
            if msg_box == 'yes':
                root.cartlist = []
                root.menulist(x)
            else:
                messagebox.showinfo('Return', 'You will now return to the application screen')
    # Calculate the purchase price with the coounty and state sales tax
    def calculate_totals(root, purchase):
        state_sales_tax = purchase * root.taxRate
        total = state_sales_tax + purchase
        return format(total, ".2f")
    # Use to set delivery method, Carry-out or Delivery
    def delivery_method(root, selection):
            root.deliveryMethod = selection
            if selection == "Delevery":
                root.x = "deli"
            else: 
                root.x = "pick"
            # Change window title
            newTitle = str(str(root.rtitle) + " (" + str(selection) + ")")
            root.scr.title(newTitle)



    
        
    #functions
    
    # Calculate the purchase price with the coounty and state sales tax
    def calculate_totals(root, purchase):
        state_sales_tax = purchase * root.taxRate
        total = state_sales_tax + purchase
        return format(total, ".2f")
    # Use to set delivery method, Carry-out or Delivery
    def delivery_method(root, selection):
            root.deliveryMethod = selection
            if selection == "Delevery":
                root.x = "deli"
            else: 
                root.x = "pick"
            # Change window title
            newTitle = str(str(root.rtitle) + " (" + str(selection) + ")")
            root.scr.title(newTitle)    

    # Adds items to the shopping cart, 
    def addlist(root,q):
        try:
            if root.vInput.check_user_input("ini", q[2]):
                q[3] = int(q[2]) * q[3]

                root.btn_cart["state"] = "normal"
                if q[-2]!="0" and q[-2].isdigit():
                    root.cartlist.append(q)
                    root.amount=root.amount+q[-1]
                    messagebox.showinfo("Cart","Item Successfully added") 
                else:
                    messagebox.showinfo("Cart","Enter Valid Quantity to add")
            else:
                    messagebox.showinfo("Cart","Enter Valid Quantity to add to cart")
        except Exception as e:
            messagebox.showinfo("Cart","Enter Valid Quantity to add to cart")
    # exit
    def exit_app(root):
        msg_box = messagebox.askquestion('Exit', 'Are you sure you want to Exit? Everything in your cart will be deleted',
                                        icon='warning')
        if msg_box == 'yes':
            # Destroy current user
            root.scr.destroy()
        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')
    # logut the user
    def Logout(root):
        msg_box = messagebox.askquestion('Logout', 'Are you sure you want to logout? Everything in your cart will be deleted',
                                        icon='warning')
        if msg_box == 'yes':
            # Destroy current user
            user.logout()
            # Load login screen
            root.Login() 
        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')
    
    def guest_login(root):
        # Login in as guest
        user.guest()
        # Load ordering screen
        root.pizmain()

    # Login command
    def usr_login(root, username, password):
        
        # check to see if username or password is empty
        if username == "" or password == "":
            # If username or password is empty show messagebox
            messagebox.showinfo("Login","Empty Entry is not allowed")
        else:
            # Check if username and password is in the database
            if user.login(username, password) == True:
                # Username and password match show messagebox
                messagebox.showinfo("Login","You have Successfully Log In\nWelcome to Mighty Pizza")
                # User is logged in goto ordering          
                root.pizmain()
            else:
                # If username and password do not match give a message
                messagebox.showinfo("Login","Wrong username or password")
                
    def check_input(this, dType: str, usrInput):
        try:
            if this.vInput.check_user_input(dType, usrInput):
                return True
            else:
                return False
        except Exception as e:
            messagebox.showinfo("Error: ",e)
      


x=Pizza()
x.main()

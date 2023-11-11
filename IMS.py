#import tkinter as tk
from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Inventory Management System SRSAC | Developed By Rohit")
        self.root.config(bg='white')
        
        #-----title-------
        self.icon_title=PhotoImage(file="Image\logo.png")
        title=Label(self.root,text="Inventory Management System SRSAC",image=self.icon_title,compound=LEFT,font=("times new roman",40,'bold'),bg='#FFFFFF',fg='#000000',anchor='w',padx=20).place(x=0,y=0,relwidth=1,height=80)
        
        
        #***********Button for lodout************
        btn_logout=Button(self.root,text="Logout",font=('times new roman',15,"bold"),bg="yellow",cursor='hand2').place(x=1210,y=100,height=30,width=150)
        
        #***********Clock************
        self.lbl_clock=Label(self.root,text="WelCome State Remote Sensing Application Centre, Jodhpur \t\t Date:DD-MM-YYYY \t\t Time:HH-MM-SS",font=("times new roman",15),bg='#4d636d',fg='white')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #**************Left Menu***********
        self.MenuLogo=Image.open("Image\menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        LeftMenu.place(x=0,y=102,width=200,height=565)
        
        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        self.icon_side=PhotoImage(file="Image\side.png")
        
        btn_menu=Label(LeftMenu,text="Menu",font=('times new roman',20),bg='#009688').pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=('times new roman',20,"bold"),bg='white',bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=('times new roman',20,"bold"),bg='white',bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=('times new roman',20,"bold"),bg='white',bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=('times new roman',20,"bold"),bg='white',bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=('times new roman',20,"bold"),bg='white',bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=('times new roman',20,"bold"),bg='white',bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        
        #***************Contanct****************
        
        self.lbl_employee=Label(self.root,text='Total Employee\n[ 0 ]',bd=5,relief=RIDGE,bg='#33bbf9',fg="white",font=('goudy old style',20,'bold'))
        self.lbl_employee.place(x=300,y=150,height=150,width=300)
        
        self.lbl_supplier=Label(self.root,text='Total Supplier\n[ 0 ]',bd=5,relief=RIDGE,bg='#33bbf9',fg="white",font=('goudy old style',20,'bold'))
        self.lbl_supplier.place(x=650,y=150,height=150,width=300)
        
        self.lbl_category=Label(self.root,text='Total Category\n[ 0 ]',bd=5,relief=RIDGE,bg='#33bbf9',fg="white",font=('goudy old style',20,'bold'))
        self.lbl_category.place(x=1000,y=150,height=150,width=300)
        
        self.lbl_product=Label(self.root,text='Total Product\n[ 0 ]',bd=5,relief=RIDGE,bg='#33bbf9',fg="white",font=('goudy old style',20,'bold'))
        self.lbl_product.place(x=300,y=330,height=150,width=300)
        
        self.lbl_sales=Label(self.root,text='Total Sales\n[ 0 ]',bd=5,relief=RIDGE,bg='#33bbf9',fg="white",font=('goudy old style',20,'bold'))
        self.lbl_sales.place(x=650,y=330,height=150,width=300)
        
        
        
        #***********Footer************
        lbl_footer=Label(self.root,text="State Remote Sensing Application Centre, Jodhpur \t\n Department of science and technology, subash nagar, pal road, jodhpur",compound=LEFT,font=("times new roman",12),bg='#4d636d',fg='white').place(x=0,y=665,width=1500)
        
#***********************************************************************
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
                
if __name__=="__main__":       
    root=Tk()
    obj=IMS(root)
    root.mainloop()


from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System SRSAC | Developed By Rohit")
        self.root.config(bg='white')
        self.root.focus_force()
        #===============================================
        # All Variables==========
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        
        self.var_emp_id=StringVar()
        self.var_status=StringVar()
        self.var_product=StringVar()
        self.var_name_hol=StringVar()
        self.var_doi=StringVar()
        self.var_dos=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_price=StringVar()
        
        #---------SearchFrame-----------
        SearchFrame=LabelFrame(self.root,text="Search Product",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
        
        #------option----
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=('Select','Product','Name','Email'),state='readonly',justify=CENTER,font=('goudy old style',15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=('goudy old style',15),bg='lightyellow').place(x=200,y=10)
        btn_search=Button(SearchFrame,text='Search',font=('goudy old style',15),bg='#4caf50',fg='white',cursor='hand2').place(x=410,y=9,width=150,height=30)
        
        #--------title----
        title=Label(self.root,text='Product Details',font=('goudy old style',15),bg='#0f4d7d',fg='white').place(x=50,y=100,width=1000)
        
        
        #======content========
        #------Row1-----------
        lbl_empid=Label(self.root,text='Emp ID',font=('goudy old style',15),bg='white').place(x=50,y=150)
        lbl_status=Label(self.root,text='Status',font=('goudy old style',15),bg='white').place(x=350,y=150)
        lbl_product=Label(self.root,text='product Name',font=('goudy old style',15),bg='white').place(x=720,y=150)
        
        
        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=('goudy old style',15),bg='lightyellow').place(x=155,y=150,width=180)
        #txt_empid=Entry(self.root,textvariable=self.var_status,font=('goudy old style',15),bg='white').place(x=500,y=150,width=180)
        cmb_status=ttk.Combobox(self.root,textvariable=self.var_status,values=('Select','Active','Submit','Other'),state='readonly',justify=CENTER,font=('goudy old style',15))
        cmb_status.place(x=500,y=150,width=180)
        cmb_status.current(0)
        txt_product=Entry(self.root,textvariable=self.var_product,font=('goudy old style',15),bg='lightyellow').place(x=850,y=150,width=180)
        
        #------Row2--------
        lbl_name_hol=Label(self.root,text='Name Holder',font=('goudy old style',15),bg='white').place(x=50,y=190)
        lbl_doi=Label(self.root,text='Date of Issue',font=('goudy old style',15),bg='white').place(x=350,y=190)
        lbl_dos=Label(self.root,text='Date of Submit',font=('goudy old style',15),bg='white').place(x=720,y=190)
        
        
        txt_name_hol=Entry(self.root,textvariable=self.var_name_hol,font=('goudy old style',15),bg='lightyellow').place(x=155,y=190,width=180)
        txt_doi=Entry(self.root,textvariable=self.var_doi,font=('goudy old style',15),bg='lightyellow').place(x=500,y=190,width=180)
        txt_dos=Entry(self.root,textvariable=self.var_dos,font=('goudy old style',15),bg='lightyellow').place(x=850,y=190,width=180)
        
        #------Row3------
        lbl_email=Label(self.root,text='Email',font=('goudy old style',15),bg='white').place(x=50,y=230)
        lbl_pass=Label(self.root,text='Password',font=('goudy old style',15),bg='white').place(x=350,y=230)
        lbl_utype=Label(self.root,text='User Type',font=('goudy old style',15),bg='white').place(x=720,y=230)
        
        
        txt_email=Entry(self.root,textvariable=self.var_email,font=('goudy old style',15),bg='lightyellow').place(x=155,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=('goudy old style',15),bg='lightyellow').place(x=500,y=230,width=180)
        #txt_utype=Entry(self.root,textvariable=self.var_utype,font=('goudy old style',15),bg='lightyellow').place(x=850,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=('Admin','Employee'),state='readonly',justify=CENTER,font=('goudy old style',15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)
        
         #------Row3------
        lbl_address=Label(self.root,text='Address',font=('goudy old style',15),bg='white').place(x=50,y=270)
        lbl_price=Label(self.root,text='Price of Product',font=('goudy old style',15),bg='white').place(x=470,y=270)        
        
        self.txt_address=Text(self.root,font=('goudy old style',15),bg='lightyellow')
        self.txt_address.place(x=155,y=270,width=300,height=60)
        txt_price=Entry(self.root,textvariable=self.var_price,font=('goudy old style',15),bg='lightyellow').place(x=600,y=270,width=180)
        
        #=========Button===========
        btn_add=Button(self.root,text='Save',command=self.add,font=('goudy old style',15),bg='#2196f3',fg='white',cursor='hand2').place(x=500,y=305,width=110,height=20)
        btn_update=Button(self.root,text='Update',command=self.update,font=('goudy old style',15),bg='#4caf50',fg='white',cursor='hand2').place(x=620,y=305,width=110,height=20)
        btn_delete=Button(self.root,text='Delete',command=self.delete,font=('goudy old style',15),bg='#f44336',fg='white',cursor='hand2').place(x=740,y=305,width=110,height=20)
        btn_clear=Button(self.root,text='Clear',command=self.clear,font=('goudy old style',15),bg='#607d8b',fg='white',cursor='hand2').place(x=860,y=305,width=110,height=20)
        
        
        #=======---Employee Details---=========
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("Eid","product","email","status","name_hol","doi","dos","pass","utype","address","price"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        
        self.EmployeeTable.heading('Eid',text='Emp_id')
        self.EmployeeTable.heading('product',text='Product')
        self.EmployeeTable.heading('email',text='Email')
        self.EmployeeTable.heading('status',text='Status')
        self.EmployeeTable.heading('name_hol',text='Name holder')
        self.EmployeeTable.heading('doi',text='Date of Issue')
        self.EmployeeTable.heading('dos',text='Date of Submit')
        self.EmployeeTable.heading('pass',text='Password')
        self.EmployeeTable.heading('utype',text='User Type')
        self.EmployeeTable.heading('address',text='Address')
        self.EmployeeTable.heading('price',text='Price of Product')
        self.EmployeeTable["show"]='headings'
        
        self.EmployeeTable.column('Eid',width=90)
        self.EmployeeTable.column('product',width=100)
        self.EmployeeTable.column('email',width=100)
        self.EmployeeTable.column('status',width=100)
        self.EmployeeTable.column('name_hol',width=100)
        self.EmployeeTable.column('doi',width=100)
        self.EmployeeTable.column('dos',width=100)
        self.EmployeeTable.column('pass',width=100)
        self.EmployeeTable.column('utype',width=100)
        self.EmployeeTable.column('address',width=100)
        self.EmployeeTable.column('price',width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
#====================================================================================        
    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where Eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into employee (Eid,product,email,status,name_hol,doi,dos,pass,utype,address,price)values(?,?,?,?,?,?,?,?,?,?,?)",(
                                        self.var_emp_id.get(),
                                        self.var_product.get(),
                                        self.var_email.get(),
                                        self.var_status.get(),
                                        self.var_name_hol.get(),
                                        
                                        self.var_doi.get(),
                                        self.var_dos.get(),
                                        
                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_price.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Addedd Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to :{str(ex)}",parent=self.root)
        
    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to :{str(ex)}",parent=self.root)
            
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        #=Print(row)
        self.var_emp_id.set(row[0])                                
        self.var_product.set(row[1])
        self.var_email.set(row[2])
        self.var_status.set(row[3])
        self.var_name_hol.set(row[4])                                
        self.var_doi.set(row[5])
        self.var_dos.set(row[6])                               
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END),
        self.txt_address.insert(END,row[9]),
        self.var_price.set(row[10])
        
#============Update================
    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where Eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    cur.execute("Update employee set product=?,email=?,status=?,name_hol=?,doi=?,dos=?,pass=?,utype=?,address=?,price=? where eid=?",(
                                        self.var_product.get(),
                                        self.var_email.get(),
                                        self.var_status.get(),
                                        self.var_name_hol.get(),
                                        
                                        self.var_doi.get(),
                                        self.var_dos.get(),
                                        
                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_price.get(),
                                        self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to :{str(ex)}",parent=self.root)
        
    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to :{str(ex)}",parent=self.root)
            
    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where Eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirem","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
                        self.clear()
            
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to :{str(ex)}",parent=self.root)
            
    def clear(self):
        self.var_emp_id.set("")                                
        self.var_product.set("")
        self.var_email.set("")
        self.var_status.set("Select")
        self.var_name_hol.set("")                                
        self.var_doi.set("")
        self.var_dos.set("")                               
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0',END),
        self.var_price.set("")
        self.show()               
   # def search(self):
                            
if __name__=="__main__":       
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()
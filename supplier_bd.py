import sqlite3
def supplier_db():
    con=sqlite3.connect(database=r'ims1.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(Eid INTEGER PRIMARY KEY AUTOINCREMENT,product text,email text,status text,name_hol text,doi text,dos text,pass text,utype text,address text,price text")
    #con.commit()
    
supplier_db()
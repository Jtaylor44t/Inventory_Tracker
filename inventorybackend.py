#Back end database
import sqlite3

#defining the database connection
def connect():
    conn=sqlite3.connect("inventory.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, name text, device_type text, make text, serial_tag text)")
    conn.commit()
    conn.close()


#allows you to insert new entries.
def insert(name,device_type,make,serial_tag):    
    conn=sqlite3.connect("inventory.db") 
    cur=conn.cursor() 
    cur.execute("INSERT INTO inventory VALUES (NULL,?,?,?,?)",(name,device_type,make,serial_tag)) 
    conn.commit()                                
    conn.close() 

#this allows you to view all the data
def view():  
    conn=sqlite3.connect("inventory.db") 
    cur=conn.cursor()
    cur.execute("SELECT * FROM inventory") 
    rows=cur.fetchall() 
    conn.close() 
    return rows

#pass empty strings so you can search for each parameter individually instead of needing to enter all 4.
def Search(name="",device_type="",make="",serial_tag=""):
    conn=sqlite3.connect("inventory.db") 
    cur=conn.cursor()
    cur.execute("SELECT * FROM inventory WHERE name=? OR device_type=? OR make=? OR serial_tag=?", (name,device_type,make,serial_tag))
    rows=cur.fetchall()                             
    conn.close() 
    return rows

#select one record and delete.
def delete(id):
    conn=sqlite3.connect("inventory.db") 
    cur=conn.cursor() 
    cur.execute("DELETE FROM inventory WHERE id=?",(id,)) 
    conn.commit()                                
    conn.close() 

#select row, values of row displays, change cell in entry and press update. get list from list box and refer to id and get new values.
def update(id,name,device_type,make,serial_tag):
    conn=sqlite3.connect("inventory.db") 
    cur=conn.cursor() 
    cur.execute("UPDATE inventory SET name=?, device_type=?, make=?, serial_tag=? WHERE id=?",(name,device_type,make,serial_tag,id))
    conn.commit()                                
    conn.close()

connect()
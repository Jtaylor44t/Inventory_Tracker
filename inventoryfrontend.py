#Tkinter(Front end) and sqlite3(Back end)
#Use pack or grid method
#Front end part
from tkinter import *
import inventorybackend

def get_selected_row(event):  #event parameter holds info about specific event binded. returns selected tuple.
    try:
        global selected_tuple   #global variable to print local variable outside function
        index=list1.curselection()[0]
        selected_tuple=list1.get(index) #from the list box, get tuple with index x
        e1.delete(0,END) #delete everything from entry
        e1.insert(END,selected_tuple[1]) #selected index of tuple (so title for index 1)
        e2.delete(0,END) 
        e2.insert(END,selected_tuple[2]) 
        e3.delete(0,END) 
        e3.insert(END,selected_tuple[3]) 
        e4.delete(0,END) 
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass
#The above e1-e4 populates entry boxes when selecting a tuple from the list box 




#view_command function for importing view function
def view_command():
    list1.delete(0, END)    #deletes everything from beginning to end row before executing
    for row in inventorybackend.view():
        list1.insert(END,row)   #gets 2 arguments. index where to insert your value, put as the first item of list, new rows put at end of list box with END

def search_command(): #get from entry widgets. StringVar() object as value.
    list1.delete(0,END) #deletes listbox contents
    for row in inventorybackend.Search(name_text.get(), device_type_text.get(), make_text.get(), serial_tag_text.get()): #<<outputs string object. #loop through backend from user input in entry widget
        list1.insert(END,row)  #insert end of list

def add_command():
    inventorybackend.insert(name_text.get(), device_type_text.get(), make_text.get(), serial_tag_text.get())
    list1.delete(0,END)
    list1.insert(END,name_text.get(), device_type_text.get(), make_text.get(), serial_tag_text.get())#deletes listbox and adds entries

def delete_command():
    inventorybackend.delete(selected_tuple[0])  #uses global variable from above.

def update_command():
    inventorybackend.update(selected_tuple[0],name_text.get(),device_type_text.get(),make_text.get(),serial_tag_text.get())
    


window=Tk()  #creates window object and wraps widgets with mainloop()

window.wm_title("Inventory Manager")   #wm method of window object

l1=Label(window, text="Name")
l1.grid(row=0,column=0)

l2=Label(window, text="Device Type")
l2.grid(row=0,column=2)
#                                                     These 4 L's are your label variables
l3=Label(window, text="Make")
l3.grid(row=1,column=0)

l4=Label(window, text="Service/Serial")
l4.grid(row=1,column=2)


name_text=StringVar()
e1=Entry(window, textvariable=name_text)      
#textvariable parameter for entry variables. expects value the user enters. This value is the StringVar() special object
e1.grid(row=0,column=1)

device_type_text=StringVar()
e2=Entry(window, textvariable=device_type_text)      
e2.grid(row=0,column=3)
#                                                  These 4 are your entry variables                                                   
make_text=StringVar()
e3=Entry(window, textvariable=make_text)      
e3.grid(row=1,column=1)

serial_tag_text=StringVar()
e4=Entry(window, textvariable=serial_tag_text)      
e4.grid(row=1,column=3)
#These entry variables require the StringVar() in a variable. Then the textvariable calls it to use the user input. They correspond to the label variables

list1=Listbox(window, height=6,width=35)    #creates list box
list1.grid(row=2,column=0,rowspan=6,columnspan=2)  #row and column span parameters will stretch the listbox

sb1=Scrollbar(window)   #scroll bar method in a variable
sb1.grid(row=2,column=2,rowspan=6)  #span the scroll bar to center it

list1.configure(yscrollcommand=sb1.set) #configure method. verticle scroll bar on y axis is set to that list box.
sb1.configure(command=list1.yview) #pass the command parameter so when you scroll the bar the view of the list will change 

list1.bind('<<ListboxSelect>>',get_selected_row)  #bind method to listbox widget takes 2 arguments. event type, function to bind to event type


b1=Button(window,text="View all", width=12,command=view_command) #have a function, grab the view function, and insert data into list box
b1.grid(row=2,column=3)                    #dont need brackets ^^ when calling view function

b2=Button(window,text="Search entry", width=12,command=search_command) #wrapper functions. passing parameters to function. need a front end function to call back end function with parameters.
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=4,column=3)  #                         These button methods add the buttons to the right of the list box

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12,command=window.destroy)   #window.destroy to close window
b6.grid(row=7,column=3)
#need to add command parameters to tell buttons what to do

window.mainloop()  #wraps all widgets in main window




#install pip3 install pyinstaller to make a standalone exe file out of scripts
#call pyinstaller and point to script
#pass --onefile to create a single exe file. and --windowed to hide command line
#    pyinstaller --onefile --windowed filename.py





#admissionForm.py

import tkinter
import os
from datetime import date
import sqlite3

def showHomeForm():
    global root     #root as global variable
    root.destroy()  #exit current window
    os.system('python home.py') #executing another python script
    
def exitAdmPortal():
    global root
    root.destroy()

def autoAppNoGen():
    #auto application no. generation
    conn = sqlite3.connect('school.db')   #creating and connecting database

    c = conn.cursor()   #defining a cursor

    c.execute('CREATE TABLE IF NOT EXISTS admission (date TEXT,appno TEXT,name TEXT,gender TEXT,bgroup TEXT,nationality TEXT,cat TEXT,fname TEXT,foccup TEXT,mname TEXT,moccup TEXT,dob TEXT,addr TEXT,phno TEXT,class_admt TEXT)')    #creating table within the database
    c.execute('SELECT * FROM admission')    #retrieving values from the table

    appno = 0
    for row in c:
        appno = row[1]  #getting last application no.

    if appno == 0:
        appno = 1   #setting application no. to 1 for 1st entry
    else:
        appno = int(appno) + 1  #incrementing application no.
    
    conn.close()    #closing the connection
    
    return appno    #return the resultant value
    
def insertRecords():
    #getting values from textbox    
    date = var_date.get()
    appno = var_appno.get()
    name = var_name.get()
    gender = var_gender.get()
    if(gender == 1):
        gender = 'Male'        
    else:
        gender = 'Female'
    bgroup = var_bgroup.get()
    nationality = var_nationality.get()
    cat = var_cat.get()
    fname = var_fname.get()
    foccup = var_foccup.get()
    mname = var_mname.get()
    moccup = var_moccup.get()
    dob = var_dob.get()
    addr = var_addr.get()
    phno = var_phno.get()    
    class_admt = var_class_admt.get()
    
    conn = sqlite3.connect('school.db')    #creating and connecting database
    print ("Opened database successfully");
    
    c = conn.cursor()   #defining a cursor
    
    c.execute('CREATE TABLE IF NOT EXISTS admission (date TEXT,appno TEXT,name TEXT,gender TEXT,bgroup TEXT,nationality TEXT,cat TEXT,fname TEXT,foccup TEXT,mname TEXT,moccup TEXT,dob TEXT,addr TEXT,phno TEXT,class_admt TEXT)')    #creating table within the database
    c.execute('INSERT INTO admission (date,appno,name,gender,bgroup,nationality,cat,fname,foccup,mname,moccup,dob,addr,phno,class_admt) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(date,appno,name,gender,bgroup,nationality,cat,fname,foccup,mname,moccup,dob,addr,phno,class_admt))    #inserting values into the table
    
    conn.commit()   #saving/commiting the database
        
    #tkinter.messagebox.showinfo(title='Message Box',message='Record inserted successfully...')  #message box
    print('Record inserted successfully...')
    
    conn.close()    #closing the connection    
    print ("Database closed successfully");
        
    #for new entry
    var_date.set(d1)
    appno = autoAppNoGen()  #calling auto application no. generation function again for new entry
    var_appno.set(appno)
    #reset all entries
    entry_name.delete(first=0,last='end')
    var_gender.set(None)        
    entry_bgroup.delete(first=0,last='end')
    var_nationality.set(value='---Select---')
    var_cat.set(value='---Select---')
    entry_fname.delete(first=0,last='end')
    entry_foccup.delete(first=0,last='end')
    entry_mname.delete(first=0,last='end')
    entry_moccup.delete(first=0,last='end')
    entry_dob.delete(first=0,last='end')
    entry_addr.delete(first=0,last='end')
    entry_phno.delete(first=0,last='end')
    entry_class_admt.delete(first=0,last='end')    
    
        
    


#form
root = tkinter.Tk()
root.title(string='KV | Admission Form')
root.geometry(newGeometry='500x600')


button_home = tkinter.Button(master=root,text='HOME',command=showHomeForm)
button_home.place(x=1)


button_exit = tkinter.Button(master=root,text='EXIT',command=exitAdmPortal)
button_exit.place(x=465)


label_heading = tkinter.Label(master=root,text='ADMISSION FORM',relief='solid',width=20,font=('bold',20))
label_heading.place(x=90,y=13)


label_date = tkinter.Label(master=root,text='DATE',width=20,font=('bold',10,'underline'))
label_date.place(x=80,y=63)
var_date = tkinter.StringVar()

today = date.today()    #get today's date
d1 = today.strftime("%d/%m/%Y") #convert today's date to dd/mm/yyyy format

var_date.set(d1)
entry_date = tkinter.Entry(master=root,textvariable=var_date,state='disabled')
entry_date.place(x=240,y=63)


label_appno = tkinter.Label(master=root,text='APPLICATION NO.',width=20,font=('bold',10,'underline'))
label_appno.place(x=80,y=93)
var_appno = tkinter.StringVar()
appno = autoAppNoGen()  #calling auto application no. generation function
var_appno.set(appno)
entry_appno = tkinter.Entry(master=root,textvariable=var_appno,state='disabled')
entry_appno.place(x=240,y=93)


label_name = tkinter.Label(master=root,text='Name',width=20,font=('bold',10))
label_name.place(x=80,y=130)
var_name = tkinter.StringVar()
entry_name = tkinter.Entry(master=root,textvariable=var_name)
entry_name.place(x=240,y=130)


label_gender = tkinter.Label(master=root,text='Gender',width=20,font=('bold',10))
label_gender.place(x=80,y=160)
var_gender = tkinter.IntVar()
radiobutton_gender_male = tkinter.Radiobutton(master=root,text='Male',padx=5,variable=var_gender,value=1)
radiobutton_gender_male.place(x=240,y=160)
radiobutton_gender_female = tkinter.Radiobutton(master=root,text='Female',padx=5,variable=var_gender,value=2)
radiobutton_gender_female.place(x=340,y=160)


label_bgroup = tkinter.Label(master=root,text='Blood Group',width=20,font=('bold',10))
label_bgroup.place(x=80,y=190)
var_bgroup = tkinter.StringVar()
entry_bgroup = tkinter.Entry(master=root,textvariable=var_bgroup)
entry_bgroup.place(x=240,y=190)


label_nationality = tkinter.Label(master=root,text='Nationality',width=20,font=('bold',10))
label_nationality.place(x=80,y=220)
list_nationality = ['Indian','Other']
var_nationality = tkinter.StringVar()
optionmenu_nationality = tkinter.OptionMenu(root,var_nationality,*list_nationality)
var_nationality.set(value='---Select---')
optionmenu_nationality.config(width=15)
optionmenu_nationality.place(x=240,y=220)


label_cat = tkinter.Label(master=root,text='Category',width=20,font=('bold',10))
label_cat.place(x=80,y=250)
list_cat = ['GEN','SC','ST','OBC','Other']
var_cat = tkinter.StringVar()
optionmenu_cat = tkinter.OptionMenu(root,var_cat,*list_cat)
var_cat.set(value='---Select---')
optionmenu_cat.config(width=15)
optionmenu_cat.place(x=240,y=250)


label_fname = tkinter.Label(master=root,text="Father's Name",width=20,font=('bold',10))
label_fname.place(x=80,y=280)
var_fname = tkinter.StringVar()
entry_fname = tkinter.Entry(master=root,textvariable=var_fname)
entry_fname.place(x=240,y=280)


label_foccup = tkinter.Label(master=root,text="Father's Occupation",width=20,font=('bold',10))
label_foccup.place(x=80,y=310)
var_foccup = tkinter.StringVar()
entry_foccup = tkinter.Entry(master=root,textvariable=var_foccup)
entry_foccup.place(x=240,y=310)


label_mname = tkinter.Label(master=root,text="Mother's Name",width=20,font=('bold',10))
label_mname.place(x=80,y=340)
var_mname = tkinter.StringVar()
entry_mname = tkinter.Entry(master=root,textvariable=var_mname)
entry_mname.place(x=240,y=340)


label_moccup = tkinter.Label(master=root,text="Mother's Occupation",width=20,font=('bold',10))
label_moccup.place(x=80,y=370)
var_moccup = tkinter.StringVar()
entry_moccup = tkinter.Entry(master=root,textvariable=var_moccup)
entry_moccup.place(x=240,y=370)


label_dob = tkinter.Label(master=root,text="D.O.B",width=20,font=('bold',10))
label_dob.place(x=80,y=400)
var_dob = tkinter.StringVar()
entry_dob = tkinter.Entry(master=root,textvariable=var_dob)
entry_dob.place(x=240,y=400)


label_addr = tkinter.Label(master=root,text="Address",width=20,font=('bold',10))
label_addr.place(x=80,y=430)
var_addr = tkinter.StringVar()
entry_addr = tkinter.Entry(master=root,textvariable=var_addr)
entry_addr.place(x=240,y=430)


label_phno = tkinter.Label(master=root,text='Contact No.',width=20,font=('bold',10))
label_phno.place(x=80,y=460)
var_phno = tkinter.StringVar()
entry_phno = tkinter.Entry(master=root,textvariable=var_phno)
entry_phno.place(x=240,y=460)


label_class_admt = tkinter.Label(master=root,text="Admission to class",width=20,font=('bold',10))
label_class_admt.place(x=80,y=490)
var_class_admt = tkinter.StringVar()
entry_class_admt = tkinter.Entry(master=root,textvariable=var_class_admt)
entry_class_admt.place(x=240,y=490)


button = tkinter.Button(master=root,text='SUBMIT',command=insertRecords)
button.place(x=240,y=520)


root.mainloop()
#viewApplication.py

import tkinter
import os
import sqlite3

#user-defined functions
def showHomeForm():
    global root     #root as global variable 
    root.destroy()  #exit current window
    os.system('python home.py') #executing another python script
    
def exitAdmPortal():
    global root
    root.destroy()

def viewRecords():    
    appno = var_appno.get() #getting value from textbox
        
    conn = sqlite3.connect('school.db')   #creating and connecting database
    print ("Opened database successfully");

    c = conn.cursor()   #defining a cursor

    c.execute('CREATE TABLE IF NOT EXISTS admission (date TEXT,appno TEXT,name TEXT,gender TEXT,bgroup TEXT,nationality TEXT,cat TEXT,fname TEXT,foccup TEXT,mname TEXT,moccup TEXT,dob TEXT,addr TEXT,phno TEXT,class_admt TEXT)')    #creating table within the database
    c.execute('SELECT * FROM admission WHERE appno = ?',(appno))    #retrieving values from the table

    f = 0
    for row in c:
        #setting values to textbox
        var_date.set(row[0])
        var_appno_2.set(row[1])
        var_name.set(row[2])
        var_gender.set(row[3])
        var_bgroup.set(row[4])
        var_nationality.set(row[5])
        var_cat.set(row[6])
        var_fname.set(row[7])
        var_foccup.set(row[8])
        var_mname.set(row[9])
        var_moccup.set(row[10])
        var_dob.set(row[11])
        var_addr.set(row[12])
        var_phno.set(row[13])    
        var_class.set(row[14])
        f = 1
        
    if(f == 1):
        #tkinter.messagebox.showinfo(title='Message Box',message='Record found...')  #message box
        print('Record found...')
    else:
        #tkinter.messagebox.showinfo(title='Message Box',message='Record not found...')
        print('Record not found...')

    conn.close()    #closing the connection
    print ("Database closed successfully");
        
    



#form
root = tkinter.Tk()
root.title(string='KV | View Application')
root.geometry(newGeometry='500x600')

button_home = tkinter.Button(master=root,text='HOME',command=showHomeForm)
button_home.place(x=1)

button_exit = tkinter.Button(master=root,text='EXIT',command=exitAdmPortal)
button_exit.place(x=465)

label_heading = tkinter.Label(master=root,text='VIEW APPLICATION',relief='solid',width=20,font=('bold',20))
label_heading.place(x=90,y=13)


label_appno = tkinter.Label(master=root,text='Enter application no.',width=20,font=('bold',10))
label_appno.place(x=80,y=63)
var_appno = tkinter.StringVar()
entry_appno = tkinter.Entry(master=root,textvariable=var_appno)
entry_appno.place(x=240,y=63)

button = tkinter.Button(master=root,text='VIEW',command=viewRecords)
button.place(x=240,y=93)


label_name = tkinter.Label(master=root,text='Name',width=20,font=('bold',10))
label_name.place(x=80,y=130)
var_name = tkinter.StringVar()
entry_name = tkinter.Entry(master=root,textvariable=var_name)
entry_name.place(x=240,y=130)

label_gender = tkinter.Label(master=root,text='Gender',width=20,font=('bold',10))
label_gender.place(x=80,y=160)
var_gender = tkinter.StringVar()
entry_gender = tkinter.Entry(master=root,textvariable=var_gender)
entry_gender.place(x=240,y=160)


label_bgroup = tkinter.Label(master=root,text='Blood Group',width=20,font=('bold',10))
label_bgroup.place(x=80,y=190)
var_bgroup = tkinter.StringVar()
entry_bgroup = tkinter.Entry(master=root,textvariable=var_bgroup)
entry_bgroup.place(x=240,y=190)

label_nationality = tkinter.Label(master=root,text='Nationality',width=20,font=('bold',10))
label_nationality.place(x=80,y=220)
var_nationality = tkinter.StringVar()
entry_nationality = tkinter.Entry(master=root,textvariable=var_nationality)
entry_nationality.place(x=240,y=220)

label_cat = tkinter.Label(master=root,text='Category',width=20,font=('bold',10))
label_cat.place(x=80,y=250)
var_cat = tkinter.StringVar()
entry_cat = tkinter.Entry(master=root,textvariable=var_cat)
entry_cat.place(x=240,y=250)

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

label_class = tkinter.Label(master=root,text="Admission to class",width=20,font=('bold',10))
label_class.place(x=80,y=490)
var_class = tkinter.StringVar()
entry_class = tkinter.Entry(master=root,textvariable=var_class)
entry_class.place(x=240,y=490)

label_appno_2 = tkinter.Label(master=root,text='APPLICATION NO.',width=20,font=('bold',10))
label_appno_2.place(x=80,y=520)
var_appno_2 = tkinter.StringVar()
entry_appno_2 = tkinter.Entry(master=root,textvariable=var_appno_2)
entry_appno_2.place(x=240,y=520)

label_date = tkinter.Label(master=root,text='DATE OF APPLICATION',width=20,font=('bold',10))
label_date.place(x=80,y=550)
var_date = tkinter.StringVar()
entry_date = tkinter.Entry(master=root,textvariable=var_date)
entry_date.place(x=240,y=550)


root.mainloop()
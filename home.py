#home.py

import tkinter
import os

def showAdmForm():
    global root     #root as global variable
    root.destroy()  #exit current window
    os.system('python admissionForm.py') #executing another python script
    
def showViewAppForm():
    global root
    root.destroy()
    os.system('python viewApplication.py')
    
def exitAdmPortal():
    global root
    root.destroy()
    




#form
root = tkinter.Tk()
root.title(string='Admission Portal')
root.geometry(newGeometry='500x600')

label_heading = tkinter.Label(master=root,text='XYZ SCHOOL',relief='ridge',width=20,font=('bold',20))
label_heading.place(x=90,y=150)

label_heading = tkinter.Label(master=root,text='ADMISSION PORTAL',relief='groove',width=20,font=('bold',13))
label_heading.place(x=150,y=200)

button_adm_form = tkinter.Button(master=root,text='Admission Form',command=showAdmForm)
button_adm_form.place(x=190,y=250)

button_view = tkinter.Button(master=root,text='View Application',command=showViewAppForm)
button_view.place(x=190,y=290)

button_exit = tkinter.Button(master=root,text='EXIT',command=exitAdmPortal)
button_exit.place(x=222,y=330)

root.mainloop()

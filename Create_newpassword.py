from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

import sqlite3

co = sqlite3.connect("signupfile1.db")
c= co.cursor()

#def clear():
    #UsernameEntry.delete(0,END)
    #newPasswordEntry.delete(0, END)
    #confirmPasswordEntry.delete(0, END)

def connect_database():

    if UsernameEntry.get() == '' or newPasswordEntry.get() == '' or confirmPasswordEntry.get() == '':
        messagebox.showerror('Error', 'All fields are Required')
    elif newPasswordEntry.get() != confirmPasswordEntry.get():
        messagebox.showerror('Error', 'Password does not match')
    else:
         messagebox.showinfo('Success', 'Registration is Successful')
         query= 'use Userdata'
         c.execute(query)
         query='select * from data where Username=%s and password=%s'
         c.execute(query, UsernameEntry.get(), newPasswordEntry.get())
         co.commit()
         #clear()
         newpassword_window.destroy()
         import signin


newpassword_window= Tk()

newpassword_window.title('Signin Page')
newpassword_window.resizable(False, False)
background=ImageTk.PhotoImage(file='bg3.jpg')

bgLabel= Label(newpassword_window, image=background)
bgLabel.pack()

heading = Label(newpassword_window, text="X Shopping Outlet", font= ("Times New Roman", 25, 'bold'),
                bg='white', fg='firebrick1')
heading.place(x=540, y=80)


Usernamelabel = Label(newpassword_window, text='Username:', font=("Times New Roman", 15, 'bold'), fg='firebrick1', bg='white')
Usernamelabel.place(x= 520, y= 170)
UsernameEntry = Entry(newpassword_window, width=28, font=("Times New Roman", 16,),
                      bg='white', bd=0, fg='firebrick1')
UsernameEntry.place(x=530, y=200)

newPasswordlabel = Label(newpassword_window, text=' New Password:', font=("Times New Roman", 15, 'bold'), fg='firebrick1', bg='white')
newPasswordlabel.place(x= 520, y= 240)
newPasswordEntry = Entry(newpassword_window, width=28, font=("Times New Roman", 16,),
                      bg='white', fg='firebrick1', bd=0)
newPasswordEntry.place(x=530, y=270)

confirmPasswordlabel = Label(newpassword_window, text=' Confirm New Password:', font=("Times New Roman", 15, 'bold'), fg='firebrick1', bg='white')
confirmPasswordlabel.place(x= 520, y= 310)
confirmPasswordEntry = Entry(newpassword_window, width=28, font=("Times New Roman", 16,),
                      bg='white', fg='firebrick1', bd=0)
confirmPasswordEntry.place(x=530, y=340)


Setbutton=Button(newpassword_window, text='Set Password', font=('Open Sans',20, 'bold'),width=10, fg='firebrick1',
                   bg='white',  activeforeground='gray',activebackground='white',bd=0, command=connect_database)
Setbutton.place(x=560, y=380)


newpassword_window.mainloop()


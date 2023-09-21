from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

import sqlite3


#fortable
co = sqlite3.connect("signupfile1.db")
c= co.cursor()
co.commit()


def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)



def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()==''or confirmEntry.get()=='':
        messagebox.showerror('Error', 'All fields are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    else:
         messagebox.showinfo('Success', 'Registration is Successful')

         c.execute('INSERT INTO example (email, Username, password, permission) VALUES '
                   '("'+emailEntry.get()+'","'+usernameEntry.get()+'", "'+confirmEntry.get()+'","user")')
         co.commit()
         clear()
         signup_window.destroy()
         import signin
        
def login_page():
    signup_window.destroy()
    import signin

#Overlook


signup_window= Tk()
signup_window.title('Signup Page')
signup_window.resizable(False, False)
background=ImageTk.PhotoImage(file='bg3.jpg')

bgLabel= Label(signup_window, image=background)
bgLabel.pack()

frame= Frame(signup_window, bg='white')
frame.place(x=510, y=80)

#varibale declaration
global email
global username
global password

#heading

heading = Label(frame, text="X Shopping Outlet", font=("Times New Roman", 25, 'bold'),
                bg='white', fg='firebrick1')
heading.grid(row=0, column=0,padx=20, pady=10)

#Email

emaillabel= Label(frame, text='Email*',font=("Times New Roman",15, 'bold'), fg='firebrick1',bg='white')
emaillabel.grid(row=1, column=0, sticky='w',padx=20, pady=5)
emailEntry= Entry(frame, width=28, font=("Times New Roman", 15, 'bold'), bg='firebrick1', fg='white', bd=0)
emailEntry.grid(row=2, column=0, sticky='w', padx=20)

#Username

usernamelabel= Label(frame, text='Username*', font=("Times New Roman", 15, 'bold'), fg='firebrick1', bg='white')
usernamelabel.grid(row=3, column=0, sticky='w', padx=20, pady=5)
usernameEntry= Entry(frame, width=28, font=("Times New Roman", 15, 'bold'), bg='firebrick1', fg='white', bd=0)
usernameEntry.grid(row=4, column=0, sticky='w', padx=20)

#password

passwordlabel= Label(frame, text='Password*', font=("Times New Roman", 15, 'bold'), fg='firebrick1', bg='white')
passwordlabel.grid(row=5, column=0, sticky='w', padx=20, pady=5)
passwordEntry= Entry(frame, width=28, font=("Times New Roman", 15, 'bold'),
                    bg='firebrick1', fg='white', bd=0)
passwordEntry.grid(row=6, column=0, sticky='w', padx=20)

#confirm Password

confirmlabel= Label(frame, text='Confirm Password', font=("Times New Roman", 15, 'bold'), fg='firebrick1', bg='white')
confirmlabel.grid(row=7, column=0, sticky='w', padx=20, pady=5)
confirmEntry= Entry(frame, width=28, font=("Times New Roman", 15, 'bold'),
                    bg='firebrick1', fg='white', bd=0)
confirmEntry.grid(row=8, column=0, sticky='w', padx=20)

#checkbutton

#termsandcinditions = Checkbutton(frame, text='I agree to the Terms and Conditions', font=("Times New Roman", 11, 'bold'),
                                 #bg='white', fg='firebrick1', bd=0)
#termsandcinditions.grid(row=9, column=0, sticky='w', padx=20, pady=10)

#signup button

signupbutton=Button(frame, text='Signup', font=('Open Sans',20, 'bold'),width=10, fg='firebrick1',
                   bg='white', activeforeground='gray',activebackground='white', bd=0,
                    command=connect_database)
signupbutton.grid(row=10, column=0, sticky='w', padx=50, pady=20)

#back to sign in

signinlabel = Label(frame, text='Already have an Account?', font=('Open Sans', 10, 'bold'),fg='firebrick1',
                    bg='white')
signinlabel.grid(row=11, column=0, sticky='w', padx=20, pady=10)

loginbutton=Button(frame, text= 'Login', font=('Open Sans',9, 'bold underline'), fg='blue',bg='white'
                             , activeforeground='blue',activebackground='white', cursor='hand2', bd=0,
                    command=login_page)
loginbutton.place(x=160, y=375)


signup_window.mainloop()



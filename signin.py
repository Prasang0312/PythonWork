from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

import sqlite3

def signin_page():
    if UsernameEntry.get() =='' or PasswordEntry.get() =='':
        messagebox.showerror('Error', 'All fields are Required')
    else:
        co = sqlite3.connect("signupfile1.db")
        c = co.cursor()
        c.execute('SELECT password, permission FROM example WHERE username="'+UsernameEntry.get()+'" ')
        x=c.fetchall()
        if(x==[]):
            messagebox.showerror('Error', 'Username not registered')
        else:
            if PasswordEntry.get() != str(x[0][0]):
                messagebox.showerror('Error', 'Password Mismatch')

            else:
                if(x[0][1]=="user"):
                    messagebox.showinfo('Success', 'Login as User')
                elif(x[0][1]=="admin"):
                    messagebox.showinfo('Success', 'Login as Admin')
                else:
                    messagebox.showinfo('Success', 'Login as Salesstaff')

    login_window.destroy()
    import Shop_page


def create_newpassword():
    login_window.destroy()
    import Create_newpassword


def signup_page():
    login_window.destroy()
    import signup

#structure

login_window = Tk()
login_window.title('Login Page')
login_window.resizable(False, False)

bgImage = ImageTk.PhotoImage(file='bg3.jpg')

bgLabel = Label(login_window, image=bgImage)
bgLabel.pack()

#headings

heading = Label(login_window, text="X Shopping Outlet", font= ("Times New Roman", 25, 'bold'),
                bg='white', fg='firebrick1')
heading.place(x=540, y=80)

#username

Usernamelabel = Label(login_window, text='Username:', font=("Times New Roman", 15, 'bold'), fg='firebrick1', bg='white')
Usernamelabel.place(x= 520, y= 170)
UsernameEntry = Entry(login_window, width=28, font=("Times New Roman", 16,),
                      bg='white', bd=0, fg='firebrick1')
UsernameEntry.place(x=530, y=200)


#Password

Passwordlabel = Label(login_window, text='Password:', font=("Times New Roman", 15, 'bold'), fg='firebrick1', bg='white')
Passwordlabel.place(x= 520, y= 240)
PasswordEntry = Entry(login_window, width=28, font=("Times New Roman", 16,),
                      bg='white', fg='firebrick1', bd=0)
PasswordEntry.place(x=530, y=270)


#forgot Password?

forgetButton= Button(login_window,text='Forgot Password?', bg='white', cursor='hand2'
                     ,font=('Times New Roman',12, 'bold'),fg='firebrick1',bd=2, command= create_newpassword)
forgetButton.place(x=632, y=310)

#Login

loginbutton=Button(login_window, text='Login', font=('Open Sans',20, 'bold'),width=10, fg='firebrick1',
                   bg='white',  activeforeground='gray',activebackground='white',bd=0,command=signin_page)
loginbutton.place(x=560, y=350)

#----- or-------

orlabel = Label(login_window, text='------------- OR -------------', font=('Open Sans', 16),fg='firebrick1',
                bg='white')
orlabel.place(x=535,y=400 )

#Create a new Account

signuplabel = Label(login_window, text='Dont have an Account?', font=('Open Sans', 10, 'bold'),fg='firebrick1',
                    bg='white')
signuplabel.place(x=520,y=450)

neuaccountbutton=Button(login_window, text= 'Create a New Account', font=('Open Sans',8, 'bold underline'), fg='blue',bg='white'
                             , activeforeground='blue',activebackground='white', cursor='hand2', bd=0,
                        command=signup_page)
neuaccountbutton.place(x=650, y=450)


login_window.mainloop()
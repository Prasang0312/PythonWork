from tkinter import *
from PIL import ImageTk

#def clear():
    #jeans_label.deletecommand('none')
    #jeans_info.deletecommand('none')
    #jeans_sb.delete(0,END)
    #hoodie_label.deletecommand('none')
    #hoodie_info.deletecommand('none')
    #hoodie_sb.delete(0, END)
    #tshirt_label.deletecommand('none')
    #tshirt_info.deletecommand('none')
    #tshirt_sb.delete(0, END)


def button_clicked():
    #clear()


    frame = Frame(shopping_window, bg='pink', highlightbackground="black", highlightthickness=1, width=350, height=550)
    frame.place(x=500, y=50)
    Bill = Label(frame, text="Your Cart", font=('calibri', 25, 'bold'), fg='firebrick1', bg='white')
    Bill.place(x=120, y=20)

    jeans_total= int(jeans_sb.get()) *39
    hoodie_total = int(hoodie_sb.get()) *29
    tshirt_total = int (tshirt_sb.get()) *25

    total_bill = jeans_total + hoodie_total + tshirt_total
    iteam1 = Label (frame, text = f"Iteam-1: Jeans = £{jeans_total}",font=('Open Sans',18, 'bold'), fg='firebrick1',
                    bg='pink')
    iteam1.place(x = 50, y= 80)

    iteam2 = Label (frame, text = f"Iteam-2: Hoodie = £{hoodie_total}",font=('Open Sans',18, 'bold'), fg='firebrick1',
                    bg='pink')
    iteam2.place(x = 50, y= 120)

    iteam3 = Label (frame, text = f"Iteam-3: T-Shirts = £{tshirt_total}",font=('Open Sans',18, 'bold'), fg='firebrick1',
                    bg='pink')
    iteam3.place(x = 50, y= 160)

    bills = Label (frame, text = f"Your Total Payment is £{total_bill}",font=('Open Sans',18, 'bold'), fg='firebrick1',
                   bg='White', bd=1 )
    bills.place(x = 50, y= 220)

    Paybutton = Button(frame, text='PAY NOW', font=('Open Sans', 25, 'bold'), width=10, fg='firebrick1',
                          bg='white', activeforeground='pink', activebackground='white', bd=0, command=button_clicked)
    Paybutton.place(x=70, y=300)

#windowdesign
shopping_window= Tk()
shopping_window.title("Welcome To X Shopping Outlet")


bgImage = ImageTk.PhotoImage(file='bg4.jpg')
bgLabel = Label(shopping_window, image=bgImage)
bgLabel.pack()
shopping_window.resizable(False, False)



#Company Name Label :

heading = Label(shopping_window, text="X Fashions \n Choose Your Fashion", font= ("Times New Roman", 30, 'bold'),
                bg='pink', fg='firebrick1')
heading.place(x=450, y=20)

#Products Details
''
#jeans

jeansImage = ImageTk.PhotoImage(file="jeans.jpg")
jeans_label = Label(image=jeansImage, borderwidth=0)
jeans_label.place(x=200, y=100)
jeans_info = Label(shopping_window, text="Blue Jeans\n£39", font=("Times New Roman", 18 , 'bold'), fg='firebrick1', bg='pink')
jeans_info.place (x=200, y=350)
jeans_sb = Spinbox(from_=0, to=10, width=5)
jeans_sb.place(x=290, y=358)

#hoodie

hoodieImage = ImageTk.PhotoImage(file="hoodie.jpg")
hoodie_label = Label(image=hoodieImage, borderwidth=0)
hoodie_label.place(x=500, y=100)
hoodie_info = Label(shopping_window, text="Blue Hoodie\n£29", font=("Times New Roman", 18 , 'bold'), fg='firebrick1', bg='pink')
hoodie_info.place (x=500, y=350)
hoodie_sb = Spinbox(from_=0, to=10, width=5)
hoodie_sb.place(x=602, y=358)

#tshirt

tshirtImage = ImageTk.PhotoImage(file="tshirt.jpg")
tshirt_label = Label(image=tshirtImage, borderwidth=0)
tshirt_label.place(x=800, y=100)
tshirt_info = Label(shopping_window, text="T-Shirts\n£25", font=("Times New Roman", 18 , 'bold'), fg='firebrick1', bg='pink')
tshirt_info.place (x=800, y=350)
tshirt_sb = Spinbox(from_=0, to=10, width=5)
tshirt_sb.place(x=872, y=358)

#finish

finishbutton = Button(shopping_window, text='Order',font=('Open Sans',25, 'bold'),width=10, fg='firebrick1',
                   bg='white',  activeforeground='pink',activebackground='white',bd=0,command= button_clicked)
finishbutton.place(x=500, y=450)



shopping_window.mainloop()


from tkinter import *
from PIL import ImageTk

#import Shop_page


#def jeans_sb():
    #jeans_total= Shop_page.jeans_sb.get() * 39

#def hoodie_sb():
    #hoodie_total = Shop_page.hoodie_sb.get() * 29

bill_window= Tk()
bill_window.title("Thank You for choosing US")
bill_window.resizable(False, False)
background = ImageTk.PhotoImage(file='bg4.jpg')

bgLabel = Label(bill_window, image=background)
bgLabel.pack()

frame= Frame(bill_window, bg='pink',highlightbackground="black", highlightthickness=1 ,width=350, height=550)
frame.place(x=750, y=50)
Bill = Label(frame, text="Your Bill", font=('calibri',25, 'bold'), fg='firebrick1', bg='white')
Bill.place(x=120, y=20)

#jeans_total = Label(frame, text=f"Jeans = {Shop_page.jeans_sb.get()}", font=('calibri',25, 'bold'), fg='firebrick1', bg='white')
j#eans_total.place(x=50, y=20)

#hoodie_total = Label(frame, text=f"Hoodie = {Shop_page.hoodie_sb.get()}", font=('calibri',25, 'bold'), fg='firebrick1', bg='white')
#hoodie_total.place( x=50, y=40)


#billing name





bill_window.mainloop()
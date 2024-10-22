from tkinter import *
from tkinter import messagebox, Label

window=Tk()
window.config(bg="Blue")
window.geometry("500x600")
window.title("Discount Page")
#user defined function
def discount():
    amt=int(e1.get())
    if(amt>=500):
        dis=(amt*15)/100
        total_amt_to_be_paid=amt-dis
        messagebox.showinfo("Amount to be paid after discount",total_amt_to_be_paid)
    elif(amt<500 and amt>=300):
        dis=(amt*10)/100
        total_amt=amt-dis
        messagebox.showinfo("Amount to be paid after discount of 10%:",total_amt)
    else:
        messagebox.showinfo("The acutal amount need to be paid:",amt)

l1=Label(window,text="Enter Billed amount:",font=30)
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)
button1=Button(window,text="Submit",command=discount)
button1.grid(row=1,column=1)

window.mainloop()
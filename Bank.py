from tkinter import *
from tkinter import messagebox
window=Tk()
window.config(bg="Blue")
window.geometry("500x600")
window.title("Bank Loan")
#user define function
def bank_loan():
    age=int(e2.get())
    salary=int(e3.get())
    credit_score=int(e4.get())
    if (age>=21 and age<60):
        if (salary>20000):
            if(credit_score>=650):
                messagebox.showinfo("Result:","Approved")
    else:
        messagebox.showinfo("Result","Failed")
l1=Label(window,text="Age:",font=25)
l1.grid(row=0,column=0)
l2=Label(window,text="Salary:",font=25)
(l2.grid(row=1,column=1))
l3=Label(window,text="Credit Score",font=25)
l3.grid(row=2,column=2)
e2=Entry(window)
e2.grid(row=0,column=1)
e3=Entry(window)
e3.grid(row=1,column=2)
e4=Entry(window)
e4.grid(row=2,column=3)
b1=Button(window,text="Submit",command=bank_loan)
b1.grid(row=5,column=7)

window.mainloop()
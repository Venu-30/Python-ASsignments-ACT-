from tkinter import*
from tkinter import  messagebox
from tkinter.ttk import Label

window=Tk()
window.config(bg="Yellow")
window.geometry("500x600")
window.title("Speed")
#user define function
def car_speed():
    speed_limit=90
    speed=int(e1.get())
    if (speed<=speed_limit):
        messagebox.showinfo("Normal","No Fine")
    elif (speed>speed_limit and speed<=speed_limit+20):
        messagebox.showinfo("Warning","Go Slow")
    else:
        messagebox.showinfo("Fine","1000 rs")


l1=Label(window,text="speed")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)
b1=Button(window,text="check",command=car_speed)
b1.grid(row=0,column=2)
window.mainloop()

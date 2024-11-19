from tkinter import *
import pymongo


class Person:
    def __init__(self, window):
        self.window = window
        self.window.title("GYM MEMBERSHIP")
        self.window.geometry("600x450")
        self.window.configure(bg="black")

        # Initialize variables
        self.id_number = IntVar()
        self.name = StringVar()
        self.age = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.membership = StringVar()
        self.job = StringVar()
        self.Payment_mode = StringVar()

        # Create and place widgets
        Label(window, text="ID_NUMBER", width=15, bg="yellow").grid(row=0, column=0, padx=5, pady=5)
        Entry(window, textvariable=self.id_number, width=25).grid(row=0, column=1, padx=5, pady=5)

        Label(window, text="Name", width=15, bg="yellow").grid(row=0, column=2, padx=5, pady=5)
        Entry(window, textvariable=self.name, width=25).grid(row=0, column=3, padx=5, pady=5)

        Label(window, text="Age", width=15, bg="yellow").grid(row=1, column=0, padx=5, pady=5)
        Entry(window, textvariable=self.age, width=25).grid(row=1, column=1, padx=5, pady=5)

        Label(window, text="Phone", width=15, bg="yellow").grid(row=1, column=2, padx=5, pady=5)
        Entry(window, textvariable=self.phone, width=25).grid(row=1, column=3, padx=5, pady=5)

        Label(window, text="Mail_ID", width=15, bg="yellow").grid(row=2, column=0, padx=5, pady=5)
        Entry(window, textvariable=self.email, width=25).grid(row=2, column=1, padx=5, pady=5)

        Label(window, text="Membership", width=15, bg="yellow").grid(row=2, column=2, padx=5, pady=5)
        Entry(window, textvariable=self.membership, width=25).grid(row=2, column=3, padx=5, pady=5)

        Label(window, text="JOB", width=15, bg="yellow").grid(row=3, column=0, padx=5, pady=5)
        Entry(window, textvariable=self.job, width=25).grid(row=3, column=1, padx=5, pady=5)

        Label(window, text="Payment_mode", width=15, bg="yellow").grid(row=3, column=2, padx=5, pady=5)
        Entry(window, textvariable=self.Payment_mode, width=25).grid(row=3, column=3, padx=5, pady=5)

        # Buttons
        Button(window, text="SUBMIT", command=self.enroll, bg="green", width=15).grid(row=4, column=0, pady=20)
        Button(window, text="UPDATE", command=self.update, bg="blue", width=15).grid(row=4, column=1, pady=20)
        Button(window, text="DELETE", command=self.delete, bg="red", width=15).grid(row=4, column=2, pady=20)
        Button(window, text="CLEAR", command=self.clear, bg="gray", width=15).grid(row=4, column=3, pady=20)

    def enroll(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["MUSCLE_GEAR_GYM"]
        collection = db["MEMBERS"]

        data = {
            "id_number": self.id_number.get(),
            "name": self.name.get(),
            "age": self.age.get(),
            "phone": self.phone.get(),
            "email": self.email.get(),
            "membership": self.membership.get(),
            "job": self.job.get(),
            "Payment_mode": self.Payment_mode.get()
        }

        result = collection.insert_one(data)
        print("Data has been inserted successfully:", result.inserted_id)
        self.clear()

    def update(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["MUSCLE_GEAR_GYM"]
        collection = db["MEMBERS"]

        query = {"id_number": self.id_number.get()}
        new_values = {"$set": {
            "name": self.name.get(),
            "age": self.age.get(),
            "phone": self.phone.get(),
            "email": self.email.get(),
            "membership": self.membership.get(),
            "job": self.job.get(),
            "Payment_mode": self.Payment_mode.get()
        }}

        result = collection.update_one(query, new_values)
        if result.matched_count > 0:
            print("Data has been updated successfully.")
        else:
            print("No matching record found.")
        self.clear()

    def delete(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["MUSCLE_GEAR_GYM"]
        collection = db["MEMBERS"]

        query = {"id_number": self.id_number.get()}
        result = collection.delete_one(query)
        if result.deleted_count > 0:
            print("Data has been deleted successfully.")
        else:
            print("No matching record found.")
        self.clear()

    def clear(self):
        self.id_number.set("")
        self.name.set("")
        self.age.set("")
        self.phone.set("")
        self.email.set("")
        self.membership.set("")
        self.job.set("")
        self.Payment_mode.set("")


# Create and run the application
window = Tk()
ob = Person(window)
window.mainloop()





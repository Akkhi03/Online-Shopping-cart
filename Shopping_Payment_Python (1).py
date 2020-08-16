from tkinter import *
import tkinter.messagebox as tm
import mysql.connector
from tkinter import ttk
import os
from PIL import Image, ImageTk
conn = mysql.connector.connect(host='localhost', port=3306, user='root', passwd='Ishwar003', db='db')
cur = conn.cursor()

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

     


        #w = Label(master, text="Rouge", fg="red")
        w = Label(master, text="Payment", bg="red",fg="white",font=("Times New Roman", 19))
        w.pack(fill=X)
       
        
        w1 = Label(master, text="", font=("Courier New", 18))
        w1.pack()
        w2 = Label(master, text="", font=("Courier New", 18))
        w2.pack()

        w3 = Label(master, text="Enter The Card Details", bg="white",fg="BLUE",font=("Times New Roman", 15))
        w3.pack(fill=X)

        w3 = Label(master, text="",font=("Courier New", 18))
        w3.pack()
        
        self.label_1 = Label(self, text="Item Code",bg="white",fg="BLUE")
        self.label_11 = Label(self, text="Amount",bg="white",fg="BLUE")
        self.label_2 = Label(self, text="Card Number",bg="white",fg="BLUE")
        self.label_3 = Label(self, text="Expired Date",bg="white",fg="BLUE")
        self.label_4 = Label(self, text="CVC",bg="white",fg="BLUE")
        self.label_5 = Label(self, text="Amount",bg="white",fg="BLUE")
        

        self.entry_1 = Entry(self)
        self.entry_1.insert(END, 0)

        self.entry_11 = Entry(self)
        self.entry_11.insert(END, 0)
        
        self.entry_2 = Entry(self)
        self.entry_2.insert(END, '')
        self.entry_3 = Entry(self)
        self.entry_3.insert(END, 0)
        self.entry_4 = Entry(self)
        self.entry_4.insert(END, 0)
        self.entry_5 = Entry(self)
        self.entry_5.insert(END, 0)
        
        
        
        self.label_1.grid(row=13, sticky=E)
        self.label_2.grid(row=14, sticky=E)
        self.label_3.grid(row=15, sticky=E)
        self.label_4.grid(row=16, sticky=E)
        self.label_5.grid(row=17, sticky=E)
        
        self.entry_1.grid(row=13, column=1)
        self.entry_2.grid(row=14, column=1)
        self.entry_3.grid(row=15, column=1)
        self.entry_4.grid(row=16, column=1)
        self.entry_11.grid(row=17, column=1)
        
        self.pack()
        

        
        

        
        self.logbtn = Button(self, text="Make Payment", bg="lightblue", width=20,command = self._add_btn_clickked)
        self.logbtn.grid(row=18, column=0)
        
        
        self.logbtn1 = Button(self, text="Quit", bg="lightblue", width=20,command = self._view_btn_clickked)
        self.logbtn1.grid(row=18, column=1)
        
        
        

    def _add_btn_clickked(self):
        #print("Clicked")
        itno = int(self.entry_1.get())
        
        amount = int(self.entry_11.get())
        
        
        if itno==0 and amount==0:
            tm.showerror("Entry Error", "Fill Your all fields")
        else:
            cur.execute ("""UPDATE shopping1 SET amt='PAID' WHERE itno='%d' """ % (itno))
            conn.commit()
            tm.showinfo("Confirmation","Payment Succesful")
        
    def _view_btn_clickked(self):
        pass
            
        
root = Tk()
root.geometry("320x240")
tree = ttk.Treeview(root)

root.title("Payment Gateway")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 400
height = 400
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)
lf = LoginFrame(root)
root.mainloop()

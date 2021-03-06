from tkinter import *
import tkinter.messagebox as tm
import mysql.connector
from tkinter import ttk
import sys
import PIL
from PIL import Image, ImageTk


conn = mysql.connector.connect(host='localhost', port=3306, user='root', passwd='Ishwar003', db='db')
cur = conn.cursor()

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        
        w = Label(master, text="Shopping Cart Management", bg="red",fg="white",font=("Times New Roman", 28))
        w.pack(fill=X)
        w1 = Label(master, text="", font=("Courier New", 18))
        w1.pack()
        w2 = Label(master, text="", font=("Courier New", 18))
        w2.pack()
        w3 = Label(master, text="Enter the purchase details", bg="white",fg="BLUE",font=("Times New Roman", 18))
        w3.pack(fill=X)
        w4 = Label(master, text="",font=("Courier New", 18))
        w4.pack()
        
        self.label_1 = Label(self, text="Item Code",bg="white",fg="BLUE")
        self.label_2 = Label(self, text="Item Name",bg="white",fg="BLUE")
        self.label_3 = Label(self, text="Quantity",bg="white",fg="BLUE")
        self.label_4 = Label(self, text="Rate of Single Quantity",bg="white",fg="BLUE")
        

        self.entry_1 = Entry(self)
        self.entry_1.insert(END, 0)
        self.entry_2 = Entry(self)
        self.entry_2.insert(END, '')
        self.entry_3 = Entry(self)
        self.entry_3.insert(END, 0)
        self.entry_4 = Entry(self)
        self.entry_4.insert(END, 0)
                     
        self.label_1.grid(row=13, sticky=E)
        self.label_2.grid(row=15, sticky=E)
        self.label_3.grid(row=17, sticky=E)
        self.label_4.grid(row=19, sticky=E)
       
        self.entry_1.grid(row=13, column=1)
        self.entry_2.grid(row=15, column=1)
        self.entry_3.grid(row=17, column=1)
        self.entry_4.grid(row=19, column=1)
        
        self.pack()
                
        self.logbtn = Button(self, text="Add Item", bg="lightblue", width=20,command = self._add_btn_clickked)
        self.logbtn.grid(row=21, column=0)
                
        self.logbtn1 = Button(self, text="View Item", bg="lightblue", width=20,command = self._view_btn_clickked)
        self.logbtn1.grid(row=21, column=1)
        
        self.logbtn2 = Button(self, text="Make Payment", bg="lightblue", width=20,command = self._update_btn_clickked)
        self.logbtn2.grid(row=21, column=2)
        
        self.logbtn3 = Button(self, text="Delete Item",bg="lightblue", width=20, command = self._delete_btn_clickked)  
        self.logbtn3.grid(row=21, column=3)

        self.logbtn4 = Button(self, text="Quit",bg="lightblue", width=20, command = self.quit)
        self.logbtn4.grid(row=21, column=4)
        
        self.logbtn5 = Button(self, text="Clear",bg="lightblue", width=20, command = self.delete)
        self.logbtn5.grid(row=21, column=5)
        

    def _add_btn_clickked(self):
        
        itno = int(self.entry_1.get())
        itname = self.entry_2.get().upper()
        qty = int(self.entry_3.get())
        rate = int(self.entry_4.get())
        tot=qty*rate
        amt="NOT PAID"
        if itno==0 and itname=='' and qty==0 and rate==0 and tot==0:
            tm.showerror("Entry Error", "Fill Your all fields")
        else:
            cur.execute("""INSERT INTO shopping1 VALUES (%s,%s,%s,%s,%s,%s)""",(itno,itname,qty,rate,tot,amt))
            conn.commit()
            tm.showinfo(" ","Items Added")
        
    def _view_btn_clickked(self):
        
        tree["columns"] = ("one", "two", "three","four","five","six")
        tree.column("one", width=100)
        tree.column("two", width=100)
        tree.column("three", width=100)
        tree.column("four", width=100)
        tree.column("five", width=100)
        tree.column("six", width=100)

        tree.heading("#0", text='S.NO')
        tree.heading("one", text="ITEM CODE")
        tree.heading("two", text="ITEM NAME")
        tree.heading("three", text="QUANTITY")
        tree.heading("four", text="RATE")
        tree.heading("five", text="TOTAL AMOUNT")
        tree.heading("six", text="PAID STATUS")
        cur.execute("""select * from shopping1""")
        cpt = 0 # Counter representing the ID of your code.
        for row in cur:
        
            tree.insert('', 'end', text=str(cpt), values=(row[0], row[1],row[2],row[3],row[4],row[5]), tags = ('oddrow','evenrow'))
            
            tree.tag_configure('oddrow', background='orange')
            tree.tag_configure('evenrow', background='white')
            cpt += 1 # i

        tree.pack()
        conn.commit()
        
    def delete(self):
        chil=tree.get_children()
        for i in chil:
            tree.delete(i)
        tm.showinfo("Data Cleared","Data has been Cleared")
        
    def delete1(self):
        chil=tree.get_children()
        for i in chil:
            tree.delete(i)
        
    def _update_btn_clickked(self):
        if __name__ == '__main__':
            import Shopping_Payment
            Shopping_Payment.LoginFrame(root)
        

    def _delete_btn_clickked(self):
        
     
        itno = int(self.entry_1.get())
        
        if itno==0:
            tm.showerror("Item Number Error","Please! Type the Item Number")
        else:
            sql = """DELETE FROM shopping1 WHERE itno= '%d'""" % (itno)
            cur.execute(sql)
            conn.commit()
            tm.showinfo(" ","Items Deleted")
            self.delete1()

    def _quit_btn_clickked(self):
        
        raise SystemExit
        sys.exit()
        
root = Tk()
root.geometry("320x240")
tree = ttk.Treeview(root)
root.title("Python: Shopping Application")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 600
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)
lf = LoginFrame(root)
root.mainloop()


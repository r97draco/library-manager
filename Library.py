from tkinter import *
from tkinter import messagebox
import sqlite3
class Users:
    def __init__(self):
        self.r1=Tk()
        self.r1.geometry("400x400")
        self.r1.title("Members")
        self.l=Label(self.r1,text="Members",font=("bold",25))
        self.b1=Button(self.r1,text="Add member",font=("normal",20),width=12,command=self.AddMembers)
        self.b2=Button(self.r1,text="All member",font=("normal",20),width=12,command=self.AllMembers)
        self.b3=Button(self.r1,text="Defaulter",font=("normal",20),width=12,command=self.Defaulters)
        self.l.place(x=150,y=10)
        self.b1.place(x=100,y=90)
        self.b2.place(x=100,y=170)
        self.b3.place(x=100,y=240)
    def AddMembers(self):
        c1=AddMember()
    def AllMembers(self):
        c2=AllMember()
    def Defaulters(self):
        c3=Defaulter()
    
class AllBook:
    def __init__(self):
        self.r3=Tk()
        self.r3.geometry("400x400")
        self.r3.title("All Books")
        self.l=Label(self.r3,text="All Books",font=("bold",25))
        self.lb=Listbox(self.r3,width=58,height=18)
        self.l.place(x=120,y=10)
        self.lb.place(x=20,y=70)
        db = sqlite3.connect("Librarydb.db")
        data=db.execute("select * from Books")
        for row in data:
            self.lb.insert(END,row)
        db.close()
class AllMember:
    def __init__(self):
        self.r3=Tk()
        self.r3.geometry("400x400")
        self.r3.title("All Members")
        self.l=Label(self.r3,text="All Members",font=("bold",25))
        self.lb=Listbox(self.r3,width=58,height=18)
        self.l.place(x=120,y=10)
        self.lb.place(x=20,y=70)
        db = sqlite3.connect("Librarydb.db")
        data=db.execute("select * from Members")
        for row in data:
            self.lb.insert(END,row)
        db.close()
class IssueBooks:
    def __init__(self):
        self.r3=Tk()
        self.r3.geometry("400x400")
        self.r3.title("Issue Books")
        self.l=Label(self.r3,text="Issue Books",font=("bold",25))
        self.l1=Label(self.r3,text="Name:",font=("normal",20))
        self.l2=Label(self.r3,text="Subject:",font=("normal",20))
        self.l3=Label(self.r3,text="User Id:",font=("normal",20))
        self.t1=Entry(self.r3,width=15,font=("normal",20))
        self.t2=Entry(self.r3,width=15,font=("normal",20))
        self.t3=Entry(self.r3,width=15,font=("normal",20))
        self.b1=Button(self.r3,text="Issue",font=("normal",20),command=self.do)
        self.l.place(x=120,y=10)
        self.l1.place(x=10,y=80)
        self.l2.place(x=10,y=140)
        self.l3.place(x=10,y=200)
        self.t1.place(x=130,y=80)
        self.t2.place(x=130,y=140)
        self.t3.place(x=130,y=200)
        self.b1.place(x=150,y=300)
    def do(self):
        db = sqlite3.connect("Librarydb.db")
        data=db.execute("select * from Books")
        for row in data:
            if row[1]==self.t1.get() and row[2]==self.t2.get():
                if row[3]>0:
                    db.execute("update Books set name=?, subject=?, quantity=? where bid=?",(row[1],row[2],row[3]-1,row[0]))
                    data1=db.execute("select * from Members")
                    for row1 in data1:
                        if row1[0]==int(self.t3.get()):
                            db.execute("update Members set name=?, mobile=?,trans=? where uid=?",(row1[1],row1[2],row1[3]+1,row1[0]))
                    db.execute("Create table if not exists Transections(tid int primary key,name text,subject text,uid int)")
                    tid=0
                    data2=db.execute("select * from Transections")
                    for row2 in data2:
                        tid=row2[0]
                    db.execute("insert into Transections values(?,?,?,?)",(tid+1,self.t1.get(),self.t2.get(),int(self.t3.get())))
                    messagebox.showinfo("Book-Issue","Suceesful!")
                else:
                    messagebox.showinfo("Book-Issue","Currently Unavailable")
            break
        else:
            messagebox.showinfo("Book-Issue","Book does not exsist")
        db.commit()
        db.close()
class AddBook:
    def __init__(self):
        self.r2=Tk()
        self.r2.geometry("400x400")
        self.r2.title("Add Books")
        self.l=Label(self.r2,text="Add Books",font=("bold",25))
        self.l1=Label(self.r2,text="Name:",font=("normal",20))
        self.l2=Label(self.r2,text="Subject:",font=("normal",20))
        self.l3=Label(self.r2,text="Quantity:",font=("normal",20))
        self.b1=Button(self.r2,text="Add Book",font=("normal",20),command=self.do)
        self.t1=Entry(self.r2,width=15,font=("normal",20))
        self.t2=Entry(self.r2,width=15,font=("normal",20))
        self.t3=Entry(self.r2,width=15,font=("normal",20))
        self.l.place(x=120,y=10)
        self.l1.place(x=10,y=80)
        self.l2.place(x=10,y=140)
        self.l3.place(x=10,y=200)
        self.t1.place(x=130,y=80)
        self.t2.place(x=130,y=140)
        self.t3.place(x=130,y=200)
        self.b1.place(x=130,y=300)
    def do(self):
        db = sqlite3.connect("Librarydb.db")
        db.execute("Create table if not exists Books(bid int primary key,name text,subject text,quantity int)")
        data=db.execute("select * from Books")
        bid1=0
        for row in data:
            bid1=row[0]
            if row[1]==self.t1.get() and row[2]==self.t2.get():
                qty=int(self.t3.get())+row[3]
                db.execute("update Books set name=?, subject=?, quantity=? where bid=?",(self.t1.get(),self.t2.get(),qty,bid1))
                db.commit()
                db.close()
                break
        else:
            db.execute("insert into Books values(?,?,?,?)",(bid1+1,self.t1.get(),self.t2.get(),int(self.t3.get())))
            db.commit()
            db.close()
        messagebox.showinfo("Message","Book saved sucessfully")
class AddMember:
    def __init__(self):
        self.r2=Tk()
        self.r2.geometry("400x400")
        self.r2.title("Add Members")
        self.l=Label(self.r2,text="Add Members",font=("bold",25))
        self.l1=Label(self.r2,text="Name:",font=("normal",20))
        self.l2=Label(self.r2,text="Mobile:",font=("normal",20))
        self.b1=Button(self.r2,text="Add Member",font=("normal",20),command=self.do)
        self.t1=Entry(self.r2,width=15,font=("normal",20))
        self.t2=Entry(self.r2,width=15,font=("normal",20))
        self.l.place(x=120,y=10)
        self.l1.place(x=10,y=80)
        self.l2.place(x=10,y=140)
        self.t1.place(x=130,y=80)
        self.t2.place(x=130,y=140)
        self.b1.place(x=110,y=300)
    def do(self):
        db = sqlite3.connect("Librarydb.db")
        db.execute("Create table if not exists Members(uid int primary key,name text,mobile text,trans int)")
        data=db.execute("select * from Members")
        bid1=0
        for row in data:
            bid1=row[0]
        db.execute("insert into Members values(?,?,?,?)",(bid1+1,self.t1.get(),self.t2.get(),0))
        db.commit()
        db.close()
        messagebox.showinfo("Message","Member added sucessfully")
class SubjectWises:
    def __init__(self):
        self.r4=Tk()
        self.r4.geometry("400x400")
        self.r4.title("Subject-Wise")
        self.l=Label(self.r4,text="Subject Wise",font=("bold",25))
        self.l1=Label(self.r4,text="Subject:",font=("normal",20))
        self.t1=Entry(self.r4,width=15,font=("normal",20))
        self.b1=Button(self.r4,text="Search",font=("normal",20),command=self.Search)
        self.lb=Listbox(self.r4,width=58,height=12)
        self.l.place(x=120,y=10)
        self.l1.place(x=10,y=80)
        self.t1.place(x=130,y=80)
        self.b1.place(x=130,y=340)
        self.lb.place(x=20,y=140)
    def Search(self):
        self.lb.delete(0,"end")
        db = sqlite3.connect("Librarydb.db")
        data=db.execute("select * from Books")
        for row in data:
            if row[2]==self.t1.get():
                self.lb.insert(END,row)
        db.close()
class Defaulter:
    def __init__(self):
        self.r3=Tk()
        self.r3.geometry("400x400")
        self.r3.title("All Members")
        self.l=Label(self.r3,text="All Members",font=("bold",25))
        self.lb=Listbox(self.r3,width=58,height=18)
        self.l.place(x=120,y=10)
        self.lb.place(x=20,y=70)
        db = sqlite3.connect("Librarydb.db")
        data=db.execute("select * from Members")
        for row in data:
            if row[3]>0:
                self.lb.insert(END,row)
        db.close()
class Books:
    def __init__(self):
        self.r1=Tk()
        self.r1.geometry("400x400")
        self.r1.title("Books")
        self.l=Label(self.r1,text="Books",font=("bold",25))
        self.b1=Button(self.r1,text="Add Book",font=("normal",20),width=12,command=self.AddBooks)
        self.b2=Button(self.r1,text="All Books",font=("normal",20),width=12,command=self.AllBooks)
        self.b3=Button(self.r1,text="Subject-Wise",font=("normal",20),width=12,command=self.SubjectWise)
        self.b4=Button(self.r1,text="Issue Book",font=("normal",20),width=12,command=self.IssueBook)
        self.l.place(x=150,y=10)
        self.b1.place(x=100,y=90)
        self.b2.place(x=100,y=170)
        self.b3.place(x=100,y=240)
        self.b4.place(x=100,y=310)
    def AddBooks(self):
        a1=AddBook()
    def AllBooks(self):
        a2=AllBook()
    def SubjectWise(self):
        a3=SubjectWises()
    def IssueBook(self):
        a4=IssueBooks()
class Transection:
   def __init__(self):
        self.r3=Tk()
        self.r3.geometry("400x400")
        self.r3.title("Transactions")
        self.l=Label(self.r3,text="Transactions",font=("bold",25))
        self.lb=Listbox(self.r3,width=58,height=18)
        self.l.place(x=120,y=10)
        self.lb.place(x=20,y=70)
        db = sqlite3.connect("Librarydb.db")
        data=db.execute("select * from Transections")
        for row in data:
            self.lb.insert(END,row)
        db.close() 
def Book():
    b=Books()
def User():
    u=Users()
def Trans():
    t=Transection()
root=Tk()
root.geometry("600x600")
root.title("Library Mangement System")
l=Label(root,text="Welcome to Library Management!!!",font=("bold",25))
b1=Button(root,text="Books",font=("normal",20),width=12,command=Book)
b2=Button(root,text="Members",font=("normal",20),width=12,command=User)
b3=Button(root,text="Transactions",font=("normal",20),width=12,command=Trans)
l.place(x=40,y=30)
b1.place(x=180,y=200)
b2.place(x=180,y=300)
b3.place(x=180,y=400)
root.mainloop()

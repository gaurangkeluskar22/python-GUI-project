from tkinter import *
#import pymysql
import re
class gui:
    def __init__(self, root):
        root.title("G-Apps co.in")
        root.configure(background="#FBD28B")
        self.allApps = Label(root, text="G-Apps", font="times 16 bold", bg="#F0DF87")
        self.allApps.pack()

        # controls start
        self.factorailbutton = Button(root, width="10", height="5", bg="#3498DB", text="Factorial",font="times 10 bold", command=self.factorialbutton)
        self.factorailbutton.pack(side=LEFT, padx=13, pady=13)
        self.misbutton = Button(root, width="10", height="5", bg="#3498DB", text="Mis", font="times 10 bold",command=self.mis)
        self.misbutton.pack(side=LEFT, padx=13, pady=13)
        self.validateemailbutton = Button(root, width="10", height="5", bg="#3498DB", text="Validate gmail", font="times 10 bold",command=self.gmail)
        self.validateemailbutton.pack(side=LEFT, padx=13, pady=13)
        self.countbutton = Button(root, width="10", height="5", bg="#3498DB", text="Word Count", font="times 10 bold",command=self.count)
        self.countbutton.pack(side=LEFT, padx=13, pady=13)

    # -----------------------------------------------------factorial code start -------------------------------------------------------------
    def factorialbutton(self):
        root = Tk()
        root.title("Allapps Factorial")
        root.propagate(0)
        root.configure(background="#FBD28B", width=400, height=200)
        self.enternumber = Label(root, text="Enter Number:")
        self.enternumber.pack(side=LEFT, pady=7, padx=7)
        self.enter = Entry(root)
        self.enter.pack(side=LEFT, pady=7, padx=7)
        self.factorialbtn = Button(root, text="submit", bg="#2475B0", command=self.ans)
        self.factorialbtn.place(x=10, y=120)
        self.ansLable = Label(root, text="")
        self.ansLable.place(x=70, y=120)
        root.mainloop()

    def ans(self):
        vax = self.enter.get()
        n = int(vax)
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        fact = str(fact)
        self.ansLable.configure(text="The factorial of " + vax + " is: " + fact)

    # --------------------------------------------------factorial code ends ---------------------------------------------------------- -------

    # --------------------------------------------------mis code start -----------------------------------------------------------------------
    def mis(self):
        root = Tk()
        root.title("Allapps Mis")
        root.propagate(0)
        root.configure(background="#FBD28B",width=400,height=300)
        self.namelable = Label(root, text="name:")
        self.nameentry = Entry(root)
        self.passwordlable = Label(root, text="password:")
        self.passwordentry = Entry(root)
        self.emaillable = Label(root, text="email:")
        self.emailentry = Entry(root)
        self.marks = Label(root,text="marks:")
        self.markse = Entry(root)
        self.output=Label(root,text="")
        self.button = Button(root,text="submit",bg="#3498DB",command=self.btn)
        self.namelable.place(x=10, y=10)
        self.nameentry.place(x=70, y=10)
        self.passwordlable.place(x=10, y=50)
        self.passwordentry.place(x=70, y=50)
        self.emaillable.place(x=10, y=100)
        self.emailentry.place(x=70, y=100)
        self.marks.place(x=10, y=150)
        self.markse.place(x=70, y=150)
        self.button.place(x=10, y=190)
        self.output.place(x=10,y=220)
        root.mainloop()

    def btn(self):
        name1=self.nameentry.get()
        password1=self.passwordentry.get()
        email=self.emailentry.get()
        marks1=self.markse.get()
        self.output.config(text="name is: "+name1+" ; password is: "+password1+" ; email id is: "+email+" ; marks is: "+marks1)
        # Open database connection
        db = pymysql.connect("localhost", "root", "", "python")

        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # Prepare SQL query to INSERT a record into the database.
        sql = "INSERT INTO `python`( `name`, `password`, `mail`, `marks`) VALUES (%s,%s,%s,%s)"
        val = (name1,password1,email,marks1)

        cursor.execute(sql,val)
        db.commit()

        cursor.execute("SELECT * from python")
        rows=cursor.fetchall()
        for echrows in rows:
            print(echrows)

# -----------------------------------------------------mis code ends----------------------------------------------------------------------

# -----------------------------------------------------gmail code start ------------------------------------------------------------------

    def gmail(self):
        root = Tk()
        root.title("G-Apps Validate Gmail")
        root.propagate(0)
        root.configure(background="#FBD28B", width=400, height=300)
        self.lable= Label(root, text="Enter Gmail id:")
        self.btn=Button(root,text="submit",bg="#3498DB",command=self.btnvalidategmail)
        self.gmailentry = Entry(root,width=60)
        self.lable.place(x=10, y=10)
        self.gmailentry.place(x=110, y=10)
        self.btn.place(x=10,y=35)
        root.mainloop()

    def btnvalidategmail(self):
        x=self.gmailentry.get()
        out=re.findall(r'[\w]+?@[a-z]+\.[a-z]{3}',x)
        print(out)
# -----------------------------------------------------gmail code ends ------------------------------------------------------------------

#-------------------------------------------------------word count start ----------------------------------------------------------------
    def count(self):
        root = Tk()
        root.title("G-Apps Word Count")
        root.propagate(0)
        root.configure(background="#FBD28B", width=400, height=300)
        self.lable = Label(root, text="Enter text:")
        self.lableoutput = Label(root, text="")
        self.btn = Button(root, text="submit", bg="#3498DB", command=self.wordcount)
        self.wordcountentry = Entry(root,width=50)
        self.lable.place(x=10, y=10)
        self.wordcountentry.place(x=110, y=10)
        self.btn.place(x=10, y=35)
        self.lableoutput.place(x=10, y=65)

    def wordcount(self):
        count=self.wordcountentry.get()
        character=len(count)
        list=count.split()
        print(list)
        words=len(list)
        self.lableoutput.config(text="NO of words: "+str(words)+" No of Characters: "+str(character))

#-------------------------------------------------------word count end ------------------------------------------------------------------

root = Tk()
g = gui(root)
root.mainloop()

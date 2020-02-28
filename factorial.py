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

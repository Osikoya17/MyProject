from tkinter import *
import math
class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title("Scientific Calculator")
        self.Newfm = Frame(self.root)
        self.Newfm.pack() 
        self.lb = Label(self.root,text="Standard") 
        self.lb.pack()
        self.menubar()
        self.standard()
        self.root.mainloop()
        
    def menubar(self):
        self.menubar=Menu(self.root,tearoff=0)
        self.show = Menu(self.menubar,tearoff=0)


        self.show.add_command(label="Standard",command=self.standard,accelerator="")
        self.show.add_separator()
        self.show.add_command(label="Scienctific",command=self.sci,accelerator="")
        self.show.add_separator()
        self.show.add_command(label="Speed",command=self.Speed,accelerator="")
        self.show.add_separator()
        self.show.add_command(label="Area",command=self.Area,accelerator="")
        self.show.add_separator()
        self.show.add_command(label="Temperature",command=self.Temperature,accelerator="")
    


        self.menubar.add_cascade(label="More...",menu=self.show,underline=1)
        self.root.config(menu=self.menubar)


    def standard(self):
        self.lb.config(text="Standard")
        self.Newfm.destroy()
        self.Newfm = Frame(self.root)
        self.Newfm.pack()
        self.fm1 = Frame(self.Newfm)
        self.fm1.pack()
        self.answer = StringVar()
        self.txt1 = Entry(self.fm1,textvariable = self.answer,width=14,font=('arial',20),state="disable",disabledbackground="White")
        self.txt1.pack(pady=5,padx=5)
        # self.answer1 = StringVar()
        # self.txt2 = Entry(self.fm1,textvariable = self.answer,width=14,font=('arial',20),state="disable",disabledbackground="White")
        # self.txt2.pack(padx=5)
        self.butfm = Frame(self.Newfm)
        self.butfm.pack()
        Button(self.butfm,text='1',width=5,height=2,command=lambda: self.getValues('1')).grid(row=0,column=0,pady=3,padx=5)
        Button(self.butfm,text='2',width=5,height=2,command=lambda: self.getValues('2')).grid(row=0,column=1,pady=3,padx=5)
        Button(self.butfm,text='3',width=5,height=2,command=lambda: self.getValues('3')).grid(row=0,column=2,pady=3,padx=5)
        Button(self.butfm,text='+',width=5,height=2,command=lambda: self.operator('+')).grid(row=0,column=3,pady=3,padx=5)
        Button(self.butfm,text='4',width=5,height=2,command=lambda: self.getValues('4')).grid(row=1,column=0,pady=3,padx=5)
        Button(self.butfm,text='5',width=5,height=2,command=lambda: self.getValues('5')).grid(row=1,column=1,pady=3,padx=5)
        Button(self.butfm,text='6',width=5,height=2,command=lambda: self.getValues('6')).grid(row=1,column=2,pady=3,padx=5)
        Button(self.butfm,text='-',width=5,height=2,command=lambda: self.operator('-')).grid(row=1,column=3,pady=3,padx=5)
        Button(self.butfm,text='7',width=5,height=2,command=lambda: self.getValues('7')).grid(row=2,column=0,pady=3,padx=5)
        Button(self.butfm,text='8',width=5,height=2,command=lambda: self.getValues('8')).grid(row=2,column=1,pady=3,padx=5)
        Button(self.butfm,text='9',width=5,height=2,command=lambda: self.getValues('9')).grid(row=2,column=2,pady=3,padx=5)
        Button(self.butfm,text='/',width=5,height=2,command=lambda: self.operator('/')).grid(row=2,column=3,pady=3,padx=5)
        Button(self.butfm,text='.',width=5,height=2,command=lambda: self.getValues('.')).grid(row=3,column=0,pady=3,padx=5)
        Button(self.butfm,text='0',width=5,height=2,command=lambda: self.getValues('0')).grid(row=3,column=1,pady=3,padx=5)
        Button(self.butfm,text='*',width=5,height=2,command=lambda: self.operator('*')).grid(row=3,column=2,pady=3,padx=5)
        Button(self.butfm,text='=',width=5,height=2,command=lambda: self.calculate()).grid(row=3,column=3,pady=3,padx=5)
        Button(self.butfm,text='CE',width=5,height=2,command=lambda: self.clear()).grid(row=4,column=1,pady=3,padx=5)


    def getValues(self,values):
        if self.txt1.get() !=" ":
            if self.txt1.get()=="0":
                self.answer.set(values)
            else:
                self.answer.set(self.txt1.get()+values)    
    

    def operator(self,val):
        self.fval=float(self.txt1.get())
        self.operate = val
        self.answer.set(0)


    def calculate(self):
        self.sval = float(self.txt1.get())
        if self.operate == "+":
            self.answer.set(self.fval + self.sval)
        elif self.operate == "-":
            self.answer.set(self.fval - self.sval)
        elif self.operate == "/":
            self.answer.set(self.fval / self.sval)  
        elif self.operate == "*":
            self.answer.set(self.fval * self.sval)                      
    def clear(self):
        self.answer.set(0)


    def sci(self):
        self.lb.config(text="Scienctific")
        self.Newfm.destroy()
        self.Newfm = Frame(self.root)
        self.Newfm.pack()
        self.answer = IntVar()
        self.txt1 = Entry(self.Newfm,textvariable=self.answer,width=20,font=('arial',15),state="disable",disabledbackground="White",border=0)
        self.txt1.pack(padx=5)
        self.fm2 = Frame(self.Newfm)
        self.fm2.pack()
        self.answer1 = StringVar()
        self.txt2 = Entry(self.fm2,textvariable=self.answer1,width=20,font=('arial',15),state="disable",disabledbackground="White",border=0)
        self.txt2.pack(pady=0,padx=5)
        self.butfm = Frame(self.Newfm)
        self.butfm.pack()
        Button(self.butfm,text='DEG',width=5,height=2,command=lambda: self.getValue('1')).grid(row=0,column=0,pady=3,padx=5)
        Button(self.butfm,text='HYP',width=5,height=2,command=lambda: self.getValue('2')).grid(row=0,column=1,pady=3,padx=5)
        Button(self.butfm,text='F-E',width=5,height=2,command=lambda: self.getValue('3')).grid(row=0,column=2,pady=3,padx=5)
        Button(self.butfm,text='MC',width=5,height=2,command=lambda: self.operato('+')).grid(row=1,column=0,pady=3,padx=5)
        Button(self.butfm,text='MR',width=5,height=2,command=lambda: self.getValue('4')).grid(row=1,column=1,pady=3,padx=5)
        Button(self.butfm,text='M+',width=5,height=2,command=lambda: self.getValue('5')).grid(row=1,column=2,pady=3,padx=5)
        Button(self.butfm,text='M-',width=5,height=2,command=lambda: self.getValue('6')).grid(row=1,column=3,pady=3,padx=5)
        Button(self.butfm,text='MS',width=5,height=2,command=lambda: self.operato('-')).grid(row=1,column=4,pady=3,padx=5)
        Button(self.butfm,text='x²',width=5,height=2,command=lambda: self.calcul('x²')).grid(row=2,column=0,pady=3,padx=5)
        Button(self.butfm,text='x',width=5,height=2,command=lambda: self.getValue('8')).grid(row=2,column=1,pady=3,padx=5)
        Button(self.butfm,text='sin',width=5,height=2,command=lambda: self.calcul('sin')).grid(row=2,column=2,pady=3,padx=5)
        Button(self.butfm,text='cos',width=5,height=2,command=lambda: self.calcul('cos')).grid(row=2,column=3,pady=3,padx=5)
        Button(self.butfm,text='tan',width=5,height=2,command=lambda: self.calcul('tan')).grid(row=2,column=4,pady=3,padx=5)
        Button(self.butfm,text='√',width=5,height=2,command=lambda: self.calcul('√')).grid(row=3,column=0,pady=3,padx=5)
        Button(self.butfm,text='10',width=5,height=2,command=lambda: self.calcul('10')).grid(row=3,column=1,pady=3,padx=5)
        Button(self.butfm,text='log',width=5,height=2,command=lambda: self.calcul('log')).grid(row=3,column=2,pady=3,padx=5)
        Button(self.butfm,text='Exp',width=5,height=2,command=lambda: self.calcul('')).grid(row=3,column=3,pady=3,padx=5)
        Button(self.butfm,text='Mod',width=5,height=2,command=lambda: self.operato('*')).grid(row=3,column=4,pady=3,padx=5)
        Button(self.butfm,text='↑',width=5,height=2,command=lambda: self.operato('*')).grid(row=4,column=0,pady=3,padx=5)
        Button(self.butfm,text='CE',width=5,height=2,command=lambda: self.clea()).grid(row=4,column=1,pady=3,padx=5)
        Button(self.butfm,text='C',width=5,height=2,command=lambda: self.clea()).grid(row=4,column=2,pady=3,padx=5)
        Button(self.butfm,text='x)',width=5,height=2,command=lambda: self.operato('*')).grid(row=4,column=3,pady=3,padx=5)
        Button(self.butfm,text='÷',width=5,height=2,command=lambda: self.operato('/')).grid(row=4,column=4,pady=3,padx=5)
        Button(self.butfm,text='π',width=5,height=2,command=lambda: self.calcul('π')).grid(row=5,column=0,pady=3,padx=5)
        Button(self.butfm,text='7',width=5,height=2,command=lambda: self.getValue('7')).grid(row=5,column=1,pady=3,padx=5)
        Button(self.butfm,text='8',width=5,height=2,command=lambda: self.getValue('8')).grid(row=5,column=2,pady=3,padx=5)
        Button(self.butfm,text='9',width=5,height=2,command=lambda: self.getValue('9')).grid(row=5,column=3,pady=3,padx=5)
        Button(self.butfm,text='×',width=5,height=2,command=lambda: self.getValue('*')).grid(row=5,column=4,pady=3,padx=5)
        Button(self.butfm,text='n!',width=5,height=2,command=lambda: self.operato('*')).grid(row=6,column=0,pady=3,padx=5) 
        Button(self.butfm,text='4',width=5,height=2,command=lambda: self.getValue('4')).grid(row=6,column=1,pady=3,padx=5)
        Button(self.butfm,text='5',width=5,height=2,command=lambda: self.getValue('5')).grid(row=6,column=2,pady=3,padx=5) 
        Button(self.butfm,text='6',width=5,height=2,command=lambda: self.getValue('6')).grid(row=6,column=3,pady=3,padx=5)
        Button(self.butfm,text='-',width=5,height=2,command=lambda: self.operato('-')).grid(row=6,column=4,pady=3,padx=5)
        Button(self.butfm,text='±',width=5,height=2,command=lambda: self.calcul('±')).grid(row=7,column=0,pady=3,padx=5) 
        Button(self.butfm,text='1',width=5,height=2,command=lambda: self.getValue('1')).grid(row=7,column=1,pady=3,padx=5)
        Button(self.butfm,text='2',width=5,height=2,command=lambda: self.getValue('2')).grid(row=7,column=2,pady=3,padx=5) 
        Button(self.butfm,text='3',width=5,height=2,command=lambda: self.getValue('3')).grid(row=7,column=3,pady=3,padx=5)
        Button(self.butfm,text='+',width=5,height=2,command=lambda: self.operato('+')).grid(row=7,column=4,pady=3,padx=5)
        Button(self.butfm,text='(',width=5,height=2,command=lambda: self.getValue('(')).grid(row=8,column=0,pady=3,padx=5) 
        Button(self.butfm,text=')',width=5,height=2,command=lambda: self.getValue(')')).grid(row=8,column=1,pady=3,padx=5)
        Button(self.butfm,text='0',width=5,height=2,command=lambda: self.getValue('0')).grid(row=8,column=2,pady=3,padx=5) 
        Button(self.butfm,text='.',width=5,height=2,command=lambda: self.getValue('.')).grid(row=8,column=3,pady=3,padx=5)
        Button(self.butfm,text='=',width=5,height=2,command=lambda: self.calcul("=")).grid(row=8,column=4,pady=3,padx=5) 


    def getValue(self,values):
        if self.txt1.get() !=" ":
            if self.txt1.get()=="0":
               self.answer.set(values)
            else:
                self.answer.set(self.txt1.get()+values)

    def operato(self,val):
        self.operate = val
        self.answer.set(self.txt1.get()+" " + val+" ")
            
    def clea(self):
        self.answer.set(0)
        self.answer1.set(" ")

    def calcul(self,an):
        if an == "sin":
            self.ans = (math.sin(float(self.txt1.get())*math.pi/180))
            self.answer.set(f"sin({self.txt1.get()})")
            self.answer1.set(self.ans)
        elif an == "tan":
            self.ans = (math.tan(float(self.txt1.get())*math.pi/180))
            self.answer.set(f"tan({self.txt1.get()})")
            self.answer1.set(self.ans)
        elif an == "cos":
            self.ans = (math.cos(float(self.txt1.get())*math.pi/180))
            self.answer.set(f"cos({self.txt1.get()})")
            self.answer1.set(self.ans)            
        elif an == "=":
            self.result = eval(self.txt1.get())
            self.answer1.set(self.result)
        elif an == "log":
            self.ans = math.log10(int(self.txt1.get()))
            self.answer.set(f"log({self.txt1.get()})")
            self.answer1.set(self.ans) 
        elif an == "√":
            self.ans = math.sqrt(int(self.txt1.get()))
            self.answer.set(f"√{self.txt1.get()}")
            self.answer1.set(self.ans) 
        elif an == "π":
            self.answer.set(3.1415926535897932384626433832795)
        elif an == "x²":
            self.ans = math.pow(float(self.txt1.get()),2)
            self.answer.set(f"{self.txt1.get()}²")
            self.answer1.set(self.ans) 


    def Speed(self):
        self.lb.config(text="Speed")
        self.Newfm.destroy()
        self.Newfm = Frame(self.root)
        self.Newfm.pack()
        self.fm1 = Frame(self.Newfm)
        self.fm1.pack()
        self.answ = StringVar()
        self.text1=Entry(self.fm1,textvariable=self.answ,state="disable",disabledbackground="White")
        self.text1.pack(side="left",pady=10)
        self.lb1 = Label(self.fm1,text='km/hrs')
        self.lb1.pack(side="left")
        self.lb2 = Label(self.fm1,text='=')
        self.lb2.pack(side="left",padx=10)
        self.answ1=IntVar()
        self.text2=Entry(self.fm1,textvariable=self.answ1,border=0,state="disable")
        self.text2.pack(side="left",padx=7,pady=10)
        self.lb3 = Label(self.fm1,text="miles/hrs")
        self.lb3.pack(pady=10)
        self.fm0 =Frame(self.Newfm)
        self.fm0.pack()
        Button(self.fm0,text="CE",width=10,command=lambda: self.clear()).pack()
        self.fm2 = Frame(self.Newfm)
        self.fm2.pack()
        Button(self.fm2,text="7",width=10,command=lambda: self.number('7')).grid(row=0,column=0,padx=5,pady=5)
        Button(self.fm2,text="8",width=10,command=lambda: self.number('8')).grid(row=0,column=1,padx=5,pady=5)
        Button(self.fm2,text="9",width=10,command=lambda: self.number('9')).grid(row=0,column=2,padx=5,pady=5)
        Button(self.fm2,text="4",width=10,command=lambda: self.number('4')).grid(row=1,column=0,padx=5,pady=5)
        Button(self.fm2,text="5",width=10,command=lambda: self.number('5')).grid(row=1,column=1,padx=5,pady=5)
        Button(self.fm2,text="6",width=10,command=lambda: self.number('6')).grid(row=1,column=2,padx=5,pady=5)
        Button(self.fm2,text="1",width=10,command=lambda: self.number('1')).grid(row=2,column=0,padx=5,pady=5)
        Button(self.fm2,text="2",width=10,command=lambda: self.number('2')).grid(row=2,column=1,padx=5,pady=5)
        Button(self.fm2,text="3",width=10,command=lambda: self.number('3')).grid(row=2,column=2,padx=5,pady=5)
        Button(self.fm2,text=".",width=10,command=lambda: self.number('.')).grid(row=3,column=0,padx=5,pady=5)
        Button(self.fm2,text="0",width=10,command=lambda: self.number('0')).grid(row=3,column=1,padx=5,pady=5)    

    def number(self,num):
        self.res=(float(self.text1.get()+num)*0.621)
        self.answ.set(self.text1.get()+num)
        self.answ1.set(self.res)
    
    def clear(self):
        self.answ.set(" ")
        self.answ1.set(0)


    def Temperature(self):
        self.lb.config(text="Temperature")
        self.Newfm.destroy()
        self.Newfm = Frame(self.root)
        self.Newfm.pack()
        self.fm1 = Frame(self.Newfm)
        self.fm1.pack()
        self.answ = StringVar()
        self.text1=Entry(self.fm1,textvariable=self.answ,state="disable",disabledbackground="White")
        self.text1.pack(side="left",pady=10)
        self.lb1 = Label(self.fm1,text='Celius')
        self.lb1.pack(side="left")
        self.lb2 = Label(self.fm1,text='=')
        self.lb2.pack(side="left",padx=10)
        self.answ1=IntVar()
        self.text2=Entry(self.fm1,textvariable=self.answ1,border=0,state="disable")
        self.text2.pack(side="left",padx=7,pady=10)
        self.lb3 = Label(self.fm1,text="Kevin")
        self.lb3.pack(pady=10)
        self.fm0 =Frame(self.Newfm)
        self.fm0.pack()
        Button(self.fm0,text="CE",width=10,command=lambda: self.clear()).pack()
        self.fm2 = Frame(self.Newfm)
        self.fm2.pack()
        Button(self.fm2,text="7",width=10,command=lambda: self.numb('7')).grid(row=0,column=0,padx=5,pady=5)
        Button(self.fm2,text="8",width=10,command=lambda: self.numb('8')).grid(row=0,column=1,padx=5,pady=5)
        Button(self.fm2,text="9",width=10,command=lambda: self.numb('9')).grid(row=0,column=2,padx=5,pady=5)
        Button(self.fm2,text="4",width=10,command=lambda: self.numb('4')).grid(row=1,column=0,padx=5,pady=5)
        Button(self.fm2,text="5",width=10,command=lambda: self.numb('5')).grid(row=1,column=1,padx=5,pady=5)
        Button(self.fm2,text="6",width=10,command=lambda: self.numb('6')).grid(row=1,column=2,padx=5,pady=5)
        Button(self.fm2,text="1",width=10,command=lambda: self.numb('1')).grid(row=2,column=0,padx=5,pady=5)
        Button(self.fm2,text="2",width=10,command=lambda: self.numb('2')).grid(row=2,column=1,padx=5,pady=5)
        Button(self.fm2,text="3",width=10,command=lambda: self.numb('3')).grid(row=2,column=2,padx=5,pady=5)
        Button(self.fm2,text=".",width=10,command=lambda: self.numb('.')).grid(row=3,column=0,padx=5,pady=5)
        Button(self.fm2,text="0",width=10,command=lambda: self.numb('0')).grid(row=3,column=1,padx=5,pady=5)


    def numb(self,num):
        self.res=(float(self.text1.get()+num)+274.14)
        self.answ.set(self.text1.get()+num)
        self.answ1.set(self.res)

    def Area(self):
        self.lb.config(text="Area")
        self.Newfm.destroy()
        self.Newfm = Frame(self.root)
        self.Newfm.pack()
        self.fm1 = Frame(self.Newfm)
        self.fm1.pack()
        self.answ = StringVar()
        self.text1=Entry(self.fm1,textvariable=self.answ,state="disable",disabledbackground="White")
        self.text1.pack(side="left",pady=10)
        self.lb1 = Label(self.fm1,text='Square Meters')
        self.lb1.pack(side="left")
        self.lb2 = Label(self.fm1,text='=')
        self.lb2.pack(side="left",padx=10)
        self.answ1=IntVar()
        self.text2=Entry(self.fm1,textvariable=self.answ1,border=0,state="disable")
        self.text2.pack(side="left",padx=7,pady=10)
        self.lb3 = Label(self.fm1,text="Square Feet")
        self.lb3.pack(pady=10)
        self.fm0 =Frame(self.Newfm)
        self.fm0.pack()
        Button(self.fm0,text="CE",width=10,command=lambda: self.clear()).pack()
        self.fm2 = Frame(self.Newfm)
        self.fm2.pack()
        Button(self.fm2,text="7",width=10,command=lambda: self.nu('7')).grid(row=0,column=0,padx=5,pady=5)
        Button(self.fm2,text="8",width=10,command=lambda: self.nu('8')).grid(row=0,column=1,padx=5,pady=5)
        Button(self.fm2,text="9",width=10,command=lambda: self.nu('9')).grid(row=0,column=2,padx=5,pady=5)
        Button(self.fm2,text="4",width=10,command=lambda: self.nu('4')).grid(row=1,column=0,padx=5,pady=5)
        Button(self.fm2,text="5",width=10,command=lambda: self.nu('5')).grid(row=1,column=1,padx=5,pady=5)
        Button(self.fm2,text="6",width=10,command=lambda: self.nu('6')).grid(row=1,column=2,padx=5,pady=5)
        Button(self.fm2,text="1",width=10,command=lambda: self.nu('1')).grid(row=2,column=0,padx=5,pady=5)
        Button(self.fm2,text="2",width=10,command=lambda: self.nu('2')).grid(row=2,column=1,padx=5,pady=5)
        Button(self.fm2,text="3",width=10,command=lambda: self.nu('3')).grid(row=2,column=2,padx=5,pady=5)
        Button(self.fm2,text=".",width=10,command=lambda: self.nu('.')).grid(row=3,column=0,padx=5,pady=5)
        Button(self.fm2,text="0",width=10,command=lambda: self.nu('0')).grid(row=3,column=1,padx=5,pady=5)


    def nu(self,num):
        self.res=(float(self.text1.get()+num)*10.76391)
        self.answ.set(self.text1.get()+num)
        self.answ1.set(self.res)
ola = Calculator()
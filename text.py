# import PIL
# from PIL import Image ,ImageTk
from tkinter.messagebox import *
from tkinter.filedialog import *
import tkinter.ttk as ttk
from tkinter import *
from tkinter import colorchooser
class Txt:
    def __init__(self):
        self.root = Tk()
        self.root.title("Notepad")
        self.root.iconbitmap("icons8_Book.ico")
        self.fm1 = Frame(self.root,width=580,height=580)
        self.fm1.pack(fill=BOTH,expand=YES)
        self.yscrol = Scrollbar(self.fm1,orient="vertical")
        self.xscrol = Scrollbar(self.root,orient="horizontal")
        self.comment = Text(self.fm1, width=120, height=30, wrap=NONE,xscrollcommand= self.xscrol.set,yscrollcommand= self.yscrol.set)
        self.comment.pack(side="left",expand=YES,fill=BOTH)
        self.yscrol.configure(command=self.comment.yview)
        self.xscrol.configure(command=self.comment.xview)
        self.yscrol.pack(side="left",anchor= E,fill=BOTH)
        self.xscrol.pack(side="top",anchor= W,fill=BOTH)
        self.root.bind_all("<Control-n>",self.newPage)
        self.comment.bind_all("<Control-Key-N>",self.newPage)
        self.root.bind_all("<Control-o>",self.openFile)
        self.comment.bind_all("<Control-Key-O>",self.openFile)
        self.itemforlistbox = [1,2,3,4,56,7,]
        # self.chocho = StringVar()
        # Radiobutton(self.root,Variable=cho,text="A",value="a",command=Onclick,tristatevalue=0)
        # Radiobutton(self.root,Variable=cho,text="B",value="b",command=Onclick,tristatevalue=0)
        # Radiobutton(self.root,Variable=cho,text="C",value="c",command=Onclick,tristatevalue=0)

        # self.root = tk.tk()
        # self.all_comboboxes = []
        # self.cb = ttk.Combobox(self.root,)
        # self.set("1")
        # self.cb.pack()
        # self.cb.bind('<<ComboSelected>>',onselect)
        self.menubar()
        self.in_path = ""
        self.root.mainloop()
    def menubar(self):
        self.menubar = Menu(self.root,tearoff=0)
        self.fileMenu =Menu(self.menubar,tearoff=0)
        self.EditMenu = Menu(self.menubar,tearoff=0)
        self.FormatMenu = Menu(self.menubar,tearoff=0)
        self.ViewMenu = Menu(self.menubar,tearoff=0)
        self.HelpMenu = Menu(self.menubar,tearoff=0)
        # self.newPlogo = Image.open("icons8_Book_32.png")
        # self.image = ImageTk.PhotoImage(self.newPlogo)
        self.fileMenu.add_command(label='New',command=self.newPage,accelerator="Ctrl+N")
        self.fileMenu.add_command(label='New Window',command=self.NewWindow,accelerator="Ctrl+Shift+N")
        self.fileMenu.add_command(label='Open',command=self.openFile,accelerator="Ctrl+O")
        self.fileMenu.add_command(label='Save',command=self.saveFile,accelerator="Ctrl+S")
        self.fileMenu.add_command(label='Save As',command=self.saveAsFile,accelerator="Ctrl+Shift+S")
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label='Page Setup...',command=self.pageSet)
        self.fileMenu.add_command(label='Print',command=self.openfile,accelerator="Ctrl+P")
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label='Exit',command=self.openfile)


        self.EditMenu.add_command(label='Undo',command=self.Undo,accelerator="Ctrl+Z")
        self.EditMenu.add_separator()
        self.EditMenu.add_command(label='Redo',command=self.redo,accelerator="Ctrl+X")
        self.EditMenu.add_command(label='Cut',command=self.Cutfile,accelerator="Ctrl+X")
        self.EditMenu.add_command(label='Copy',command=self.copyfile,accelerator="Ctrl+C")
        self.EditMenu.add_command(label='Paste',command=self.Pastefile,accelerator="Ctrl+V")
        self.EditMenu.add_command(label='Delete',command=self.deletefile,accelerator="Del")
        self.EditMenu.add_separator()
        self.EditMenu.add_command(label='Find&replace',command=self.Find,accelerator="Ctrl+F")
        self.EditMenu.add_command(label='Go To...',command=self.goto,accelerator="Ctrl+G")
        self.EditMenu.add_separator()
        self.EditMenu.add_command(label='Select All',command=self.selectall,accelerator="Ctrl+A")
        self.EditMenu.add_command(label='Time/Date',command=self.openfile,accelerator="F5")


        self.FormatMenu.add_checkbutton(label="WordWrap",command=self.openfile)
        self.FormatMenu.add_command(label='Font...',command=self.font)
        self.FormatMenu.add_command(label='Color',command=self.getColor)

        
        self.opt = Menu(self.ViewMenu,tearoff=0)
        self.opt.add_command(label="Zoom in",accelerator="Ctl+Plus")
        self.opt.add_command(label="Zoom out",accelerator="Ctl+Minus")
        self.opt.add_command(label="Restore Default Zoom",accelerator="Ctrl+0")
        self.ViewMenu.add_cascade(label="Zoom",menu=self.opt,underline=1)
        self.ViewMenu.add_checkbutton(label="Status Bar",command=self.openfile)
        
        
        self.HelpMenu.add_command(label='View Help',command=self.openfile)
        self.HelpMenu.add_command(label='Send Feedback',command=self.openfile)
        self.HelpMenu.add_separator()
        self.HelpMenu.add_command(label='About Notepad',command=self.openfile)

        # self.opt = Menu(self.fileMenu,tearoff=0)
        # self.opt.add_command(label="option 1")
        # self.opt.add_command(label="option 2")
        # self.opt.add_command(label="option 3")
        # self.opt.add_command(label="option 4")
        self.menubar.add_cascade(label="File",menu=self.fileMenu,underline=1)
        self.menubar.add_cascade(label="Edit",menu=self.EditMenu,underline=1)
        self.menubar.add_cascade(label="Format",menu=self.FormatMenu,underline=1)
        self.menubar.add_cascade(label="View",menu=self.ViewMenu,underline=1)
        self.menubar.add_cascade(label="Help",menu=self.HelpMenu,underline=1)
        self.root.config(menu=self.menubar)



    def newPage(self,event=NONE):
        msg=askyesnocancel("Warning","Do You Want Save This File")
        if msg ==  True:
            self.saveFile()
            self.comment.delete(1.0,END)
        elif msg ==False:
            self.comment.delete(1.0,END)

    def openFile(self,event=NONE):
        self.in_path = askopenfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files", "*.*")])
        with open(self.in_path,"r") as self.infile:
            self.comment.delete(1.0,END)
            myfile = self.infile.read()
            self.comment.insert(1.0,myfile,END)
            self.root.title(self.in_path.split("/")[6] + " - Notepad")

    def saveAsFile(self):
        self.in_path = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files", "*.*")])
        with open(self.in_path,"w") as self.infile:
            self.infile.write(self.comment.get(1.0,END))

            self.root.title(self.in_path.split("/")[6] + " - Notepad")

    def saveFile(self):
        if self.in_path == "":
            self.saveAsFile()
        else:    
            with open(self.in_path,"w") as self.infile:
                self.infile.write(self.comment.get(1.0,END))
                self.root.title(self.in_path.split("/")[6] + " - Notepad")


    def NewWindow(self):
        text11 = Txt()

    def Undo(self):
        self.comment.event_generate("<<Undo>>") 
        print("Undo")
            # showinfo("Message","There is nothing to undo")    

    def redo(self):
        try:
            self.comment.edit_redo()
        except:
            showinfo("Message","There is nothing to redo") 


    def copyfile(self):
        self.comment.event_generate("<<Copy>>")
    def Cutfile(self):
        self.comment.event_generate("<<Cut>>")
    def Pastefile(self):
        self.comment.event_generate("<<Paste>>") 
    def deletefile(self):
        try:
            self.comment.delete(SEL_FIRST,SEL_LAST)
        except:
            showinfo("Message","Select Portion To delete")   
    def selectall(self):
        try:
            self.comment.tag_add(SEL,1.0,END)     
            self.comment.mark_set(INSERT,1.0)
            self.comment.see(INSERT)
            return "break"
        except:
            showinfo("Message","The Page is Empty")        
    def pageSet(self):
        self.Top = Toplevel()
        self.Top.title("Page Setup")
        # self.top1 =  Frame(self.Top)
        # self.top1.pack(anchor=NW,padx=5)
        # self.top2 =  Frame(self.Top)
        # self.top2.pack(side="left",anchor=W,padx=5)
        # self.top3 = Frame(self.Top)
        # self.top3.pack(anchor=NW,pady=4)
        # self.top4= Frame(self.Top)
        # self.top4.pack(anchor=W,pady=4)
        self.lbFrm = LabelFrame(self.Top,text="Paper",width=50)
        self.lbFrm.grid(row=0, column=0,columnspan=6,padx=7,pady=5)
        self.lb2 = Label(self.lbFrm,text="Size:")
        self.lb2.grid(row=0,column=0)
        self.all_comboboxes = []
        self.cb1 = ttk.Combobox(self.lbFrm,values=[1,2,3,4],width=40)
        # self.set("1")
        self.cb1.grid(row=0,column=1,padx=5)
        self.cb1.bind('<<ComboSelected>>')
        self.lb2 = Label(self.lbFrm,text="Source:",state=DISABLED)
        self.lb2.grid(row=1,column=0)
        self.all_comboboxes = []
        self.cb2 = ttk.Combobox(self.lbFrm,state=DISABLED,values=(1,2,3,4,5),width=40)
        # self.set("1")
        self.cb2.grid(row=1,column=1,pady=5)
        self.cb2.bind('<<ComboSelected>>')
        self.lbFrm3 = LabelFrame(self.Top,text="Preview")
        self.lbFrm3.grid(row=0,column=17,padx=5,pady=5)
        Text(self.lbFrm3,height=5,width=20).grid(row=1,column=1)
        # Radiobutton(self.lbFrm1,text="Landscape",value="b",tristatevalue=0).grid(row=1,column=0)
        self.lbFrm1 = LabelFrame(self.Top,text="Orientation")
        self.lbFrm1.grid(row=1,column=0,padx=6)
        Radiobutton(self.lbFrm1,text="Potrait....  ",value="a",tristatevalue=0).grid(row=0,column=0)
        Radiobutton(self.lbFrm1,text="Landscape",value="b",tristatevalue=0).grid(row=1,column=0)
        self.lbFrm2 = LabelFrame(self.Top,text="Margin(inches)")
        self.lbFrm2.grid(row=1,column=1)
        self.lb3=Label(self.lbFrm2,text="Left:")
        self.lb3.grid(row=0,column=0,pady=5)
        self.ent1 = Entry(self.lbFrm2,width=6)
        
        self.ent1.grid(row=0,column=1,padx=5,pady=5)
        self.lb4=Label(self.lbFrm2,text="Right:")
        self.lb4.grid(row=0,column=3,pady=5)
        self.ent2 = Entry(self.lbFrm2,width=6)
        self.ent2.grid(row=0,column=4,padx=5,pady=5)
        self.lb5=Label(self.lbFrm2,text="Top:")
        self.lb5.grid(row=1,column=0,pady=5)
        self.ent3 = Entry(self.lbFrm2,width=6)
        self.ent3.grid(row=1,column=1,padx=5,pady=5)
        self.lb6=Label(self.lbFrm2,text="Bottom:")
        self.lb6.grid(row=1,column=3,pady=5)
        self.ent4 = Entry(self.lbFrm2,width=6)
        self.ent4.grid(row=1,column=4,columnspan=15,pady=5)
        self.lb7=Label(self.Top,text="Header: ")
        self.lb7.grid(row=2,column=0,pady=5)
        self.ent5 = Entry(self.Top,width=35)
        self.ent5.grid(row=2,column=1,pady=5)
        self.lb8 =Label(self.Top,text="Footer: ")
        self.lb8.grid(row=3,column=0,pady=10)
        self.ent6 = Entry(self.Top,width=35)
        self.ent6.grid(row=3,column=1,pady=10)
        

    
    def Find(self):
        self.to = Toplevel()
        self.scrfm= Frame(self.to)
        self.scrfm.pack()
        self.lb1 = Label(self.scrfm,text="Find What:")
        self.lb1.grid(row=0,column=0,pady=5,padx=5)
        self.ans = StringVar()
        self.ent = Entry(self.scrfm,textvariable=self.ans,width=40)
        self.ent.grid(row=0,column=1,padx=5)
        self.lb2 = Label(self.scrfm,text="Replace with:")
        self.lb2.grid(row=1,column=0,pady=5,padx=5)
        self.ans1 = StringVar()
        self.ent2 = Entry(self.scrfm,textvariable=self.ans1,width=40)
        self.ent2.grid(row=1,column=1,padx=5)
        Button(self.scrfm,text="Find Next", width=7, command=lambda : self.findnext()).grid(row=2,column=0)
        Button(self.scrfm,text="Replace", width=7, command=lambda : self.replaced()).grid(row=2,column=1)
        Button(self.scrfm,text="Find All", width=7, command=lambda : self.findnext()).grid(row=2,column=2)


        # self.to.add
    def findnext(self):
        start = "1.0"
        end = "end"
        start = self.comment.index(start)
        end = self.comment.index(end)
        count = IntVar()
        count = count
        self.comment.mark_set("matchStart",start)
        self.comment.mark_set("matchEnd",end)
        self.comment.mark_set("searchLimit",end)
        targetfind = self.ent.get()
        if targetfind:
            while True:
                where = self.comment.search(targetfind,"matchEnd","searchLimit",count=count)
                if where == "":
                    break
                elif where:
                    pastit = where + ("+%dc" % len(targetfind))
                    self.comment.mark_set("matchStart",where)
                    self.comment.mark_set("matchEnd","%s+%sc" % where,count.get())
                    self.comment.tag_add(SEL , where,pastit)
                    self.comment.see(INSERT)
                    self.comment.focus()
        self.comment.tag_remove(SEL_FIRST , 1.0,END)



    def replaced(self):
        self.bodytxt=self.comment.get(1.0, END)
        self.finded = self.ent.get()
        self.replacew = self.ent2.get()
        self.bodytxt2 = self.bodytxt.replace(self.finded,self.replacew)
        self.comment.replace(1.0,"end",self.bodytxt2)

    def goto(self):
        def go():
            self.goline=self.enter.get()
            self.comment.mark_set(INSERT,self.goline + ".0")
            self.comment.see(INSERT)
            self.comment.focus()



     
        self.cover = Toplevel()
        self.cover.title("Go to")
        self.con = Label(self.cover,text="Enter Line Number?")
        self.con.grid(row=0,column=0)
        self.enter = Entry(self.cover,width=50)
        self.enter.grid(row=1,column=0)
        Button(self.cover,text="Go to",width=10,command= go).grid(row=2,column=0)


    def getColor(self):
        try:
            (rgb,color) = colorchooser.askcolor()
            self.comment.tag_add("color1", SEL_FIRST,SEL_LAST) 
            self.comment.tag_configure("color1", foreground=color)
        except:
            pass


    def font(self):
        self.can = Toplevel()
        self.koko = Label(self.can,text="Font:")
        self.koko.grid(row=0,column=1)
        Entry(self.can,width=10).grid(row=1,column=1,pady=5)
        itemlist=[1,2,3,4,5,6,7,12,4,5,5,67,7,88,77]
        list1= Listbox(self.can,width=15,height=10,font=("times",13),exportselection=0,yscrollcommand=self.yscrol.set)
        list1.bind('<<ListboxSelect>>')
        list1.grid(row=2,column=1)
        self.yscrol = Scrollbar(self.can,orient="vertical")
        self.yscrol.configure(command=list1.yview)
        self.lb = Label(self.can,text="Font styles:")
        self.lb.grid(row=0,column=3)
        Entry(self.can,width=10).grid(row=1,column=3,pady=5)
        itemlist1=["Regular","Bold","Italic","Bold Italic"]
        list2= Listbox(self.can,width=15,height=10,font=("times",13))
        list2.bind('<<ListboxSelect>>')
        list2.grid(row=2,column=3)
        self.lb1 = Label(self.can,text="Size:")
        self.lb1.grid(row=0,column=5)
        Entry(self.can,width=10).grid(row=1,column=5,pady=5)
        itemlist3=[11,13,14,15,16]
        list3= Listbox(self.can,width=7,height=10,font=("times",13))
        list3.bind('<<ListboxSelect>>')
        list3.grid(row=2,column=5)
        self.lFrm = LabelFrame(self.can,text="Sample",width=10)
        self.lb9 = Label(self.lFrm,text="AaBbYyZz")
        self.lb9.grid(row=1,column=1)
        self.lFrm.grid(row=3,column=5)
        self.all_comboboxes = []
        self.cb1 = ttk.Combobox(self.can,values=[1,2,3,4],width=10)
        # self.set("1")
        self.cb1.grid(row=5,column=5,padx=5)
        self.cb1.bind('<<ComboSelected>>')
        self.lb2 = Label(self.can,text="Script:",state=DISABLED)
        self.lb2.grid(row=4,column=5)

        for item in itemlist:
            list1.insert(END,item)
            print(item)
        for items in itemlist1:
            list2.insert(END,items)
            print(items)            
        for it in itemlist3:
            list3.insert(END,it)
            print(it)        
        

    def openfile():
        pass






text = Txt()        
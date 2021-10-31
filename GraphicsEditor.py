from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import *
import PIL 
from PIL import Image,ImageTk
class Graphics:
    def __init__(self):
        # self.lastx = ""0
        # self.lasty = ""
        self.cover = Tk()
        self.cover.title("Untiltled - Graphics Editor")
        self.cover.geometry("800x550")
        self.cover.iconbitmap("Paint_Palette.ico")
        self.fm1 = Frame(self.cover)
        self.fm1.pack(side=LEFT,anchor=NW)
        self.btn=Button(self.fm1,width=30,height=30,command=self.drag)
        self.btn.grid(row=0,column=0,pady=2)
        self.btn1=Button(self.fm1,width=30,height=30,command=lambda:self.draw("circle"))
        self.btn1.grid(row=1,column=0,pady=2)
        self.btn2=Button(self.fm1,width=30,height=30,command=lambda:self.draw("rec"))
        self.btn2.grid(row=2,column=0,pady=2)
        self.btn3=Button(self.fm1,width=30,height=30)
        self.btn3.grid(row=3,column=0,pady=2)
        self.btn4=Button(self.fm1,width=30,height=30,command=lambda:self.draw("line"))
        self.btn4.grid(row=4,column=0,pady=2)
        self.btn5=Button(self.fm1,width=30,height=30)
        self.btn5.grid(row=5,column=0,pady=2)
        self.fm2 = Frame(self.cover)
        self.fm2.pack(anchor=W)
        self.canva = Canvas(self.fm2,bg="#F9F9F9",width=700,height=550)
        self.canva.grid(row=0,column=0,padx=10)
        self.menubar()
        self.loadimage()
        self.coord = {"x":0,"y":0,"x2":0,"y2":0}
        self.line = []
        self.in_path = ""

        # self.loadcursor = Image.open("icons8_Cursor_16.png")
        # self.imagecursor = ImageTk.PhotoImage(self.loadcursor,master=self.cover)

        # self.btn.config(image=self.imagecursor)
        self.cover.mainloop()

    def menubar(self):
        self.menubar = Menu(self.cover,tearoff=0)
        self.fileMenu =Menu(self.menubar,tearoff=0)
        self.EditMenu = Menu(self.menubar,tearoff=0)
        self.HelpMenu = Menu(self.menubar,tearoff=0)


        self.newPlogo = Image.open("icons8_New_File_32.png")
        self.image_New = ImageTk.PhotoImage(self.newPlogo)
        self.fileMenu.add_command(label="New",accelerator="New",image=self.image_New)
        self.fileMenu.add_separator()

        self.newWlogo = Image.open("icons8_New_Window_32.png")
        self.image_NewWin = ImageTk.PhotoImage(self.newWlogo)
        self.fileMenu.add_command(label="New window",accelerator="New window",image=self.image_NewWin)
        self.fileMenu.add_separator()

        self.openlogo = Image.open("icons8_Open_32.png")
        self.image_open = ImageTk.PhotoImage(self.openlogo)
        self.fileMenu.add_command(label="Open",accelerator="Open",image=self.image_open,command=self.open)
        self.fileMenu.add_separator()

        self.savelogo = Image.open("icons8_Save_32.png")
        self.image_save = ImageTk.PhotoImage(self.savelogo)
        self.fileMenu.add_command(label="Save",accelerator="Save",image=self.image_save)
        self.fileMenu.add_separator()

        self.saveaslogo = Image.open("icons8_Save_as_32.png")
        self.image_saveas = ImageTk.PhotoImage(self.savelogo)
        self.fileMenu.add_command(label="Save As",accelerator="Save As",image=self.image_saveas,command=self.saveAsFile)
        self.fileMenu.add_separator()
        # self.newPlogo = Image.open("icons8_Book_16.png")
        # self.image = ImageTk.PhotoImage(self.newPlogo)

        self.copylogo = Image.open("icons8_Copy_32.png")
        self.image_copy = ImageTk.PhotoImage(self.copylogo)
        self.EditMenu.add_command(label="Copy",image=self.image_copy,accelerator="Copy")
        self.EditMenu.add_separator()

        self.cutlogo = Image.open("icons8_Cut_32.png")
        self.image_cut = ImageTk.PhotoImage(self.cutlogo)
        self.EditMenu.add_command(label="Cut",image=self.image_cut,accelerator="Cut")
        self.EditMenu.add_separator()

        self.deletelogo = Image.open("icons8_Delete_32.png")
        self.image_delete = ImageTk.PhotoImage(self.deletelogo)    
        self.EditMenu.add_command(label="Delete",image=self.image_delete,accelerator="Delete")
        self.EditMenu.add_separator()

        self.eraserlogo = Image.open("icons8_Eraser_32.png")
        self.image_eraser = ImageTk.PhotoImage(self.eraserlogo)    
        self.EditMenu.add_command(label="Eraser",image=self.image_eraser,accelerator="Eraser")
        self.EditMenu.add_separator()

        self.selectlogo = Image.open("icons8_Select_All_32.png")
        self.image_select = ImageTk.PhotoImage(self.selectlogo)    
        self.EditMenu.add_command(label="Select All",image=self.image_select,accelerator="Select All")
        self.EditMenu.add_separator()



        self.menubar.add_cascade(label="File",menu=self.fileMenu)
        self.menubar.add_cascade(label="Edit",menu=self.EditMenu)
        self.menubar.add_cascade(label="Help",menu=self.HelpMenu)
        self.cover.config(menu=self.menubar)

    def loadimage(self):
        loadcursor = Image.open("icons8_Cursor_16.png")
        self.image_cursor = ImageTk.PhotoImage(loadcursor,master=self.cover)
        self.btn.config(image=self.image_cursor)

        loadcircle = Image.open("icons8_Circle_16.png")
        self.image_cirle = ImageTk.PhotoImage(loadcircle)
        self.btn1.config(image=self.image_cirle)

        loadrec =  Image.open("icons8_Rectangular_16.png")
        self.image_rec = ImageTk.PhotoImage(loadrec)
        self.btn2.config(image=self.image_rec)

        loadtriangle = Image.open("icons8_Triangle_16.png")
        self.image_tri = ImageTk.PhotoImage(loadtriangle)
        self.btn3.config(image=self.image_tri)

        loadline = Image.open("icons8_Line_16.png")
        self.image_line = ImageTk.PhotoImage(loadline)
        self.btn4.config(image=self.image_line)

        loadpaint = Image.open("icons8_Paint_Brush_16.png")
        self.image_paint = ImageTk.PhotoImage(loadpaint)
        self.btn5.config(image=self.image_paint)

    

    def draw(self,shape):
        if shape == "circle":
            self.canva.bind("<Button-1>",self.start)
            self.canva.bind("<B1-Motion>",self.moveStart)
        elif shape == "line":
            self.canva.bind("<Button-1>",self.lin)
            self.canva.bind("<B1-Motion>",self.lin_move)
        elif shape == "rec":
            self.canva.bind("<Button-1>",self.rec)
            self.canva.bind("<B1-Motion>",self.rec_move)            

    def lin(self,event):
        self.coord["x"] = event.x
        self.coord["y"] = event.y

        self.line.append(self.canva.create_line(self.coord["x"],self.coord["y"],self.coord["x"],self.coord["y"]))

    def lin_move(self,event):
        self.coord["x2"] = event.x
        self.coord["y2"] = event.y

        self.canva.coords(self.line[-1],self.coord["x"],self.coord["y"],self.coord["x2"],self.coord["y2"])

    def start(self,event):
        self.circlex0 = self.canva.canvasx(event.x)
        self.circley0 = self.canva.canvasy(event.y)

        self.circle=self.canva.create_oval(self.circlex0,self.circley0,self.circlex0,self.circley0,fill="#263D42")

    def moveStart(self,event):
        self.circlex1 = self.canva.canvasx(event.x)
        self.circley1 = self.canva.canvasy(event.y)

        self.canva.coords(self.circle,self.circlex0,self.circley0,self.circlex1,self.circley1)

    def rec(self,event):
        self.rectx0 = self.canva.canvasx(event.x)
        self.recty0 = self.canva.canvasy(event.y)

        self.rec=self.canva.create_rectangle(self.rectx0,self.recty0,self.rectx0,self.recty0,fill="#263D42")

    def rec_move(self,event):
        self.rectx1 = self.canva.canvasx(event.x)
        self.recty1 = self.canva.canvasy(event.y)

        self.canva.coords(self.rec,self.rectx0,self.recty0,self.rectx1,self.recty1)
    def drag(self):
        self.canva.bind("<Button-1>",self.mouseDown)
        self.canva.bind("<B1-Motion>",self.mouseMove)

    def mouseDown(self,event):
        # # self.canva.move(self.acr,100,100)
            self.lastx=event.x
            self.lasty=event.y
        # print(self.canva.coords(self.lin))

    def mouseMove(self,event):
        self.canva.move(CURRENT,event.x - self.lastx,event.y - self.lasty)
        self.lastx = event.x
        self.lasty = event.y
        # self.canva.bind("<Button-1>",mouseDown)

    def open(self):
        self.open1 = askopenfilenames(defaultextension=".png",filetypes=[("All Files","*.*"),("jpeg","*.jpg*"),("png","*.png*")])
        self.image = Image.open(self.open1)
        self.image = ImageTk.PhotoImage(self.image)
        self.item_id = self.canva.create_image(400,400,image=self.image)

    def save(self):
        if self.in_path == "":
            self.saveAsFile()
        else:
            self.cord = self.canva.coords(self.canva.find_all())
            x = self.canva.winfo_rootx() + self.cord[0]
            y = self.canva.winfo_rooty() + self.cord[1]
            x1 = self.canva.winfo_rootx() + self.cord[2]
            y1 = self.canva.winfo_rooty() + self.cord[3]
            ImageGrab.grab().crop((x,y,x1,y1)).save(self.in_path)     
    def saveAsFile(self):
        self.in_path = asksaveasfilename(initialfile='Untitled.png',defaultextension=".png",filetypes=[("All Files", "*.*"),("PNG","*.png*")])
        # print(self.in_path)
        self.cord = self.canva.coords(self.canva.find_all())
        print(self.cord)
        x = self.canva.winfo_rootx() + self.cord[0]
        y = self.canva.winfo_rooty() + self.cord[1]
        x1 = self.canva.winfo_rootx() + self.cord[2]
        y1 = self.canva.winfo_rooty() + self.cord[3]
        ImageGrab.grab().crop(x,y,x1,y1).save(self.in_path)
        self.cover.title(self.in_path.split("/")[6] + " - Graphics Editor")
        # with open(self.in_path,"w") as self.infile:
        #     self.infile.write(self.a.get(1.0,END))

        # self.cover.title(self.in_path.split("/")[6] + " - Graphics Editor")


paint = Graphics()    
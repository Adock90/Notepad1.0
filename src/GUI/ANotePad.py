from tkinter import *
from tkinter import filedialog
from Writer.saveLod import *
import os

paths = os.getcwd()


app = Tk()
app.geometry("300x500")
app.title("Unititled - ANotePad")
app.iconbitmap("media\\Icon.ico")


NameBar = Label(app, text="Untitled", anchor=E)
NameBar.pack(fill=X, side=BOTTOM, ipady=5)

frame = LabelFrame(app, width=1000, height=1000)
frame.pack()


scrolly = Scrollbar(frame)
scrolly.pack(side=RIGHT, fill=Y)

TextArea = Text(frame, width=1000000, height=1000000, font=("sans serif", 10, "bold"))
TextArea.pack(ipadx=100, ipady=100)


MENU = Menu(app)
app.config(menu=MENU)
def N():
    NewF(TextArea,app, NameBar)

def O():
    OpenF(TextArea, NameBar, app)

def S():
    Save(TextArea, app, NameBar)

def SEN():
    saveasEn(TextArea, app, NameBar)

def OE():
    openE(TextArea, app, NameBar)

Opt = Menu(MENU, tearoff=False)
MENU.add_cascade(label="File", menu=Opt)
Opt.add_command(label="New File", command=N)
Opt.add_command(label="Open", command=O)
Opt.add_command(label="Save", command=S)
Opt.add_command(label="SaveEncrypted", command=SEN)
Opt.add_command(label="OpenEncrypted", command=OE)
scrolly.config(command=TextArea.yview)
app.mainloop()
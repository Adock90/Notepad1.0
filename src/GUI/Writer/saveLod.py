from tkinter import *
from tkinter import filedialog
import os
from cryptography.fernet import Fernet


paths = os.getcwd()

def NewF(text, titles):
    name = "Untitled"
    text.delete("1.0", END)
    titles.title(f'{name} New')

def OpenF(textA, sb, titles):
    textA.delete("1.0", END)
    files = filedialog.askopenfile(initialdir=paths, filetypes=(("Text Files", "*.txt"), ("All Files","*.*")))
    name = files
    sb.config(text=f'{name}')

    content = files.read()

    textA.insert(END, content)
    titles.title(name)

def Save(textAr, titles, sb):
    sfiles = filedialog.asksaveasfilename(initialdir=paths, title="Save File", filetypes=(("Text Files", "*.txt"),("All Files", "*.*")))
    text = textAr.get(1.0, END)
    f = open(sfiles, "w")
    f.write(text)
    f.close()
    titles.title(f'{sfiles}')
    sb.config(text=f'{sfiles}')

def saveasEn(textAr, titles, sb):
    sfiles = filedialog.asksaveasfilename(initialdir=paths, title="Save File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    text = textAr.get(1.0, END)
    f = open(sfiles, "w")
    f.write(text)
    f.close()
    Encrypt(f=sfiles)
    titles.title(f'{sfiles}')
    sb.config(text=f'{sfiles}')


def Encrypt(f):
    key = Fernet.generate_key()
    with open(f+".key", "wb") as keyFile:
        keyFile.write(key)
        keyFile.close()
    with open(f,"rb") as readbytes:
        bytess = readbytes.read()
        readbytes.close()
    encrypted = Fernet(key).encrypt(bytess)
    with open(f, "wb") as fin:
        fin.write(encrypted)
        fin.close()

def Decrypt(f):
    with open(f+".key", "rb") as keyFile:
        key = keyFile.read()
        keyFile.close()
    with open(f,"rb") as readbytes:
        bytess = readbytes.read()
        readbytes.close()
    key.decode('utf-8')
    global decrypted
    decrypted = Fernet(key).decrypt(bytess)
    return decrypted

def openE(textAr, titles, sb):
    ofiles = filedialog.askopenfilename(initialdir=paths, title="Open File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    textAr.delete("1.0", END)
    name = ofiles
    sb.config(text=f'{name}')

    Decrypt(ofiles)
    con = decrypted
    textAr.insert(END, con)
    titles.title(name)
# from tkinter import Label, Tk, Button

# window = Tk()
# w = Label(window, text="Hello, world!")
# w.pack()

# btn = Button(window, text="Hello, world!")
# btn.pack()

# window.mainloop()

from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
from tkinter import ttk

from ping import ping
import time

host = '10.10.5.5'

def ping_loc():
    text_area.insert(tk.INSERT, str(ping(host)) + '\n')

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=0)
ttk.Button(frm, text="Quit", command=ping_loc).grid(column=10, row=0)

text_area = scrolledtext.ScrolledText(root,  
                                      wrap = tk.WORD,  
                                      width = 40,  
                                      height = 10,  
                                      font = ("Times New Roman", 
                                              15)) 

text_area.grid(column = 0, pady = 10, padx = 10) 

root.geometry("800x400")
root.mainloop()
from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
from tkinter import ttk
import time

from ping import *
from config import Config
from log import Log

config = Config()

root = Tk()

root.geometry("800x400")

def ping_loc():
    pass

ttk.Button(text="Quit", command=root.destroy).place(x=450, y=20)
ttk.Button(text="Leaving", command=ping_loc).place(x=450, y=100)
ttk.Button(text="Reboot SR", command=ping_loc).place(x=450, y=140)
ttk.Button(text="Reboot LR", command=ping_loc).place(x=450, y=180)
ttk.Button(text="SR Interface Off", command=ping_loc).place(x=450, y=220)
ttk.Button(text="LR Interface Off", command=ping_loc).place(x=450, y=260)
ttk.Button(text="Switch Antennas", command=ping_loc).place(x=450, y=300)


# text_area = scrolledtext.ScrolledText(root,  
#                                       wrap = tk.WORD,  
#                                       width = 40,  
#                                       height = 15,  
#                                       font = ("Times New Roman", 
#                                               15))

text_area = Text(root, wrap=tk.WORD, width=40, height=20)

text_area.place(x=20, y=20) 

count = 0

def ping_textbox():
    text_area.config(state=tk.NORMAL)
    text_area.tag_config('warning', background='yellow')
    text_area.insert(tk.INSERT, str(int(ping(config.host_to_ping))) + ' ms \n')
    
    if int(text_area.index('end-1c').split('.')[0]) > 18:
        text_area.delete("1.0", "2.0")

    text_area.config(state=tk.DISABLED)
    root.after(config.ping_interval, ping_textbox)

root.after(config.ping_interval, ping_textbox)

root.mainloop()
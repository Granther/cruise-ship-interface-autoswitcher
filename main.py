from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
from tkinter import ttk
import time

from ping import *
from config import Config
from log import Log
from utils import Utils

config = Config()
utils = Utils()

root = Tk()
root.geometry("800x400")

def ping_loc():
    pass

def test(gort):
    print(gort)

ttk.Button(text="Quit", command=root.destroy).place(x=450, y=20)
ttk.Button(text="Leaving", command=utils.leaving).place(x=450, y=100)
ttk.Button(text="Reboot SR", command=lambda: utils.reboot(0)).place(x=450, y=140)
ttk.Button(text="Reboot LR", command=lambda: utils.reboot(1)).place(x=450, y=180)
ttk.Button(text="SR Interface Off", command=lambda: utils.inter_off(0)).place(x=450, y=220)
ttk.Button(text="LR Interface Off", command=lambda: utils.inter_off(1)).place(x=450, y=260)
ttk.Button(text="Switch Antennas", command=utils.switch_antenna).place(x=450, y=300)

text_area = Text(root, wrap=tk.WORD, width=15, height=20)

text_area.place(x=20, y=20) 

text_area.tag_config('high_lat', background='yellow')
text_area.tag_config('mid_lat', background='red')
text_area.tag_config('good_lat', background='green')

def ping_textbox():
    tag = ''

    text_area.config(state=tk.NORMAL)

    p = int(ping(config.host_to_ping))

    if p < 100:
        tag = 'good_lat'
    elif p < 180:
        tag = 'mid_lat'
    else:
        tag = 'high_lat'

    text_area.insert(tk.INSERT, str(p) + ' ms \n', tag)
    
    if int(text_area.index('end-1c').split('.')[0]) > 20:
        text_area.delete("1.0", "2.0")

    text_area.config(state=tk.DISABLED)
    root.after(config.ping_interval, ping_textbox)

root.after(config.ping_interval, ping_textbox)

root.mainloop()
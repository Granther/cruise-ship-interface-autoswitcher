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
utils = Utils(config=config)
log = Log('main')

root = Tk()
root.geometry("800x400")
root.title('Grants Better Ping Autoswitch')

x_col = 200

button_label = Label(root, text='Control')
button_label.place(x=x_col, y=2)

ttk.Button(text="Quit", command=lambda: root.destroy()).place(x=x_col, y=20)
ttk.Button(text="Leaving", command=lambda: utils.leaving()).place(x=x_col, y=100)
ttk.Button(text="Reboot SR", command=lambda: utils.reboot(0)).place(x=x_col, y=140)
ttk.Button(text="Reboot LR", command=lambda: utils.reboot(1)).place(x=x_col, y=180)
ttk.Button(text="SR Interface Off", command=lambda: utils.inter_off(0)).place(x=x_col, y=220)
ttk.Button(text="LR Interface Off", command=lambda: utils.inter_off(1)).place(x=x_col, y=260)
ttk.Button(text="Switch Antennas", command=lambda: utils.switch_antenna()).place(x=x_col, y=300)

status_label = Label(root, text='Status')
status_label.place(x=450, y=2)

status_textbox = Text(root, wrap=tk.WORD, width=40, height=20)
status_textbox.place(x=450, y=20)

ping_label = Label(root, text='Pings')
ping_label.place(x=20, y=2)

ping_textbox = Text(root, wrap=tk.WORD, width=15, height=20)
ping_textbox.place(x=20, y=20) 

ping_textbox.tag_config('high_lat', background='yellow')
ping_textbox.tag_config('mid_lat', background='red')
ping_textbox.tag_config('good_lat', background='green')

def ping_loop():
    tag = ''

    ping_textbox.config(state=tk.NORMAL)

    ping_result = 999

    try:
        ping_result = ping(config.host_to_ping, timeout=0.1)
    except PingException:
        pass
    except Exception as e:
        pass

    if ping_result < config.green_ping_threshold:
        tag = 'good_lat'
    elif ping_result < config.yellow_ping_threshold:
        tag = 'mid_lat'
    else:
        tag = 'high_lat'

    ping_textbox.insert(tk.INSERT, str(ping_result) + ' ms \n', tag)
    
    if int(ping_textbox.index('end-1c').split('.')[0]) > 20:
        ping_textbox.delete("1.0", "2.0")

    ping_textbox.config(state=tk.DISABLED)
    root.after(config.ping_interval, ping_loop)

# def periodic_check():
#     if utils.ath0_status(0) == 0:



#     root.after(config.periodic_check_interval, periodic_check)

root.after(config.ping_interval, ping_loop)
#root.after(config.periodic_check_interval, periodic_check)

root.mainloop()
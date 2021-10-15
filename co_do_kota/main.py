import requests

from tkinter import *
from tkinter import ttk



def create_window():
    
    def change_fact():
        try:
            response = requests.get("https://catfact.ninja/fact")
            display_text.set(response.json()['fact'])
        except:
            display_text.set("nie udalo sie pobrac ciekawostki")
            
    root = Tk(className='cat facts')
    
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    
    display_text = StringVar()
    ttk.Label(frm, textvariable=display_text, wraplengt=400, anchor="center", width=100).grid(column=0, row=0)
    change_fact()
    
    ttk.Button(frm, text="Inna ciekawostka", command=change_fact).grid(column=0, row=1)
    ttk.Button(frm, text="Wyjdz", command=root.destroy).grid(column=0, row=2)
    
    root.mainloop()

create_window()


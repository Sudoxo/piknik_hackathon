import pyautogui
from pynput import mouse

from tkinter import *
from tkinter import ttk


def create_window():
    root = Tk(className='color picker')

    w = Canvas(root, width=200, height=200)
    w.create_rectangle(0,0,200,200,fill='#%02x%02x%02x' % color)
    
    #w.create_text(100,220,text="Zapis heksadecymalny: " + ('#%02x%02x%02x' % color))
    l = Label(root, text = "Zapis heksadecymalny: " + ('#%02x%02x%02x' % color))
    l2 = Label(root, text = "Zapis RGB: (" + str(color[0]) + ", " + str(color[1]) + ", " + str(color[2]) + ")")
    l3 =

    w.pack()
    l.pack()
    l2.pack()
    root.mainloop()

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        global color
        color = pyautogui.pixel(x,y)
        return False



listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()    

create_window()

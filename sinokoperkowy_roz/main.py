import pyautogui
from pynput import mouse

from tkinter import *
from tkinter import ttk

import colorsys

#following rgb_to_cmyk function is taken from https://stackoverflow.com/questions/14088375/how-can-i-convert-rgb-to-cmyk-and-vice-versa-in-python

RGB_SCALE = 255
CMYK_SCALE = 100


def rgb_to_cmyk(r, g, b):
    if (r, g, b) == (0, 0, 0):
        # black
        return 0, 0, 0, CMYK_SCALE

    # rgb [0,255] -> cmy [0,1]
    c = 1 - r / RGB_SCALE
    m = 1 - g / RGB_SCALE
    y = 1 - b / RGB_SCALE

    # extract out k [0, 1]
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy

    # rescale to the range [0,CMYK_SCALE]
    return c * CMYK_SCALE, m * CMYK_SCALE, y * CMYK_SCALE, k * CMYK_SCALE

def create_window():
    root = Tk(className='color picker')

    w = Canvas(root, width=200, height=200)
    w.create_rectangle(0,0,200,200,fill='#%02x%02x%02x' % color)
    
    red = color[0]
    green = color[1]
    blue = color[2]

    hsv = colorsys.rgb_to_hsv(red/255,green/255,blue/255)
    hls = colorsys.rgb_to_hls(red/255,green/255,blue/255)
    cmyk = rgb_to_cmyk(red,green,blue)

    l = Label(root, text = "Zapis heksadecymalny: " + ('#%02x%02x%02x' % color))
    l2 = Label(root, text = "Zapis RGB: (" + str(red) + ", " + str(green) + ", " + str(blue) + ")")
    l3 = Label(root, text="Zapis HSV: (" + str(hsv[0]*360) + ", " + str(hsv[1]) + ", " + str(hsv[2]) + ")")
    l4 = Label(root, text="Zapis HLS: (" + str(hls[0]*360) + ", " + str(hls[1]) + ", " + str(hls[2]) + ")")
    l5 = Label(root, text="Zapis CMYK: (" + str(cmyk[0]) + ", " + str(cmyk[1]) + ", " + str(cmyk[2]) + ", " + str(cmyk[3]) + ")")


    w.pack()
    l.pack()
    l2.pack()
    l3.pack()
    l4.pack()
    l5.pack()
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

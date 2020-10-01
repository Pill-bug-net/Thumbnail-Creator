from PIL import Image
import tkinter as tk
from tkinter import filedialog as fd

def callback():
    name= fd.askopenfilename()
    targetDir = fd.askdirectory()
    im = Image.open(name)
    MAX_SIZE = (250,250)
    MID_SIZE = (125,125)
    SML_SIZE = (60,60)
    im.thumbnail(MAX_SIZE)
    im.save(targetDir + "\\MAX_SIZE.png")

    im.thumbnail(MID_SIZE)
    im.save(targetDir + "\\MID_SIZE.png")
    
    im.thumbnail(SML_SIZE)
    im.save(targetDir + "\\SML_SIZE.png")
    
    #im.show()

tk.Button(text='Chose image file',command=callback).pack(fill=tk.X)
tk.mainloop()
#im = Image.open("C:\\Users\\yuta\\Pictures\\pill-bug.PNG")


from PIL import Image
import tkinter as tk
from tkinter import filedialog as fd

import urllib

def createThumbnail(filepath,targetDir):
    im = Image.open(filepath)
    MAX_SIZE = (250,250)
    MID_SIZE = (125,125)
    SML_SIZE = (60,60)
    im.thumbnail(MAX_SIZE)
    im.save(targetDir + "\\MAX_SIZE.png")

    im.thumbnail(MID_SIZE)
    im.save(targetDir + "\\MID_SIZE.png")
    
    im.thumbnail(SML_SIZE)
    im.save(targetDir + "\\SML_SIZE.png")

def createThumbnailBasedOnLocal():
    name= fd.askopenfilename()
    targetDir = fd.askdirectory()
    createThumbnail(name,targetDir)


def createThumbnailBasedOnOnline():
    urllib.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "00000001.jpg")

tk.Button(text='Chose image from local file',command=createThumbnailBasedOnLocal).pack(fill=tk.X)
tk.Button(text='PastURL and creating thumbnail', command=createThumbnailBasedOnOnline).pack(fill=tk.X)
tk.mainloop()


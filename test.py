from tkinter import *
from PIL import ImageTk

ROOT = Tk()
LOOP_ACTIVE = True
count = 0
image_path = "baby.webp"
img = Image.open(image_path)
photo = ImageTk.PhotoImage(img)
while count < 3:
    LABEL = Label(ROOT, image=photo)
    LABEL.pack()
    count+= 1
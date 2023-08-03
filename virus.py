import pyautogui as p
from random import randint
import tkinter as tk
from PTL import Image, ImageTk

for i in range(20):
    x = randint(1, 1920)
    y = randint(1, 1080)
    p.moveTo(x, y, 0.2)
    
    root = tk.Tk()
    root.title = ("?")

    # Load the image 
    image_path = "baby.webp"
    img = Image.open(image_path)
    photo = ImageTk.PhotoImage(img)   
    
    # Create a label to display the image
    label = tk.Label(root, image=photo)
    label.pack()

    root.mainloop()
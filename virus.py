from PIL import Image, ImageTk
import tkinter as tk
from multiprocessing import Process, freeze_support


def show_image(i):
    img = Image.open('baby.webp')
    window = tk.Tk()
    window.title(f"Window {i}")
    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(window, image=tk_img)
    label.pack()

    # Set the window's position
    x = 50 + (i - 1) * 200  # Change the x position for each window
    y = 50
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

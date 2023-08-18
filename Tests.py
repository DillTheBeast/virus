import os
from email.message import EmailMessage
import ssl
import smtplib
from random import randint

emailer = "logger274@gmail.com"
emailerPassword = "aaybvlfbvjdjafsv"
receiver = "ariellewmaltese@gmail.com"

num = randint(1, 10000000)

subject = 'I am a bot'
# body = """
# Test
# """
body = f"Your random number is: {num}"

em = EmailMessage()
em['From'] = emailer
em['To'] = receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(emailer, emailerPassword)
    smtp.sendmail(emailer, receiver, em.as_string())

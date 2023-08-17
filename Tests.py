import os
from email.message import EmailMessage
import ssl
import smtplib

emailer = "logger274@gmail.com"
emailerPassword = "aaybvlfbvjdjafsv"
receiver = "dillonmaltese@gmail.com"

subject = 'Subject Test'
body = """
Body
Test
"""

em = EmailMessage()
em['From'] = emailer
em['To'] = receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(emailer, emailerPassword)
    smtp.sendmail(emailer, receiver, em.as_string())
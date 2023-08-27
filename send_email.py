import smtplib
import ssl
import os
from dotenv import load_dotenv


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "ggronnii@gmail.com"
    load_dotenv()
    password = os.getenv("PASSWORD")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, message)
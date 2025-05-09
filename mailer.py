from email.message import EmailMessage
import csv
import random
import smtplib
import ssl
import time

# SMTP config (Gmail example, you can edit the server based on what email provider you want)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
EMAIL_ADDRESS = "UR EMAIL HERE"
EMAIL_PASSWORD = "16 LETTER CODE THAT YOU CAN GENERATE, CALLED AN APP PASSWORD"  # Use an App Password, not your actual one

# Load recipients
with open("recipients.csv", newline='') as csvfile:  # import the attached CSV file to the same folder as this, edit the csv and tailor it to your intrests
    reader = csv.DictReader(csvfile)
    recipients = [row for row in reader]

# Create secure SSL context
context = ssl.create_default_context()

# Start sending
with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for person in recipients:
        name = person["name"]
        email = person["email"]

        # Personalize email
        msg = EmailMessage()
        msg["Subject"] = f"PUT YOUR SUBJECT HERE"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = email
        msg.set_content(f"""Hey {name},\n\ THE JUICY STUFF (YOUR CONTENT OF THE EMAIL GOES HERE)""")

        # Send email
        server.send_message(msg)
        print(f"Sent to {name} at {email}")

        # Random delay to mimic human behavior and STOP SPAM
        time.sleep(random.uniform(20, 60))  # 20–60 seconds between sends

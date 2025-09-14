import smtplib
from email.message import EmailMessage

def send_alert(subject, body, to_email):
    EMAIL_ADDRESS = "youremail@gmail.com"   # replace with your email
    EMAIL_PASSWORD = "yourpassword"         # replace with app password

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print(f"Alert sent to {to_email}")

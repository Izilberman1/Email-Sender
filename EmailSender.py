import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Itamar Zilberman'
email['to'] = 'blahblahblah@gmail.com'
email['subject'] = 'Thank you! <3'

email.set_content('May you receive the Galaxy ring from Samsung.')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    #Google's pass through password (https://myaccount.google.com/apppasswords.)
    smtp.login('yoyoyoyoyo@gmail.com', '***********')
    smtp.send_message(email)
    print("email sent successfully")


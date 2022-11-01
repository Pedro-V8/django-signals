from json import load
from django.db.models.signals import post_save
from signals.models import Profile
from django.dispatch import receiver
from dotenv import load_dotenv

import os
import smtplib
import email.message

load_dotenv()
def enviar_email(user_email):  
    content_email = """
    <p>YOUR HTML FILE</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Your Subject"
    msg['From'] = os.getenv('SENDER_EMAIL')
    msg['To'] = user_email
    password = os.getenv('GOOGLE_PASS') 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(content_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('### EMAIL SENT ###')


@receiver(post_save , sender=Profile)
def send_email(sender , instance , created , **kwargs):
    if created:
        enviar_email(str(instance))
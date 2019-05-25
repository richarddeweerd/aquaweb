'''Email routines'''

from flask_mail import Message
from flask import current_app
from app import mail

def send_email(subject, sender, recipients, text_body, html_body):
    '''Send email'''
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    with current_app.app_context():
        mail.send(msg)
        
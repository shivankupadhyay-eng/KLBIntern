from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(email, username):
    subject = 'Welcome to our platform!'
    message = f'Hi {username}, thanks for registering with us. We are excited to have you on board!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

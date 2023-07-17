from django.core.mail import send_mail
from django.conf import settings


def send_emails(email, token):

    subject = ' Conform Login'
    message = f'Conform your account clicking on the link: http://127.0.0.1:8000/homepage/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = []
    send_mail(subject , message, email_from, recipient_list)
    print(message)
    return True



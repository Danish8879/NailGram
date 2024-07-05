
from django.conf import settings
from django.core.mail import send_mail


def send_account_activation_email(email, email_token):
    subject = "NailGram Account Verification"
    email_from = settings.EMAIL_HOST_USER

    content = f"Please click on the link to activate your account \n\n\n  Verification link : http://127.0.0.1:8000/accounts/activate/{email_token}"

    send_mail(subject,content,email_from,[email])
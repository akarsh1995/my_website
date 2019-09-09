from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from celery import shared_task


@shared_task
def email_templated(subject, text_template, recipient_list, context, html_template=None):
    msg_html = render_to_string(html_template, context) if html_template else None
    msg_text = render_to_string(text_template, context)
    send_mail(subject=subject, message=msg_text, from_email=settings.EMAIL_HOST_USER,
              recipient_list=recipient_list, html_message=msg_html)

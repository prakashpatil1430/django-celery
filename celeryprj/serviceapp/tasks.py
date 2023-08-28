from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_task_with_celery():
    send_mail(
        "Celery worked yeah",
        "sending mail using celery.",
        "prakashpatilmeti@gmail.com",
        ["prakashpatilmeti@gmail.com"],
        fail_silently=False,
    )
    print("Mail from celery")
    return None


@shared_task
def wish(name, msg):
    return f'Hello {name} {msg}'

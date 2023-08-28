# from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_mail_task_with_celery
# from .helpers import send_mail_without_celery
from datetime import datetime

# using celery task of sendong mail


def disp_celery_call(request):
    start_time = datetime.now()
    for i in range(5):

        send_mail_task_with_celery.delay()
        print(f'{i}')
    return HttpResponse(f"sent mail using celery,time taken :{datetime.now()-start_time}")

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('send_mail/', views.disp_celery_call),

]

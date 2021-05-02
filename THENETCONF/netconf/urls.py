# todoapp/urls.py
from django.urls import path
from .views import index, program, committee, Intro, contact, register

urlpatterns = [
    path('', index, name='index'),
    path('program', program, name='program'),
    path('committee', committee, name='committee'),
    path('contact', contact, name='contact'),
    path('register', register, name='register'),


]
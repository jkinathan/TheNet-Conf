# todoapp/urls.py
from django.urls import path
from .views import index, program, committee, Intro

urlpatterns = [
    path('', Intro.as_view(), name='index'),
    path('program', program, name='program'),
    path('committee', committee, name='committee'),

]
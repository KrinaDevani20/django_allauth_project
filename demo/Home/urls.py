from .views import hello,login
from django.urls import path

app_name = 'Home'


urlpatterns=[
    path('',hello,name='Home'),
    path("login",login)
]
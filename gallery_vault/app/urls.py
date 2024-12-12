from django.urls import path
from . import views
urlpatterns=[
    path('',views.login),
    path('register',views.register),
    path('index',views.index),
    path('logout',views.user_logout),
    path('upload',views.upload),
]
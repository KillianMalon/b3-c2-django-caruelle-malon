from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.listing, name='listing'),
]
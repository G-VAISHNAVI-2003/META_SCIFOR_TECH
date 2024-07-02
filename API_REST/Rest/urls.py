# blog/urls.py
from django.urls import path
from rest import views

urlpatterns = [
    path('', views.fetch_posts, name='fetch_posts'),
]

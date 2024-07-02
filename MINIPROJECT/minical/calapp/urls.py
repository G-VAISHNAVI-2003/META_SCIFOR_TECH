from django.urls import path

from calapp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('blog',views.blog,name="blog"),
]

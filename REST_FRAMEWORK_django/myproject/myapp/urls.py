from django.urls import path
from .views import PostView,post_list_view 

urlpatterns = [
    path('', post_list_view, name='post_list_view'),
    path('posts/',PostView.as_view(),name='post-list'),
    path('posts/<int:pk>/',PostView.as_view(),name = 'post-detail'),
]

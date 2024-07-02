from django.urls import path
from .views import g_get, g_post, g_put, g_patch, g_delete

urlpatterns = [
    path('get/', g_get, name='g_get'),  
    path('posts/', g_post, name='g_post'),  
    path('posts/<int:post_id>/', g_put, name='g_put'),  
    path('patch/<int:post_id>/', g_patch, name='g_patch'),  
    path('delete/<int:post_id>/', g_delete, name='g_delete'), 
    ]

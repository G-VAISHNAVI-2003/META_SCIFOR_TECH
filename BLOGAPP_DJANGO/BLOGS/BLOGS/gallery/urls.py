from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('Template/index.html', views.product_list, name='product_list'),
	path('Template/index2.html', views.product_detail, name='product_detail'),
	path('Template/edit.html', views.edit_product, name='edit_product'),
	path('Template/delete.html', views.delete_product, name='delete_product'),
]

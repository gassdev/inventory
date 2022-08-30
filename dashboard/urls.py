from django.urls import path
from . import views
app_name='dashboard'
urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('staff/', views.staff, name='staff'),
    path('product/', views.product, name='product'),
    path('product/delete/<int:pk>/', views.delete_product, name='product-delete'),
    path('product/update/<int:pk>/', views.update_product, name='product-update'),
    path('order/', views.order, name='order'),
]

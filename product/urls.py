from django.urls import path

from . import views

urlpatterns = [
    path('api/products/', views.product_list, name="product_list"),
    path('api/products/<int:product_id>/', views.product_detail, name='product_detail'),
]
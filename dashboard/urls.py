from django.urls import path
from .import views


urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard-index'),  
    path('staff/', views.staff_view, name='dashboard-staff'),
    path('orders/', views.orders_view, name='dashboard-orders'),
    path('products/', views.products_view, name='dashboard-products'),
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'),
    path('product/update/<int:pk>/', views.product_update, name='dashboard-product-update'),
]   

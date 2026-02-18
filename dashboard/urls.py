from django.urls import path
from .import views


urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard-index'),  
    path('staff/', views.staff_view, name='dashboard-staff'),
    path('products/', views.products_view, name='dashboard-products'),
    path('orders/', views.orders_view, name='dashboard-orders'),
]   

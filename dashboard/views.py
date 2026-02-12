from django.shortcuts import render
from django.http import HttpResponse

def dashboard_view(request):
    return render(request, 'dashboard/index.html')


def staff_view(request):
    return render(request, 'dashboard/staff.html')  

def products_view(request):
    return render(request, 'dashboard/product.html')

def orders_view(request):
    return render(request, 'dashboard/order.html')

def register(request):
    return render(request, 'dashboard/register.html')   


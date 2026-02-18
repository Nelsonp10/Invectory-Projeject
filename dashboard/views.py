from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from.models import product
from django.http import HttpResponse

@login_required
def dashboard_view(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff_view(request):
    return render(request, 'dashboard/staff.html')  

@login_required
def products_view(request):
    return render(request, 'dashboard/product.html')

@login_required
def orders_view(request):
    return render(request, 'dashboard/order.html')

def register(request):
    return render(request, 'dashboard/register.html')   


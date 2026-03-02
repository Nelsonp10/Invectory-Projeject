from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from.models import product
from django.http import HttpResponse
from .models import product
from .forms import ProductForm

@login_required
def dashboard_view(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff_view(request):
    return render(request, 'dashboard/staff.html')  

@login_required
def products_view(request):
    items =product.objects.all()
   #items = product.objects.raw('SELECT * FROM dashboard_product')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
         form.save()
        return redirect('dashboard-products')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'form':form,
    }
    return render(request, 'dashboard/product.html',context)

def product_delete(request,pk):
    item = product.objects.get(id=pk)
    if request.method =='POST':
        item.delete()
        return redirect('dashboard-products')
    
    return render(request, 'dashboard/product_delete.html')

def product_update(request,pk):
    item = product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect ('dashboard-products')
            
    else:
        form = ProductForm(instance = item)
    context= {
        'form': form,

        }
    return render(request,'dashboard/product_update.html',context)


@login_required
def orders_view(request):
    return render(request, 'dashboard/order.html')

def register(request):
    return render(request, 'dashboard/register.html')   



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from.models import product
from django.http import HttpResponse
from .models import product, oder
from .forms import ProductForm, oderForm
from django.contrib.auth.models import User
from django.contrib import messages

@login_required
def dashboard_view(request):
    oders= oder.objects.all()
    if request.method == 'POST':
        form = oderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff=request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form =oderForm()
       
    context={
       'oders':oders,
       'form':form,
    }
    return render(request, 'dashboard/index.html',context)

@login_required
def staff_view(request):
    workers = User.objects.all()
    context = {
        'workers':workers
    }
    return render(request, 'dashboard/staff.html', context)  

@login_required
def products_view(request):
    items =product.objects.all()
   #items = product.objects.raw('SELECT * FROM dashboard_product')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
         form.save()
         product_name = form.cleaned_data.get('name')
         messages.success(request, f'{product_name} has been added')

        return redirect('dashboard-products')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'form':form,
    }
    return render(request, 'dashboard/product.html',context)
@login_required
def staff_detail(request,pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers':workers,
    }
    
    return render (request,'dashboard/staff_detail.html',context)

@login_required
def product_delete(request,pk):
    item = product.objects.get(id=pk)
    if request.method =='POST':
        item.delete()
        return redirect('dashboard-products')
    
    return render(request, 'dashboard/product_delete.html')

@login_required
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
    oders = oder.objects.all()
    context ={
        'oders':oders,
    }
    return render(request, 'dashboard/order.html',context)

def register(request):
    return render(request, 'dashboard/register.html')   



import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import Product, ProductForm

# Create your views here.

@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required
def product(request):
    items = Product.objects.order_by('-id').all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added sucessfully!')
            return redirect('dashboard:product')
    else:
        form = ProductForm()

    context = {
        'items': items,
        'form': form
    }
    return render(request, 'dashboard/product.html', context)

@login_required
def delete_product(request, pk):
    item = Product.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.info(request, 'Product deleted successfully!')
        return redirect('dashboard:product')
    return render(request, 'dashboard/delete_product.html')

@login_required
def update_product(request, pk):
    item = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('dashboard:product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form':form
    }
    return render(request, 'dashboard/update_product.html', context)


@login_required
def order(request):
    return render(request, 'dashboard/order.html')
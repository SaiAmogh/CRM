from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.
@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    products = Product.objects.all()
    product_count = products.count()
    workers_count = User.objects.all().count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('app-index')
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'products': products,
        'workers_count': workers_count,
        'product_count': product_count,
        'orders_count': orders_count,
        'form': form
    }
    return render(request, 'app/index.html', context)

#staff
@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    product_count = Product.objects.all().count()
    orders_count = Order.objects.all().count()
    context = {
        'workers': workers,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'product_count': product_count,
    }
    return render(request,'app/staff.html',context)

#staff detail
@login_required
def staff_detail(request,pk):
    workers = User.objects.get(id=pk)
    context ={
        'workers': workers,
    }
    return render(request, 'app/staff_detail.html',context)

#product

@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    product_count = items.count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('app-product')
    else:
        form = ProductForm()
    context = {
        'items':items,
        'product_count': product_count,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'form':form
    }
        
    
    return render(request, 'app/product.html', context)

#product delete

@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('app-product')
    return render(request,'app/product_delete.html')


#product update
@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('app-product')
    else:
        form = ProductForm(instance=item)
    context ={
        'form':form
    }
    return render(request, 'app/product_update.html', context)



#order
@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    workers_count = User.objects.all().count()
    product_count = Product.objects.all().count()
    orders_count = orders.count()
    context = {
        'orders':orders,
        'orders_count': orders_count,
        'workers_count': workers_count,
        'product_count': product_count,
    }
    return render(request, 'app/order.html', context)

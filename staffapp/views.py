from django.shortcuts import render,redirect,get_object_or_404
from ProductApp.models import Product
from ProductApp.forms import ProductForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from ProductApp.models import Order
from django.contrib.auth.models import User


# Create your views here.

def staff_view(request):
    all_product = Product.objects.count()
    all_order = Order.objects.count()
    user_visited = User.objects.filter(is_staff=False,is_superuser=False).count()

    return render(request,'staffapp/staff.html',{'all_product':all_product,'all_order':all_order,'users':user_visited})


#add product
def add_product_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        form.is_valid()
        form.save()
        messages.success(request,'Product added successfuly',extra_tags='success')
        return redirect('products')
    return render(request, 'StaffApp/add_product.html',{'form': form})

#product show in staff
def products_view(request):
    data = Product.objects.all()
    return render(request,'staffapp/product.html',{'data':data})

#update product 
def product_update_view(request,id):
    obj=Product.objects.get(id=id)
    form = ProductForm(instance=obj)
    if request.method == 'POST':
        form =ProductForm(request.POST,instance=obj)
        if form.is_valid:
            form.save()
            return redirect('products')
    return render(request,'staffapp/add_product.html',{'form':form})

#product delete 
def product_delete_confirm_view(request,id):
    product=Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return render(request,'staffapp/product_confirm.html',{'product':product})

@staff_member_required
def staff_orders_view(request):
    orders = Order.objects.all().order_by('-created_at')

    return render(request, 'staffapp/orders.html', {
        'orders': orders
    })

@staff_member_required
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        status = request.POST.get('status')
        order.status = status
        order.save()

    return redirect('staff_orders')

#customers count

def customers_view(request):
    all_user = User.objects.filter(is_staff=False,is_superuser=False)
    return render(request,'staffapp/customers.html',{'users':all_user})
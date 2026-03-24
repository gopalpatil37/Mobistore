from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import OrderItem,Order


# Create your views here.
def home_view(request):
    products= Product.objects.all()

    return render(request, 'ProductApp/index.html',{'products':products})

def about_view(request):
    return render(request, 'ProductApp/about.html')

def mobile_view(request):
    return render(request, 'ProductApp/mobiles.html',)

def contact_view(request):
    return render(request, 'ProductApp/contact.html')

def profile_view(request):
    return render(request, 'ProductApp/profile.html')

# views.py
def products(request):
    data = Product.objects.all()
    return render(request, 'ProductApp/products.html',{'all_data':data})

def offer_view(request):
    return render(request, 'ProductApp/offers.html')


def product_detail_view(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'ProductApp/product_detail.html',{'product':product})

@require_POST
def add_to_cart(request,id):
    product = get_object_or_404(Product, id=id)

    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)]['quantity'] += 1
    else:
        cart[str(id)] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
            'image': product.image.url
        }

    request.session['cart'] = cart
    return redirect('cart_view')

def cart_view(request):
    cart = request.session.get('cart', {})
    total = 0

    for item in cart.values():
        item['item_total'] = item['price'] * item['quantity']
        total += item['item_total']

    return render(request, 'ProductApp/cart.html', {
        'cart': cart,
        'total': total
    })


def increase_quantity(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)]['quantity'] += 1

    request.session['cart'] = cart
    return redirect('cart_view')


def decrease_quantity(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)]['quantity'] -= 1

        if cart[str(id)]['quantity'] <= 0:
            del cart[str(id)]

    request.session['cart'] = cart
    return redirect('cart_view')


def remove_from_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        del cart[str(id)]

    request.session['cart'] = cart
    return redirect('cart_view')


@login_required
def checkout_view(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('cart_view')

    total = 0
    for item in cart.values():
        item['item_total'] = item['price'] * item['quantity']
        total += item['item_total']

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # 1️⃣ Create Order
        order = Order.objects.create(
            user=request.user,
            name=name,
            phone=phone,
            address=address,
            total_amount=total
        )

        # 2️⃣ Create Order Items
        for item in cart.values():
            OrderItem.objects.create(
                order=order,
                product_name=item['name'],
                price=item['price'],
                quantity=item['quantity']
            )

        # 3️⃣ Clear cart
        request.session['cart'] = {}

        return render(request, 'ProductApp/order_success.html', {
            'order_id': order.id
        })

    return render(request, 'ProductApp/checkout.html', {
        'cart': cart,
        'total': total
    })


@login_required
def my_orders_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'ProductApp/my_orders.html', {
        'orders': orders
    })
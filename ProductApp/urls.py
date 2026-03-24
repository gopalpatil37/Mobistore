from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name='home'),
    path('about/',views.about_view, name='about'),
    path('mobiles/',views.mobile_view, name='mobiles'),
    path('contact/',views.contact_view, name='contact'),
    path('profile/',views.profile_view, name='profile'),
    path('products/', views.products, name='all_products'),
    path('offer/',views.offer_view, name='offer'),

    
    path('product-detail/<id>',views.product_detail_view, name='product_detail'),
    path('add-to-cart/<id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/',views.cart_view,name='cart_view'),
    path('cart/increase/<int:id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('my-orders/', views.my_orders_view, name='my_orders'),

]
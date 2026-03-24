from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/',views.staff_view,name='dashboard'),
    path('add-product/',views.add_product_view, name='add_product'),
    path('products/',views.products_view,name='products'),
    path('update/<id>/',views.product_update_view,name='update'),
    path('delete-confirm/<id>/',views.product_delete_confirm_view,name='delete_confirm'),

    path('orders/', views.staff_orders_view, name='staff_orders'),
    path('orders/update/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('customers',views.customers_view,name='customers'),
]




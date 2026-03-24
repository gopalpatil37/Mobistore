from django.contrib import admin
from .models import Product,Order,OrderItem



# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display =  ['image','name','brand','price','price','ram','storage','processor']

admin.site.register(Product,ProductAdmin)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product_name', 'price', 'quantity']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'phone', 'total_amount', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'phone', 'user__username']
    inlines = [OrderItemInline]
    readonly_fields = ['total_amount', 'created_at']
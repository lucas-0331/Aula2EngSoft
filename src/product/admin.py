from django.contrib import admin
from .models import Category, Product, Order, Product_Order


class CategoryInline(admin.StackedInline):
    model = Product
    extra = 1
    

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'product_value',
        'product_quantity',
        'product_category',
        'product_establishment',
    )


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


class OrderInline(admin.TabularInline):
    model = Product_Order
    extra = 1
    

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInline]


class Product_OrderAdmin(admin.ModelAdmin):
    list_display = (
        'product_order_products',
        'product_order_order',
        'product_order_quantity',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product_Order, Product_OrderAdmin)
from django.contrib import admin
from .models import Product, Order

admin.site.site_header = 'Inventory System'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'qty')
    list_filter = ('category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
from django.contrib import admin
from .models import Category, Product, Shop

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'open']
    list_filter = ['open']
    list_editable = ['open']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
from django.contrib import admin

from product.models import Category, Product


# admin registration for model Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


# admin registration for model Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image_url', 'cost', 'count', 'category', )

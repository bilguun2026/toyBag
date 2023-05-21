from django.contrib import admin

from .models import  CartItem, Category, Toy

# Register your models here.
admin.site.register(Toy)
admin.site.register(CartItem)
admin.site.register(Category)



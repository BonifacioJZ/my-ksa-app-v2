from django.contrib import admin
from .models.cart import Cart, CartItem
# Register your models here.

admin.site.register(Cart)
admin.site.register(CartItem)

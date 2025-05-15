import uuid
from django.db import models
from django.conf import settings
from src.product.models.presentation import Presentation

# Create your models here.
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_items = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Carrito de {self.user.username} - {self.total_items} productos"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    presentation = models.ForeignKey(Presentation,related_name="presentation",on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"
        ordering = ['-created_at']
        unique_together = ('cart', 'presentation',)

    def __str__(self):
        return f"Item en el carrito de {self.cart.user.username} - {self.quantity} unidades de {self.presentation.name}"
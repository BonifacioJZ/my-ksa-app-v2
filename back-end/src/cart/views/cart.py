from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..serializers.cart import CartSerializer, CartItemSerializer
from ..models.cart import Cart, CartItem
from ...product.models.presentation import Presentation

class CartDetailView(generics.RetrieveAPIView):
    """
    Vista para obtener, actualizar o eliminar un carrito.
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = CartSerializer
    
    def get_object(self):
        cart,_ = Cart.objects.get_or_create(user=self.request.user)
        return cart
    
    
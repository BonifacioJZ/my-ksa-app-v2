from rest_framework import generics,status
from rest_framework.response import Response
from decimal import Decimal
from rest_framework.request import Request
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
    
class AddToCartView(generics.GenericAPIView):
    """
    Vista para agregar un producto al carrito.
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = CartItemSerializer
    
    def post(self,request:Request, *args, **kwargs):
        """
        Agrega un producto al carrito.
        """
        cart,_ = Cart.objects.get_or_create(user=self.request.user)
        presentation_id = request.data.get('presentation')
        quantity = Decimal(request.data.get('quantity',1))
        
        try:
            presentation = Presentation.objects.get(id=presentation_id)
        except Presentation.DoesNotExist:
            return Response({"detail": "Producto no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        item,created = CartItem.objects.get_or_create(cart=cart,presentation=presentation)
        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()
        return Response(CartItemSerializer(item).data, status=status.HTTP_201_CREATED)
    
class RemoveToCartView(generics.DestroyAPIView):
    """
    Vista para eliminar un producto del carrito.
    """
    permission_classes = [IsAuthenticated,]
    
    def delete(self,request:Request,pk=None, *args, **kwargs):
        """
        Elimina un producto del carrito.
        """
        cart,_ = Cart.objects.get_or_create(user=self.request.user)
        try:
            item = cart.items.get(pk=pk)
            item.delete()
            return Response({"detail": "Producto eliminado del carrito."}, status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({"detail": "Producto no encontrado en el carrito."}, status=status.HTTP_404_NOT_FOUND)
        except CartItem.MultipleObjectsReturned:
            return Response({"detail": "Error al eliminar el producto del carrito."}, status=status.HTTP_400_BAD_REQUEST)

class CleanCartView(generics.GenericAPIView):
    """
    Vista para limpiar el carrito.
    """
    permission_classes = [IsAuthenticated,]
    
    def delete(self,request:Request, *args, **kwargs):
        """
        Limpia el carrito.
        """
        cart,_ = Cart.objects.get_or_create(user=self.request.user)
        cart.items.all().delete()
        return Response({"detail": "Carrito limpiado."}, status=status.HTTP_204_NO_CONTENT)
            
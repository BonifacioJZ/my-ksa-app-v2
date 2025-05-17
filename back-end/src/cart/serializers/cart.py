from rest_framework import serializers
from src.cart.models.cart import Cart, CartItem
from src.product.models.presentation import Presentation
from src.product.models.product import Product
from src.user.models import UserAccount

class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para el usuario.
    """
    class Meta:
        model = UserAccount
        fields = ('id', 'username', 'email')
        read_only_fields = ('id',)

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializador para el producto.
    """
    class Meta:
        model = Product
        fields = ('id', 'name', 'slug')
        read_only_fields = ('id', 'slug')
    
class PresentationSerializer(serializers.ModelSerializer):
    """
    Serializador para la presentación del producto.
    """
    product = ProductSerializer(read_only=True)
    
    class Meta:
        model = Presentation
        fields = ('id', 'sku', 'name', 'stock', 'bar_code', 'abbreviation', 'product', 'price')
        read_only_fields = ('id',)
    

class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializador para los items del carrito.
    """
    presentation_details = PresentationSerializer(source="presentation",read_only=True)
    total = serializers.SerializerMethodField(method_name='total_item')
    
    class Meta:
        model = CartItem
        fields = ('id', 'presentation','presentation_details', 'quantity', 'total',)
        read_only_fields = ('id',)
    
    def total_item(self,cart_item:CartItem):
        """
        Calcula el total del item en el carrito.
        """
        return cart_item.presentation.price * cart_item.quantity
    
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    user_detail = UserSerializer(read_only=True,source='user')
    total_items = serializers.SerializerMethodField(method_name='total_products')
    class Meta:
        model = Cart
        fields = ('id', 'user', 'user_detail','total_items',  'items')
        read_only_fields = ('id', 'items','user_detail',)
    
    def total(self,cart:Cart):
        """
        Calcula el total del carrito.
        """
        total = 0
        for item in cart.items.all():
            total += item.presentation.price * item.quantity
        return total
    
    def total_products(self,cart:Cart):
        """
        Calcula el total de items en el carrito.
        """
        total = 0
        for item in cart.items.all():
            total += item.quantity
        return total
    
    def to_representation(self, instance: Cart):
        """
        Serializa el objeto Cart.
        """
        representation = super().to_representation(instance)
        representation['total'] = self.total(instance)
        return representation
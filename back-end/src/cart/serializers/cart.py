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
    presentation = PresentationSerializer(source="presentation",read_only=True)
    total = serializers.SerializerMethodField(method_name='total')
    
    class Meta:
        model = CartItem
        fields = ('id', 'presentation' 'quantity', 'total',)
        read_only_fields = ('id',)
    
    def total(self,cart_item:CartItem):
        """
        Calcula el total del item en el carrito.
        """
        return cart_item.presentation.price * cart_item.quantity
    def to_representation(self, instance: CartItem):
        """
        Serializa el objeto CartItem.
        """
        representation = super().to_representation(instance)
        representation['total'] = self.total(instance)
        return representation
    
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    user_detail = UserSerializer(read_only=True,source='user')
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
    def to_representation(self, instance: Cart):
        """
        Serializa el objeto Cart.
        """
        representation = super().to_representation(instance)
        representation['total'] = self.total(instance)
        return representation
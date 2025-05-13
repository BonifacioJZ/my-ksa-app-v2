from rest_framework import serializers
from ..models.presentation import Presentation
from ..models.product import Product

class ProductPresentationSerializer(serializers.ModelSerializer):
    """
    Serializador para la presentación de productos.
    """
    class Meta:
        model = Product
        fields = ('name', 'slug',)
        read_only_fields = ( 'slug',)

class PresentationListSerializer(serializers.ModelSerializer):
    """
    Serializador para la lista y creación de presentaciones.
    """
    product_detail = ProductPresentationSerializer(source='product',read_only=True)
    class Meta:
        model = Presentation
        fields = (
            'id', 
            'sku',
            'name',
            'stock',
            'bar_code',
            'abbreviation',
            'product',
            'product_detail',
            'price', 
            'slug',
            )
        read_only_fields = ('id', 'slug',)
        extra_kwargs = {
            'name': {'required': True},
            'sku': {'required': True},
            'stock': {'required': True},
            'bar_code': {'required': True},
            'abbreviation': {'required': True},
            'product': {'required': True},
            'price': {'required': True},
        }
class PresentationDetailSerializer(serializers.ModelSerializer):
    """
    Serializador para la recuperación de detalles de una presentación.
    """
    product_detail = ProductPresentationSerializer(source="product",read_only=True)
    
    class Meta:
        model = Presentation
        fields = (
            'id', 
            'sku',
            'name',
            'stock',
            'bar_code',
            'abbreviation',
            'product',
            'product_detail',
            'price', 
            'slug',
            'created_at', 
            'updated_at',
        )
        read_only_fields = ('id', 'slug', 'created_at', 'updated_at',)
        
class PresentationSearchSerializer(serializers.ModelSerializer):
    """
    Serializador para la recuperación de detalles de una presentación.
    """
    product_detail = ProductPresentationSerializer(source="product",read_only=True)
    
    class Meta:
        model = Presentation
        fields = (
            'id', 
            'sku',
            'name',
            'stock',
            'bar_code',
            'abbreviation',
            'product',
            'product_detail',
            'price', 
            'slug',
            'created_at', 
            'updated_at',
        )
        read_only_fields = ('id', 'slug', 'created_at', 'updated_at',)

class PresentationUpdateSerializer(serializers.ModelSerializer):
    """
    Serializador para la actualización de una presentación.
    """
    class Meta:
        model = Presentation
        fields = (
            'id', 
            'sku',
            'name',
            'stock',
            'bar_code',
            'abbreviation',
            'product',
            'price', 
            'slug',
        )
        read_only_fields = ('id', 'slug',)
        extra_kwargs = {
            'name': {'required': True},
            'sku': {'required': True},
            'stock': {'required': True},
            'bar_code': {'required': True},
            'abbreviation': {'required': True},
            'product': {'required': True},
            'price': {'required': True},
        }

class PresentationDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = ('id', 'name', 'slug')
        read_only_fields = ('id', 'slug')
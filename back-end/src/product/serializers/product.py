from rest_framework import serializers
from ..models.product import Product
from ..models.category import Category
from ..models.presentation import Presentation

class PresentationProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = ('id', 'sku', 'name', 'stock', 'product', 'price',)
        read_only_fields = ('id',)
class CategoryProductSerializer(serializers.ModelSerializer):
    """
    Serializador para la categoría de un producto.
    """
    class Meta:
        model = Category
        fields = ( 'name', 'slug')
        read_only_fields = ('slug',)

class BrandProductSerializer(serializers.ModelSerializer):
    """
    Serializador para la marca de un producto.
    """
    class Meta:
        model = Product
        fields = ('name', 'slug',)
        read_only_fields = ('slug',)

class ProductListCreateSerializer(serializers.ModelSerializer):
    category_details = CategoryProductSerializer(source='category', read_only=True) 
    brand_details = BrandProductSerializer(source='brand', read_only=True)
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'category',
            'category_details',
            'brand',
            'brand_details',
            'slug',
            'created_at',
            'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at','slug',)
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': True},
            'brand': {'required': True},
            'category': {'required': True},
        }
        
class ProductDetailSerializer(serializers.ModelSerializer):
    """
    Serializador para los detalles de un producto.
    """
    category_details = CategoryProductSerializer(source='category', read_only=True) 
    brand_details = BrandProductSerializer(source='brand', read_only=True)
    presentation = PresentationProductSerializer(many=True, read_only=True, source="products")
    
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'category',
            'category_details',
            'brand',
            'brand_details',
            'presentation',
            'slug',
            'created_at',
            'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at','slug',)


class ProductUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'category',
            'brand',
            'slug',
            'created_at',
            'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at','slug',)
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': True},
            'brand': {'required': True},
            'category': {'required': True},
        }
class ProductDeleteSerializer(serializers.ModelSerializer):
    """
    Serializador para eliminar un producto.
    """
    class Meta:
        model = Product
        fields = ('id', 'name', 'slug')
        read_only_fields = ('id', 'slug')
        extra_kwargs = {
            'name': {'required': True}
        }
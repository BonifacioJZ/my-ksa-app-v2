from rest_framework import serializers
from ..models.product import Product
from ..models.category import Category

class CategoryProductSerializer(serializers.ModelSerializer):
    """
    Serializador para la categoría de un producto.
    """
    class Meta:
        model = Category
        fields = ( 'name', 'slug')
        read_only_fields = ('slug',)

class ProductListCreateSerializer(serializers.ModelSerializer):
    category_details = CategoryProductSerializer(source='category', read_only=True) 
    
    
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'category',
            'category_details',
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
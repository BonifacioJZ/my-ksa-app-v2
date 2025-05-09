from rest_framework import serializers
from ..models.category import Category
from ..models.product import Product


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'name', 'description', 'slug']
        read_only_fields = ['slug']
        
class CategoryListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description','slug', )
        read_only_fields = ('id', 'slug',)
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': False},
        }

class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductCategorySerializer(many=True, read_only=True,source='category')
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'slug','products', 'created_at', 'updated_at']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at','products']
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': False},
        }

class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'slug', 'created_at', 'updated_at']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': False},
        }

class CategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'slug', 'created_at', 'updated_at']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': False},
        }

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'slug', 'created_at', 'updated_at']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': False},
        }
from rest_framework import serializers
from ..models.brand import Brand
from ..models.product import Product


class BrandProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'slug',)
        read_only_fields = ('slug',)

class BrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'slug')
        read_only_fields = ('id', 'slug')
        extra_kwargs = {
            'name': {'required': True}
        }
        
class BrandDetailSerializer(serializers.ModelSerializer):
    products = BrandProductSerializer(many=True, read_only=True, source='brand')
        
    class Meta:
        model = Brand
        fields = ('id', 'name', "products" ,'slug', 'created_at', 'updated_at')
        read_only_fields = ('id', 'slug', 'created_at', 'updated_at')
        extra_kwargs = {
            'name': {'required': True}
        }

class BrandUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'slug')
        read_only_fields = ('id', 'slug')
        extra_kwargs = {
            'name': {'required': True}
        }

class BrandDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'slug')
        read_only_fields = ('id', 'slug')
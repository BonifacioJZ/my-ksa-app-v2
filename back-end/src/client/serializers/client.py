from rest_framework import serializers
from ..models.client import Client

class ClientCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'last_name','email', 'phone', 'address','slug')
        read_only_fields = ('id', 'slug')
        extra_kwargs = {
            'name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': False},
            'phone': {'required': True},
            'address': {'required': False},
        }
class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'last_name', 'email', 'phone', 'address','slug')
        read_only_fields = ('id', 'slug')

class ClientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'last_name', 'email', 'phone', 'address','slug')
        read_only_fields = ('id', 'slug')
        extra_kwargs = {
            'name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': False},
            'phone': {'required': True},
            'address': {'required': False},
        }

class ClientDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'last_name', 'email', 'phone', 'address','slug')
        read_only_fields = ('id', 'slug')


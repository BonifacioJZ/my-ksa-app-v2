from rest_framework import serializers
from ..models.sale import Sale,SaleDetail

class SaleCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('folio','client','date','total','pay','change','status','seller',)
        read_only_fields = ['id', 'folio','client', 'total', 'seller']
        extra_kwargs = {
            'date': {'required': False},
            'pay': {'required': False},
            'change': {'required': False},
            'status': {'required': False},
        }
        
    def perform_create(self, serializer):
        """
        Create a new sale
        """
        serializer.save(seller=self.context['request'].user)
        return serializer
    def create(self, validated_data):
        return super().create(validated_data)
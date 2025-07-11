from django.db import transaction
from rest_framework import serializers
from ..models.sale import Sale,SaleDetail
from ...cart.models.cart import Cart
from ...product.serializers.product import PresentationProductSerializer


class SaleDetailSerializer(serializers.ModelSerializer):
    presentation_details = PresentationProductSerializer(read_only=True,source='presentation')
    class Meta:
        model = SaleDetail
        fields = ('presentation_details','presentation', 'quantity', 'price')
class SaleCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id','folio','client','date','total','pay','change','status','seller',)
        read_only_fields = ['id', 'folio', 'total', 'seller']
        extra_kwargs = {
            'date': {'required': False},
            'pay': {'required': False},
            'change': {'required': False},
            'status': {'required': False},
        }
        
    def create(self, validated_data):
        user = self.context['request'].user
        client = validated_data['client']
        try:
            cart = Cart.objects.prefetch_related('items').get(user=user)
        except Cart.DoesNotExist:
            raise serializers.ValidationError("El carrito no existe.")
        if not cart.items.exists():
            raise serializers.ValidationError("El carrito está vacío.")
        
        with transaction.atomic():
            sale = Sale.objects.create(
                client=client,
                total=cart.get_total(),
                pay=validated_data.get('pay', 0),
                change=validated_data.get('change', 0),
                status=validated_data.get('status', 'pending'),
                seller=user
            )
            for item in cart.items.all():
                presentation = item.presentation
                if presentation.stock < item.quantity:
                    raise serializers.ValidationError(
                        f"Cantidad solicitada para {presentation.name} no disponible en stock."
                    )
                # Actualizar el stock del producto
                presentation.stock -= item.quantity
                presentation.save()
                # Crear el detalle de la venta
                SaleDetail.objects.create(
                    sale=sale,
                    presentation=item.presentation,
                    quantity=item.quantity,
                    price=item.presentation.price,
                    subtotal=item.get_subtotal()
                )
            # Limpiar el carrito después de la compra
        cart.items.all().delete()
        return sale
    
class SaleDetailsSerializer(serializers.ModelSerializer):
    details = SaleDetailSerializer(many=True, read_only=True,source='sale')
    
    class Meta:
        model = Sale
        fields = ('id', 'folio', 'client', 'date', 'total', 'pay', 'change', 'status', 'seller', 'details')
        read_only_fields = ['id', 'folio', 'total', 'seller']


class SaleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'folio', 'client', 'date', 'total', 'pay', 'change', 'status')
        read_only_fields = ['id', 'folio', 'total','date']
        extra_kwargs = {
            'pay': {'required': True},
            'change': {'required': True},
            'status': {'required': True},
        }
    
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q,Value,F
from django.db.models.functions import Concat,Coalesce
from ..serializers.presentation import PresentationSearchSerializer

class ProductSearchView(ListAPIView):
    serializer_class = PresentationSearchSerializer
    #permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        query = self.request.query_params.get('q', '').strip()
        if not query:
            return self.serializer_class.Meta.model.objects.none()
        return self.serializer_class.Meta.model.objects.annotate(
            search_text=Concat(
                Coalesce(F('product__name'), Value('')),
                Value(' '),
                Coalesce(F('name'), Value('')),
            )
        ).filter(
                Q(search_text__icontains=query) |
                Q(sku__icontains=query) |
                Q(bar_code__icontains=query)|
                Q(name__icontains=query) |
                Q(product__name__icontains=query)
                )
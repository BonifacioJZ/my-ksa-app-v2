from rest_framework import  status,generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from ..models.sale import Sale
from ..serializers.sale import SaleCreateListSerializer,SaleDetailsSerializer

class SaleListCreateView(generics.ListCreateAPIView):
    """
    Sale List and Create View
    """
    permission_classes = [IsAuthenticated]
    serializer_class = SaleCreateListSerializer
    queryset = Sale.objects.all()
    
    def get(self, request, *args, **kwargs):
        """
        Get all sales
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SaleRetrieveView(generics.RetrieveAPIView):
    """
    Sale Retrieve, Update and Destroy View
    """
    permission_classes = [IsAuthenticated]
    serializer_class = SaleDetailsSerializer
    queryset = Sale.objects.all().prefetch_related()
    lookup_field = 'folio'
    
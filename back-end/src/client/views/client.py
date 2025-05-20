from rest_framework import generics
from ..models.client import Client
from ..serializers.client import ClientCreateListSerializer, ClientDetailSerializer, ClientUpdateSerializer, ClientDeleteSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


class ClientListCreateView(generics.ListCreateAPIView):
    """
    Vista API para listar y crear instancias de Client.
    Permite a los usuarios autenticados crear nuevos clientes y a cualquier usuario ver la lista de clientes.
    """
    queryset = Client.objects.all()
    serializer_class = ClientCreateListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]  # Permite lectura a todos y escritura solo a autenticados

class ClientRetrieveView(generics.RetrieveAPIView):
    """
    Vista API para recuperar una instancia específica de Client.
    Solo requiere autenticación para operaciones de escritura, pero la lectura está permitida para todos.
    """
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    lookup_field = 'slug'

class ClientUpdateView(generics.UpdateAPIView):
    """
    Vista API para actualizar una instancia existente de Client.
    Solo los usuarios autenticados pueden actualizar la información de un cliente.
    """
    permission_classes = [IsAuthenticated,]
    queryset = Client.objects.all()
    serializer_class = ClientUpdateSerializer
    lookup_field = 'slug'

class ClientDeleteView(generics.DestroyAPIView):
    """
    Vista API para eliminar una instancia de Client.
    Solo los usuarios autenticados pueden eliminar clientes.
    Al eliminar, retorna un mensaje personalizado con el nombre del cliente eliminado.
    """
    permission_classes = [IsAuthenticated,]
    queryset = Client.objects.all()
    serializer_class = ClientDeleteSerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"detail": f"Cliente '{instance.name}' eliminado correctamente."},
            status=status.HTTP_200_OK
        )

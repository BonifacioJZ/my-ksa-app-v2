from rest_framework.generics import ListCreateAPIView,RetrieveAPIView, UpdateAPIView, DestroyAPIView
from ..serializers.presentation import PresentationListSerializer,PresentationDetailSerializer,PresentationUpdateSerializer,PresentationDeleteSerializer
from rest_framework.response import Response
from rest_framework import status

class PresentationCreateListView(ListCreateAPIView):
    """
    PresentationCreateListView es una vista que proporciona funcionalidad para listar
    y crear presentaciones.

    Atributos:
        serializer_class (Serializer): Especifica el serializador que se utilizará
            para serializar y deserializar los datos de las presentaciones.
        queryset (QuerySet): Define el conjunto de consultas que contiene todos los
            objetos de presentación que se recuperarán y listarán.
    """
    serializer_class = PresentationListSerializer
    queryset = PresentationListSerializer.Meta.model.objects.select_related().all()
    
class PresentationRetrieveView(RetrieveAPIView):
    """
    PresentationRetrieveView es una vista que proporciona funcionalidad para recuperar
    los detalles de una presentación específica.

    Atributos:
        serializer_class (Serializer): Especifica el serializador que se utilizará
            para serializar y deserializar los datos de la presentación.
        queryset (QuerySet): Define el conjunto de consultas que contiene todos los
            objetos de presentación que se recuperarán y listarán.
        lookup_field (str): Especifica el campo que se utilizará para buscar la
            presentación. En este caso, se utiliza 'slug' como campo de búsqueda.
    """
    serializer_class = PresentationDetailSerializer
    queryset = PresentationDetailSerializer.Meta.model.objects.select_related().all()
    lookup_field = 'slug'  # Campo utilizado para buscar la presentación (por defecto es 'pk')
    # permission_classes = [IsAuthenticated]  # Configurar según los requisitos de acceso
    
class PresentationUpdateView(UpdateAPIView):
    """
    PresentationUpdateView es una vista que proporciona funcionalidad para actualizar
    los detalles de una presentación específica.

    Atributos:
        serializer_class (Serializer): Especifica el serializador que se utilizará
            para serializar y deserializar los datos de la presentación.
        queryset (QuerySet): Define el conjunto de consultas que contiene todos los
            objetos de presentación que se recuperarán y listarán.
        lookup_field (str): Especifica el campo que se utilizará para buscar la
            presentación. En este caso, se utiliza 'slug' como campo de búsqueda.
    """
    serializer_class = PresentationUpdateSerializer
    queryset = PresentationUpdateSerializer.Meta.model.objects.select_related().all()
    lookup_field = 'slug'  # Campo utilizado para buscar la presentación (por defecto es 'pk')
    # permission_classes = [IsAuthenticated]  # Configurar según los requisitos de acceso

class PresentationDeleteView(DestroyAPIView):
    """
    PresentationDeleteView es una vista que proporciona funcionalidad para eliminar
    una presentación específica.

    Atributos:
        serializer_class (Serializer): Especifica el serializador que se utilizará
            para serializar y deserializar los datos de la presentación.
        queryset (QuerySet): Define el conjunto de consultas que contiene todos los
            objetos de presentación que se recuperarán y listarán.
        lookup_field (str): Especifica el campo que se utilizará para buscar la
            presentación. En este caso, se utiliza 'slug' como campo de búsqueda.
    """
    serializer_class = PresentationDeleteSerializer
    queryset = PresentationDeleteSerializer.Meta.model.objects.select_related().all()
    lookup_field = 'pk'  # Campo utilizado para buscar la presentación (por defecto es 'pk')
    # permission_classes = [IsAuthenticated]  # Configurar según los requisitos de acceso
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"detail": f"Marca '{instance.name}' eliminada correctamente."},
            status=status.HTTP_200_OK
        )
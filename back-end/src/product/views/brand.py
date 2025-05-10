from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.brand import BrandCreateSerializer, BrandDetailSerializer, BrandUpdateSerializer, BrandDeleteSerializer


class BrandListCreateView(ListCreateAPIView):
    """
    Vista basada en clases que permite listar y crear instancias del modelo 'Brand'.

    Atributos:
        serializer_class (Serializer): Define el serializador que se utilizará para 
            validar y transformar los datos de entrada y salida.
        queryset (QuerySet): Especifica el conjunto de datos que se utilizará para 
            las operaciones de listado y creación.
        permission_classes (list): (Opcional) Especifica los permisos requeridos
            para acceder a esta vista. Descomentar y configurar según sea necesario.
    """
    serializer_class = BrandCreateSerializer
    queryset = BrandCreateSerializer.Meta.model.objects.all()
    # permission_classes = [IsAuthenticated,]


class BrandRetrieveApiView(RetrieveAPIView):
    """
    Vista basada en clases que permite obtener los detalles de una instancia del modelo 'Brand'.

    Esta vista permite recuperar información detallada sobre un único objeto 'Brand'
    utilizando su identificador único 'slug'.

    Atributos:
        serializer_class (Serializer): Define el serializador que se utilizará para
            validar y transformar los datos de entrada y salida.
        queryset (QuerySet): Especifica el conjunto de datos que se utilizará para
            las operaciones de recuperación, con datos relacionados precargados para optimización.
        lookup_field (str): El campo utilizado para buscar la instancia de 'Brand'.
            Por defecto es 'slug'.
        permission_classes (list): (Opcional) Especifica los permisos requeridos
            para acceder a esta vista. Descomentar y configurar según sea necesario.
    """
    serializer_class = BrandDetailSerializer
    queryset = BrandDetailSerializer.Meta.model.objects.all().prefetch_related()
    lookup_field = 'slug'  # Campo utilizado para buscar la categoría (por defecto es 'pk')
    # permission_classes = [IsAuthenticated,]


class BrandUpdateApiView(UpdateAPIView):
    """
    Vista basada en clases que permite actualizar una instancia del modelo 'Brand'.

    Esta vista permite modificar los datos de un único objeto 'Brand' utilizando su identificador único 'slug'.

    Atributos:
        serializer_class (Serializer): Define el serializador que se utilizará para
            validar y transformar los datos de entrada y salida.
        queryset (QuerySet): Especifica el conjunto de datos que se utilizará para
            las operaciones de actualización.
        lookup_field (str): El campo utilizado para buscar la instancia de 'Brand'.
            Por defecto es 'slug'.
        permission_classes (list): (Opcional) Especifica los permisos requeridos
            para acceder a esta vista. Descomentar y configurar según sea necesario.
    """
    serializer_class = BrandUpdateSerializer
    queryset = BrandUpdateSerializer.Meta.model.objects.all()
    lookup_field = 'slug'
    # permission_classes = [IsAuthenticated, IsAdminUser,]


class BrandDeleteApiView(DestroyAPIView):
    """
    Vista basada en clases que permite eliminar una instancia del modelo 'Brand'.

    Esta vista permite eliminar un único objeto 'Brand' utilizando su identificador único 'pk'.

    Atributos:
        serializer_class (Serializer): Define el serializador que se utilizará para
            validar y transformar los datos de entrada y salida.
        queryset (QuerySet): Especifica el conjunto de datos que se utilizará para
            las operaciones de eliminación.
        lookup_field (str): El campo utilizado para buscar la instancia de 'Brand'.
            Por defecto es 'pk'.
        permission_classes (list): (Opcional) Especifica los permisos requeridos
            para acceder a esta vista. Descomentar y configurar según sea necesario.
    """
    serializer_class = BrandDeleteSerializer
    queryset = BrandDeleteSerializer.Meta.model.objects.all()
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticated, IsAdminUser,]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"detail": f"Marca '{instance.name}' eliminada correctamente."},
            status=status.HTTP_200_OK
        )

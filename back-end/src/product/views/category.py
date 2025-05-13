from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from ..serializers.category import CategoryListCreateSerializer,CategoryDetailSerializer,CategoryUpdateSerializer,CategoryDeleteSerializer
from rest_framework.response import Response
from rest_framework import status

class CategoryListCreateView(ListCreateAPIView):
    """
    Vista genérica para listar y crear categorías.

    Esta clase utiliza `ListCreateAPIView` de Django REST Framework, 
    lo que permite manejar solicitudes GET para obtener una lista de categorías 
    y solicitudes POST para crear nuevas categorías.

    Atributos:
        serializer_class (Serializer): Define el serializador que se utiliza 
            para validar y transformar los datos de entrada y salida. En este caso, 
            se utiliza `CategoryListCreateSerializer`, que debe estar definido en 
            el módulo `serializers.category`.

        queryset (QuerySet): Especifica el conjunto de datos que se utilizará 
            para las operaciones de la vista. Se obtiene del modelo asociado al 
            serializador (`CategoryListCreateSerializer.Meta.model`) y recupera 
            todos los objetos de ese modelo.

    Notas:
        - La clase `permission_classes` está comentada. Si se requiere control 
          de acceso, se debe descomentar y configurar con una clase de permisos 
          adecuada, como `IsAuthenticated` para restringir el acceso a usuarios autenticados.
    """
    permission_classes = [IsAuthenticatedOrReadOnly,]  # Configurar según los requisitos de acceso
    serializer_class = CategoryListCreateSerializer  # Serializador para manejar los datos
    queryset = CategoryListCreateSerializer.Meta.model.objects.select_related().all()  # Conjunto de datos

class CategoryRetrieveView(RetrieveAPIView):
    """
    Vista genérica para recuperar detalles de una categoría específica.

    Esta clase utiliza `RetrieveAPIView` de Django REST Framework, lo que permite 
    manejar solicitudes GET para obtener los detalles de una categoría específica 
    identificada por su Slug.

    Atributos:
        serializer_class (Serializer): Define el serializador que se utiliza 
            para validar y transformar los datos de salida. En este caso, 
            se utiliza `CategoryDetailSerializer`, que debe estar definido en 
            el módulo `serializers.category`.

        queryset (QuerySet): Especifica el conjunto de datos que se utilizará 
            para las operaciones de la vista. Se obtiene del modelo asociado al 
            serializador (`CategoryDetailSerializer.Meta.model`) y recupera 
            todos los objetos de ese modelo.
    Notas:
        - La clase `permission_classes` está comentada. Si se requiere control 
          de acceso, se debe descomentar y configurar con una clase de permisos 
          adecuada, como `IsAuthenticated` para restringir el acceso a usuarios autenticados.
    """
    permission_classes = [IsAuthenticatedOrReadOnly,]  # Configurar según los requisitos de acceso
    serializer_class = CategoryDetailSerializer  # Serializador para manejar los datos
    queryset = CategoryDetailSerializer.Meta.model.objects.all().prefetch_related()  # Conjunto de datos
    lookup_field = 'slug'  # Campo utilizado para buscar la categoría (por defecto es 'pk')

class CategoryUpdateView(UpdateAPIView):
    """
    Vista genérica para actualizar una categoría existente.

    Esta clase utiliza `UpdateAPIView` de Django REST Framework, lo que permite 
    manejar solicitudes PUT y PATCH para actualizar los detalles de una categoría 
    específica identificada por su Slug.

    Atributos:
        serializer_class (Serializer): Define el serializador que se utiliza 
            para validar y transformar los datos de entrada. En este caso, 
            se utiliza `CategoryUpdateSerializer`, que debe estar definido en 
            el módulo `serializers.category`.

        queryset (QuerySet): Especifica el conjunto de datos que se utilizará 
            para las operaciones de la vista. Se obtiene del modelo asociado al 
            serializador (`CategoryUpdateSerializer.Meta.model`) y recupera 
            todos los objetos de ese modelo.
    Notas:
        - La clase `permission_classes` está comentada. Si se requiere control 
          de acceso, se debe descomentar y configurar con una clase de permisos 
          adecuada, como `IsAuthenticated` para restringir el acceso a usuarios autenticados.
    """
    # permission_classes = [IsAuthenticated]  # Configurar según los requisitos de acceso
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = CategoryUpdateSerializer  # Serializador para manejar los datos
    queryset = CategoryUpdateSerializer.Meta.model.objects.all()  # Conjunto de datos
    lookup_field = 'slug'  # Campo utilizado para buscar la categoría (por defecto es 'pk')

class CategoryDeleteView(DestroyAPIView):
    """
    Vista genérica para eliminar una categoría existente.

    Esta clase utiliza `DestroyAPIView` de Django REST Framework, lo que permite
    manejar solicitudes DELETE para eliminar una categoría específica identificada por su Slug.

    Atributos:
        queryset (QuerySet): Especifica el conjunto de datos que se utilizará
            para las operaciones de la vista. Se obtiene del modelo asociado al
            serializador (`CategoryUpdateSerializer.Meta.model`) y recupera
            todos los objetos de ese modelo.
    Notas:
        - La clase `permission_classes` está comentada. Si se requiere control
          de acceso, se debe descomentar y configurar con una clase de permisos
          adecuada, como `IsAuthenticated` para restringir el acceso a usuarios autenticados.
    """
    # permission_classes = [IsAuthenticated, IsAdminUser]  # Configurar según los requisitos de acceso
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = CategoryDeleteSerializer  # Serializador para manejar los datos
    queryset = CategoryUpdateSerializer.Meta.model.objects.all()  # Conjunto de datos
    lookup_field = 'pk'  # Campo utilizado para buscar la categoría (por defecto es 'pk')
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"detail": f"Marca '{instance.name}' eliminada correctamente."},
            status=status.HTTP_200_OK
        )
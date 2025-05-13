from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from ..serializers.product import ProductListCreateSerializer,ProductDetailSerializer, ProductUpdateSerializer,ProductDeleteSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


class ProductListCreateView(ListCreateAPIView):
    """
    Vista genérica para listar y crear productos.

    Esta clase utiliza `ListCreateAPIView` de Django REST Framework, 
    lo que permite manejar solicitudes GET para obtener una lista de productos 
    y solicitudes POST para crear nuevos productos.

    Atributos:
        serializer_class (Serializer): Define el serializador que se utiliza 
            para validar y transformar los datos de entrada y salida. En este caso, 
            se utiliza `ProductListCreateSerializer`, que debe estar definido en 
            el módulo `serializers.product`.

        queryset (QuerySet): Especifica el conjunto de datos que se utilizará 
            para las operaciones de la vista. Se obtiene del modelo asociado al 
            serializador (`ProductListCreateSerializer.Meta.model`) y recupera 
            todos los objetos de ese modelo.

    Notas:
        - La clase `permission_classes` está comentada. Si se requiere control 
          de acceso, se debe descomentar y configurar con una clase de permisos 
          adecuada, como `IsAuthenticated` para restringir el acceso a usuarios autenticados.
    """
    permission_classes = [IsAuthenticatedOrReadOnly,]  # Configurar según los requisitos de acceso
    serializer_class = ProductListCreateSerializer  # Serializador para manejar los datos
    queryset = ProductListCreateSerializer.Meta.model.objects.select_related().all().prefetch_related() # Conjunto de datos

class ProductDetailView(RetrieveAPIView):
    """
    Vista genérica para recuperar detalles de un producto específico.

    Esta clase utiliza `RetrieveAPIView` de Django REST Framework, lo que permite
    manejar solicitudes GET para obtener los detalles de un producto específico
    identificada por su Slug.

    Atributos:
        serializer_class (Serializer): Define el serializador que se utiliza
            para validar y transformar los datos de salida. En este caso,
            se utiliza `ProductDetailSerializer`, que debe estar definido en
            el módulo `serializers.product`.

        queryset (QuerySet): Especifica el conjunto de datos que se utilizará
            para las operaciones de la vista. Se obtiene del modelo asociado al
            serializador (`ProductDetailSerializer.Meta.model`) y recupera
            todos los objetos de ese modelo.
    Notas:
        - La clase `permission_classes` está comentada. Si se requiere control
          de acceso, se debe descomentar y configurar con una clase de permisos
          adecuada, como `IsAuthenticated` para restringir el acceso a usuarios autenticados.
    """
    permission_classes = [IsAuthenticatedOrReadOnly,]  # Configurar según los requisitos de acceso
    serializer_class = ProductDetailSerializer  # Serializador para manejar los datos
    queryset = ProductDetailSerializer.Meta.model.objects.select_related().all() # Conjunto de datos
    lookup_field = 'slug'  # Campo utilizado para identificar el producto

class ProductUpdateView(UpdateAPIView):
    """
    Vista genérica para actualizar un producto específico.

    Esta clase utiliza `UpdateAPIView` de Django REST Framework, lo que permite
    manejar solicitudes PUT y PATCH para actualizar los detalles de un producto
    específico identificado por su Slug.

    Atributos:
        serializer_class (Serializer): Define el serializador que se utiliza
            para validar y transformar los datos de entrada. En este caso,
            se utiliza `ProductUpdateSerializer`, que debe estar definido en
            el módulo `serializers.product`.

        queryset (QuerySet): Especifica el conjunto de datos que se utilizará
            para las operaciones de la vista. Se obtiene del modelo asociado al
            serializador (`ProductUpdateSerializer.Meta.model`) y recupera
            todos los objetos de ese modelo.
    Notas:
        - La clase `permission_classes` está comentada. Si se requiere control
          de acceso, se debe descomentar y configurar con una clase de permisos
          adecuada, como `IsAuthenticated` para restringir el acceso a usuarios autenticados.
    """
    permission_classes = [IsAuthenticatedOrReadOnly,]  # Configurar según los requisitos de acceso
    serializer_class = ProductUpdateSerializer  # Serializador para manejar los datos
    queryset = ProductUpdateSerializer.Meta.model.objects.select_related().all() # Conjunto de datos
    lookup_field = 'slug'  # Campo utilizado para identificar el producto


class ProductDeleteView(DestroyAPIView):
    """
    Vista genérica para eliminar un producto específico.

    Esta clase utiliza `DestroyAPIView` de Django REST Framework, lo que permite
    manejar solicitudes DELETE para eliminar un producto específico identificado
    por su Slug.

    Atributos:
        serializer_class (Serializer): Define el serializador que se utiliza
            para validar y transformar los datos de entrada. En este caso,
            se utiliza `ProductDeleteSerializer`, que debe estar definido en
            el módulo `serializers.product`.

        queryset (QuerySet): Especifica el conjunto de datos que se utilizará
            para las operaciones de la vista. Se obtiene del modelo asociado al
            serializador (`ProductDeleteSerializer.Meta.model`) y recupera
            todos los objetos de ese modelo.
    Notas:
        - La clase `permission_classes` está comentada. Si se requiere control
          de acceso, se debe descomentar y configurar con una clase de permisos
          adecuada, como `IsAuthenticated` para restringir el acceso a usuarios autenticados.
    """
    permission_classes = [IsAuthenticatedOrReadOnly,]  # Configurar según los requisitos de acceso
    serializer_class = ProductDeleteSerializer  # Serializador para manejar los datos
    queryset = ProductDeleteSerializer.Meta.model.objects.select_related().all() # Conjunto de datos
    lookup_field = 'pk'  # Campo utilizado para identificar el producto
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"detail": f"Marca '{instance.name}' eliminada correctamente."},
            status=status.HTTP_200_OK
        )
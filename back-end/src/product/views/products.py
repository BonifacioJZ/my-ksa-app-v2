from rest_framework.generics import ListCreateAPIView
from ..serializers.product import ProductListCreateSerializer

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
    #permission_classes = []  # Configurar según los requisitos de acceso
    serializer_class = ProductListCreateSerializer  # Serializador para manejar los datos
    queryset = ProductListCreateSerializer.Meta.model.objects.select_related().all() # Conjunto de datos
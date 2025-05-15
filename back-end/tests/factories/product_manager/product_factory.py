from src.product.models.product import Product
from tests.factories.category_manager.category_factory import CategoryFactory
from tests.factories.brand_manager.brand_factory import BrandFactory

class ProductFactory:
    def build_product(self):
        """
        Método para construir un producto.
        """
        return Product.objects.create(
            name="Product Name",
            description="Product Description",
            category=CategoryFactory().build_category(),
            brand=BrandFactory().build_brand(),
        )
    def build_product_JSON(self):
        """
        Método para construir un JSON de producto.
        """
        return {
            "name": "Product Name",
            "description": "Product Description",
            "category": CategoryFactory().build_category().id,
            "brand": BrandFactory().build_brand().id,
        }
    def build_product_invalid(self):
        """
        Método para construir un producto inválido.
        """
        return {
            "name": "",
            "description": "Product Description",
            "category": CategoryFactory().build_category().id,
            "brand": BrandFactory().build_brand().id,
        }
    def build_product_invalid_category(self):
        """
        Método para construir un producto inválido con categoría inválida.
        """
        return {
            "name": "Product Name",
            "description": "Product Description",
            "category": "invalid-category",
            "brand": "invalid-brand",
        }
    def build_product_invalid_brand(self):
        """
        Método para construir un producto inválido con marca inválida.
        """
        return {
            "name": "Product Name",
            "description": "Product Description",
            "category": CategoryFactory().build_category().id,
            "brand": "invalid-brand",
        }
    def build_product_invalid_price(self):
        """
        Método para construir un producto inválido con precio inválido.
        """
        return {
            "name": "Product Name",
            "description": "Product Description",
            "category": CategoryFactory().build_category().id,
            "brand": BrandFactory().build_brand().id,
        }
from src.product.models.presentation import Presentation
from tests.factories.product_manager.product_factory import ProductFactory

class PresentationFactory:
    def build_presentation(self):
        """
        Método para construir una presentación.
        """
        return Presentation.objects.create(
            product=ProductFactory().build_product(),
            name="Presentation Name",
            price=100.0,
            stock=10,
            sku="SKU123",
            bar_code="1234567890123",
            abbreviation="ch",
        )
    
    def build_presentation_JSON(self):
        """
        Método para construir un JSON de presentación.
        """
        return {
            "product": ProductFactory().build_product().id,
            "name": "Presentation Name",
            "price": 100.0,
            "stock": 10,
            "sku": "SKU123",
            "bar_code": "1234567890123",
            "abbreviation": "ch",
        }
    def build_presentation_invalid(self):
        """
        Método para construir una presentación inválida.
        """
        return {
            "product": ProductFactory().build_product().id,
            "name": "",
            "price": 100.0,
            "stock": 10,
            "sku": "SKU123",
            "bar_code": "1234567890123",
            "abbreviation": "ch",
        }
    def build_presentation_invalid_product(self):
        """
        Método para construir una presentación inválida con producto inválido.
        """
        return {
            "product": "invalid-product",
            "name": "Presentation Name",
            "price": 100.0,
            "stock": 10,
            "sku": "SKU123",
            "bar_code": "1234567890123",
            "abbreviation": "ch",
        }
    def build_presentation_invalid_price(self):
        """
        Método para construir una presentación inválida con precio inválido.
        """
        return {
            "product": ProductFactory().build_product().id,
            "name": "Presentation Name",
            "price": -100.0,
            "stock": 10,
            "sku": "SKU123",
            "bar_code": "1234567890123",
            "abbreviation": "ch",
        }
    def build_presentation_invalid_stock(self):
        """
        Método para construir una presentación inválida con stock inválido.
        """
        return {
            "product": ProductFactory().build_product().id,
            "name": "Presentation Name",
            "price": 100.0,
            "stock": -10,
            "sku": "SKU123",
            "bar_code": "1234567890123",
            "abbreviation": "ch",
        }
    def build_presentation_invalid_sku(self):
        """
        Método para construir una presentación inválida con SKU inválido.
        """ 
        return {
            "product": ProductFactory().build_product().id,
            "name": "Presentation Name",
            "price": 100.0,
            "stock": 10,
            "sku": "",
            "bar_code": "1234567890123",
            "abbreviation": "ch",
        }
    def build_presentation_invalid_barcode(self):
        """
        Método para construir una presentación inválida con código de barras inválido.
        """
        return {
            "product": ProductFactory().build_product().id,
            "name": "Presentation Name",
            "price": 100.0,
            "stock": 10,
            "sku": "SKU123",
            "bar_code": "",
            "abbreviation": "ch",
        }
    def build_presentation_invalid_abbreviation(self):
        """
        Método para construir una presentación inválida con abreviatura inválida.
        """
        return {
            "product": ProductFactory().build_product().id,
            "name": "Presentation Name",
            "price": 100.0,
            "stock": 10,
            "sku": "SKU123",
            "bar_code": "1234567890123",
            "abbreviation": "",
        }
    def build_presentation_invalid_sku_length(self):
        """
        Método para construir una presentación inválida con SKU de longitud inválida.
        """
        return {
            "product": ProductFactory().build_product().id,
            "name": "Presentation Name",
            "price": 100.0,
            "stock": 10,
            "sku": "SKU12345678901234567890",
            "bar_code": "1234567890123",
            "abbreviation": "ch",
        }
    def build_presentation_invalid_barcode_length(self):
        """
        Método para construir una presentación inválida con código de barras de longitud inválida.
        """
        return {
            "product": ProductFactory().build_product().id,
            "name": "Presentation Name",
            "price": 100.0,
            "stock": 10,
            "sku": "SKU123",
            "bar_code": "123456789012345678901234567890",
            "abbreviation": "ch",
        }
    def build_presentation_invalid_abbreviation_length(self):
        """
        Método para construir una presentación inválida con abreviatura de longitud inválida.
        """
        return {
            "product": ProductFactory().build_product().id,
            "name": "Presentation Name",
            "price": 100.0,
            "stock": 10,
            "sku": "SKU123",
            "bar_code": "1234567890123",
            "abbreviation": "ch" * 20,
        }
    def build_presentation_invalid_product_not_exist(self):
        """
        Método para construir una presentación inválida con producto que no existe.
        """
        return {
            "product": "invalid-product",
            "name": "Presentation Name",
            "price": 100.0,
            "stock": 10,
            "sku": "SKU123",
            "bar_code": "1234567890123",
            "abbreviation": "ch",
        }
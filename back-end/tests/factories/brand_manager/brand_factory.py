from src.product.models.brand import Brand

class BrandFactory:
    def build_brand_JSON(self):
        """
        Método para construir un JSON de marca.
        """
        return {
            "name": "Brand Name",
        }
    def build_brand(self):
        """
        Método para construir una marca.
        """
        return Brand.objects.create(**self.build_brand_JSON())
        
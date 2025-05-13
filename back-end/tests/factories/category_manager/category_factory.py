from src.product.models.category import Category

class CategoryFactory:
    def build_category_JSON(self):
        """
        Método para construir un JSON de categoría.
        """
        return {
            "name": "Category Name",
            "description": "Category Description",
        }
    
    def build_category(self):
        """
        Método para construir una categoría.
        """
        return Category.objects.create(**self.build_category_JSON())
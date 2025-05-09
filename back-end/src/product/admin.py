from django.contrib import admin
from .models import product, category, brand, presentation
# Register your models here.
admin.site.register(brand.Brand)
admin.site.register(category.Category)
admin.site.register(presentation.Presentation)
admin.site.register(product.Product)


from django.contrib import admin
from .models.sale import Sale, SaleDetail
# Register your models here.

admin.site.register(Sale)
admin.site.register(SaleDetail)

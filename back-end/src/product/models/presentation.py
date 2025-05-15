from django.db import models
import uuid
from .product import Product
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.validators import MinValueValidator
from decimal import Decimal

class Presentation(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(verbose_name="Nombre",max_length=250,blank=False,null=False)
    sku= models.CharField(verbose_name="SKU", unique=True,max_length=8,blank=False,null=False)
    bar_code= models.CharField(verbose_name="Codigo de Barras",max_length=13,blank=False,null=False)
    stock = models.IntegerField(verbose_name="Stock")
    price = models.DecimalField(verbose_name="Precio",max_digits=10,decimal_places=2,validators=[MinValueValidator(Decimal('0.00'))],blank=False,null=False)
    product = models.ForeignKey(Product,verbose_name="Productos",related_name="products",on_delete=models.CASCADE)
    abbreviation = models.CharField(verbose_name="Abreviatura",max_length=50,blank=False,null=False)
    slug = models.SlugField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    class Meta:
        verbose_name = "presentation"
        verbose_name_plural = "presentations"

    def __str__(self):
        return self.name


def create_presentation_slug(sender,instance:Presentation,*args, **kwargs):
    if instance.slug:
        return
    
    id = str(uuid.uuid4())
    instance.slug = slugify('{}-{}'.format(
        instance.name.upper().strip(),id[:8]
    ))
pre_save.connect(create_presentation_slug,sender=Presentation)
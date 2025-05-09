from django.db import models
import uuid
from django.utils.text import slugify
from .brand import Brand
from .category import Category
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(verbose_name="Nombre",max_length=250,blank=False,null=False)
    description = models.TextField(verbose_name="Descripcion",null=True,blank=True)
    category = models.ForeignKey(Category,verbose_name="Categoria",related_name="category",on_delete=models.CASCADE)
    slug = models.SlugField(null=True,blank=True)
    brand = models.ForeignKey(Brand,verbose_name="Marca",related_name="brand",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

def create_product_slug(sender,instance:Product,*args, **kwargs):
    if instance.slug:
        return
    
    id = str(uuid.uuid4())
    instance.slug = slugify('{}-{}'.format(
        instance.name.upper().strip(),id[:8]
    ))

pre_save.connect(create_product_slug,sender=Product)
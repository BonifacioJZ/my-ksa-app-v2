from django.db import models
import uuid
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.

class Brand(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(verbose_name="Marca",max_length=250,blank=False,null=False)
    slug = models.SlugField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    class Meta:
        verbose_name = "brand"
        verbose_name_plural = "brands"

    def __str__(self):
        return self.name


def create_brand_slug(sender,instance:Brand,*args, **kwargs):
    if instance.slug:
        return
    
    id = str(uuid.uuid4())
    instance.slug = slugify('{}-{}'.format(
        instance.name.upper().strip(),id[:8]
        ))

pre_save.connect(create_brand_slug,sender=Brand)

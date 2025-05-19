import string
from django.db import models
import uuid
import random
from datetime import datetime
from django.db.models.signals import pre_save
from django.utils.text import slugify
from src.client.models.client import Client
from src.product.models.presentation import Presentation
from core import settings

class Sale(models.Model):
    CHOICES =[
        ('paid','Pagado'),
        ('pending','Pendiente'),
        ('canceled','Cancelado')
        ]
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    folio = models.CharField(max_length=20,unique=True,editable=False)
    client = models.ForeignKey(Client,related_name='client',on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    total= models.DecimalField(max_digits=10,decimal_places=2)
    pay = models.DecimalField(max_digits=10,decimal_places=2)
    change = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=20,choices=CHOICES,default='pending')
    seller = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='seller',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        managed = True
        verbose_name = 'sale'
        verbose_name_plural = 'sales'
    def __str__(self) -> str:
        return f"Sale {self.folio} - {self.client}"
    def save(self, *args, **kwargs):
        if not self.folio:
            date = datetime.now().strftime("%Y%m%d")
            rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            self.folio = f"{date}-{rand}"  # Formato 20240219-ABC12
        super().save(*args, **kwargs)

class SaleDetail(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    sale = models.ForeignKey(Sale,related_name='sale',on_delete=models.CASCADE) 
    presentation = models.ForeignKey(Presentation,related_name='sale_items',on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10,decimal_places=2)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        managed = True
        verbose_name = 'sale detail'
        verbose_name_plural = 'sale details'
    def __str__(self) -> str:
        return f"Sale Detail {self.id} - {self.sale.folio} - {self.presentation.name} - {self.presentation.product.name}" 
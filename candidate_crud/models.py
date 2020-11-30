from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Candidates(models.Model):
    address       = models.CharField(max_length=255, unique=True, verbose_name="Direccion")
    dni           = models.CharField(max_length=100, unique=True, verbose_name="DNI")
    telephone     = models.CharField(max_length=100, unique=True, verbose_name="Telefono")
    mobile        = models.CharField(max_length=100, unique=True, verbose_name="Movil")
    birth_date    = models.DateField(auto_now=False, auto_now_add=False)
    image         = models.ImageField(upload_to='portrait/%Y/%m/%d', null=True, blank=True, verbose_name='Logo de empresa')
    created_at    = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    # Retorna el contenido de esta clase en un string y devuelve el nombre
    def __str__(self):
        return self.address

    class Meta:
        db_table = 'provinces'
        abstract = True
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

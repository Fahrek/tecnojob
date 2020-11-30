from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Companies(models.Model):
    c_name        = models.CharField(max_length=255, unique=True, verbose_name="Nombre empresa")
    cif           = models.CharField(max_length=255, unique=True, verbose_name="CIF")
    email         = models.EmailField(max_length=255, verbose_name="Email")
    site          = models.URLField(max_length=255, verbose_name="Web")
    logo          = models.ImageField(upload_to='logos/%Y/%m/%d', null=True, blank=True, verbose_name='Logo de empresa')
    created_at    = models.DateTimeField(auto_now_add=True, verbose_name='Fecha alta')
    last_modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.c_name

    class Meta:
        db_table = 'companies'
        abstract = True
        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'
        ordering = ['id']

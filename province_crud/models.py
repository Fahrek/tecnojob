from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Provinces(models.Model):
    p_name        = models.CharField(max_length=255, unique=True, verbose_name="Nombre provincia")
    created_at    = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    # Retorna el contenido de esta clase en un string y devuelve el nombre
    def __str__(self):
        return self.city_name

    class Meta:
        db_table = 'provinces'
        abstract = True
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
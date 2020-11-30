from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cities(models.Model):
    city_name     = models.CharField(max_length=255, unique=True, verbose_name="Nombre ciudad")
    created_at    = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    # Foreign Key apuntando a la id de Provincias
    # prov_id = models.ForeignKey(Provinces, on_delete=models.CASCADE, null=True, blank=True)

    # Retorna el contenido de esta clase en un string y devuelve el nombre
    def __str__(self):
        return self.city_name

    class Meta:
        db_table = 'cities'
        abstract = True
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

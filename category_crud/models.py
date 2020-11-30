from django.db import models


# Create your models here. La PK la genera automaticamente Django con el uso de modelos
class Categoria(models.Model):
    name          = models.CharField(max_length=100, null=False, unique=True, verbose_name="Nombre")
    slug          = models.SlugField(max_length=255)
    created_at    = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    # Retorna el contenido de esta clase en un string y devuelve el nombre
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        abstract = True
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Offer(models.Model):
    title         = models.CharField(max_length=255, unique=True, verbose_name='Título')
    salary        = models.DecimalField(max_digits=8, decimal_places=2)
    sal_min       = models.DecimalField(max_digits=8, decimal_places=2)
    sal_max       = models.DecimalField(max_digits=8, decimal_places=2)
    description   = models.TextField(null=True, verbose_name='Contenido de la oferta')
    url           = models.URLField(max_length=255, verbose_name="URL")
    is_remote     = models.BooleanField(verbose_name="En remoto")
    image         = models.ImageField(upload_to='logos/%Y/%m/%d', null=True, blank=True, verbose_name='Logo de empresa')
    crt_type      = models.CharField(max_length=255, verbose_name='Tipo de contrato')
    crt_period    = models.CharField(max_length=255, verbose_name='Tipo de contrato')
    created_at    = models.DateTimeField(auto_now_add=True, verbose_name='Fecha alta')
    last_modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    # Foreign Keys apuntando a ID de Compañía y Categoría respectivamente
    # company  = models.ForeignKey(Companies, on_delete=models.CASCADE, null=True, blank=True)
    # category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'offers'
        abstract = True
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'
        ordering = ['id']

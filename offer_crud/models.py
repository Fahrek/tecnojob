from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Offer(models.Model):
    title         = models.CharField(max_lenght=255, unique=True, verbose_name='Título')
    salary        = models.DecimalField(max_digits=8, decimal_places=2)
    sal_min       = models.DecimalField(max_digits=8, decimal_places=2)
    sal_max       = models.DecimalField(max_digits=8, decimal_places=2)
    description   = models.TextField(null=True, verbose_name='Contenido de la oferta')
    image         = models.ImageField(upload_to='logos/%Y/%m/%d', null=True, blank=True, verbose_name='Logo de empresa')
    created_at    = models.DateTimeField(auto_now_add=True, verbose_name='Fecha alta')
    last_modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    # Foreign Keys
    # company  = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'offers'
        abstract = True
        verbose_name = 'oferta'
        verbose_name_plural = 'Ofertas'
        ordering = ['id']

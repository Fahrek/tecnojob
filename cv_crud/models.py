from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Curriculums(models.Model):
    work_exp      = models.TextField(verbose_name="Experiencia laboral")
    studies       = models.TextField(verbose_name="Estudios")
    lang          = models.CharField(max_length=255, verbose_name="Idiomas")
    skills        = models.CharField(max_length=255, verbose_name="Habilidades")
    knowledge     = models.CharField(max_length=255, verbose_name="Conocimientos")
    cv_others     = models.TextField(verbose_name="Otros")
    created_at    = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    # Foreign Key apuntando a la ID de candidato
    # candidate_id = models.ForeignKey(Candidates, on_delete=models.CASCADE, null=True, blank=True)

    # Retorna el contenido de esta clase en un string y devuelve el nombre
    def __str__(self):
        return self.work_exp

    class Meta:
        db_table = 'curriculums'
        abstract = True
        verbose_name = 'CV'
        verbose_name_plural = "CV's"
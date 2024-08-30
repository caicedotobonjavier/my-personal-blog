from django.db import models
#
from model_utils.models import TimeStampedModel
#
from ckeditor.fields import RichTextField
#
from django.conf import settings
# Create your models here.

class Category(TimeStampedModel):
    name = models.CharField('Nombre Categoria', max_length=50, unique=True)
    short_name = models.CharField('Nombre Corto', max_length=5, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']
        unique_together = ['name', 'short_name']


    def __str__(self):
        return self.name


class Entry(TimeStampedModel):
    category = models.ForeignKey(Category, related_name='entry_category', on_delete=models.CASCADE)
    title = models.CharField('Titulo', max_length=50)
    resumen = models.CharField('Resumen', max_length=50, blank=True, null=True)
    content = RichTextField('Contenido')
    imagen = models.ImageField('Imagen', upload_to='publicaciones', blank=True, null=True)
    active = models.BooleanField('Activo', default=True)
    in_home = models.BooleanField('En Home', default=False)
    portada = models.BooleanField('POrtada', default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='entry_user', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']
    

    def __str__(self):
        return self.title
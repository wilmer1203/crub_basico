from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.


class Articulo(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(upload_to='static/upload_images', verbose_name="Imagen", null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Autor")
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['-fecha_creacion']

    def __str__(self):          
        return self.titulo

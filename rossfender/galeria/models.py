from django.db import models

class Gallery(models.Model):
    tittle = models.CharField(max_length=50,verbose_name="Titulo")
    description =models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen",upload_to='cakes')
    date = models.DateField( auto_now_add=True,verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Galería"
        verbose_name_plural ="Pasteles"
        ordering = ["-date"]


def __str__(self):
    return self.tittle

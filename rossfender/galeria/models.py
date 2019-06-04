from django.db import models

class Gallery(models.Model):
    tittle = models.CharField(max_length=50)
    description =models.TextField()
    image = models.ImageField()
    date = models.DateField( auto_now_add=True)


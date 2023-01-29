from django.db import models

class Inicio (models.Model):
    texto = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='profile_images', null=True, blank=True)
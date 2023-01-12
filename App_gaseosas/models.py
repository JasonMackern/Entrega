from django.db import models

# Create your models here.
class Gaseosas (models.Model):
    nombre = models.CharField(max_length= 50, verbose_name = "nombre")
    precio = models.IntegerField(verbose_name = "precio")
    stock = models.BooleanField(default= True, verbose_name = "en stock")

    def __str__ (self):
        return self.nombre
    
    class Meta:
        verbose_name = "Gaseosa"
        verbose_name_plural = "Gaseosas"
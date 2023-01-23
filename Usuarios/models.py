from django.contrib.auth.models import User
from django.db import models

class Prefil_de_usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    telefono = models.CharField(max_length=25, null=True, blank=True)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    foto_de_perfil = models.ImageField(upload_to='profile_images', null=True, blank=True)
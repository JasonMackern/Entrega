from django.contrib import admin
from Usuarios.models import Prefil_de_usuario

@admin.register(Prefil_de_usuario)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('telefono', 'fecha_de_nacimiento')
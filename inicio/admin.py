from django.contrib import admin
from inicio.models import Inicio

@admin.register(Inicio)
class admin_inicio (admin.ModelAdmin):
    list_display = ("texto", "imagen")
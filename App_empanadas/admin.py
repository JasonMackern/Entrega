from django.contrib import admin

# Register your models here.
from App_empanadas.models import Empanadas

@admin.register(Empanadas)
class admin_empanadas (admin.ModelAdmin):
    list_display = ("nombre", "precio", "stock")
    list_filter = ("stock",)
    search_fields = ("nombre",)
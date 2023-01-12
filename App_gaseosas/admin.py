from django.contrib import admin

# Register your models here.
from App_gaseosas.models import Gaseosas

@admin.register(Gaseosas)
class admin_gaseosas (admin.ModelAdmin):
    list_display = ("nombre", "precio", "stock")
    list_filter = ("stock",)
    search_fields = ("nombre",)
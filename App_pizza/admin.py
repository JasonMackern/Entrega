from django.contrib import admin

# Register your models here.
from App_pizza.models import Pizzas

@admin.register(Pizzas)
class admin_pizzas (admin.ModelAdmin):
    list_display = ("nombre", "precio", "stock")
    list_filter = ("stock",)
    search_fields = ("nombre",)
# Generated by Django 4.1.4 on 2023-01-10 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_pizza', '0002_alter_pizzas_options_alter_pizzas_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzas',
            name='stock',
            field=models.BooleanField(default=True, verbose_name='en stock'),
        ),
    ]
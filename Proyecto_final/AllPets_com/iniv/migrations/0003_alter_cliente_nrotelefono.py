# Generated by Django 3.2.8 on 2022-06-17 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iniv', '0002_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nroTelefono',
            field=models.IntegerField(verbose_name='Telefono'),
        ),
    ]

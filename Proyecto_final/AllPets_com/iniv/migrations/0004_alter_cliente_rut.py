# Generated by Django 3.2.8 on 2022-06-17 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iniv', '0003_alter_cliente_nrotelefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rut',
            field=models.IntegerField(max_length=20, primary_key=True, serialize=False, verbose_name='Rut'),
        ),
    ]
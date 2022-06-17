# Generated by Django 4.0.5 on 2022-06-13 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID de Categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Codigo del  Producto')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre del Producto')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('imagen', models.ImageField(blank='True', null='True', upload_to='images/', verbose_name='Imagen del producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iniv.categoria', verbose_name='Categoria')),
            ],
        ),
    ]

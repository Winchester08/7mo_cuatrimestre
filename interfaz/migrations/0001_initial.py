# Generated by Django 4.2.7 on 2024-10-22 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Nombre x', max_length=30, verbose_name='Nombre Usuario')),
                ('usuario', models.CharField(max_length=30, verbose_name='Usuario')),
                ('clave', models.CharField(max_length=10, verbose_name='Clave')),
                ('tipo_usuario', models.CharField(max_length=20, verbose_name='Tipo Usuario')),
            ],
        ),
    ]
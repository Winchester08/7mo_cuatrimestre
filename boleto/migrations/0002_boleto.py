# Generated by Django 4.2.7 on 2024-10-23 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boleto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='boleto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre Usuario')),
                ('telefono', models.CharField(default='0000', max_length=10, verbose_name='Telefono')),
                ('num_boleto', models.CharField(max_length=10, verbose_name='Num Boleto')),
                ('origen', models.CharField(max_length=100, verbose_name='Origen')),
                ('destino', models.CharField(max_length=100, verbose_name='Destino')),
                ('fecha_salida', models.DateField(verbose_name='Fecha Salida')),
                ('fecha_llegada', models.DateField(verbose_name='Fecha Llegada')),
                ('hsalida', models.CharField(max_length=15, verbose_name='Hora salida')),
                ('hllegada', models.CharField(max_length=15, verbose_name='Hora llegada')),
            ],
        ),
    ]

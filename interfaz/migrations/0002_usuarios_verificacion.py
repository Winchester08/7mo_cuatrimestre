# Generated by Django 4.2.7 on 2024-10-22 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interfaz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='verificacion',
            field=models.CharField(default='1', max_length=2, verbose_name='Verificacion'),
        ),
    ]

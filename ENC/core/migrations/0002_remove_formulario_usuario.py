# Generated by Django 5.0.6 on 2024-07-07 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario',
            name='usuario',
        ),
    ]

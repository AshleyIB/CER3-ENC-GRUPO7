# Generated by Django 5.0.6 on 2024-07-07 16:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='fecha_modificacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produccion',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='producciones_modificadas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='operador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producciones_registradas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='LogCambiosRegistroProduccion',
        ),
    ]
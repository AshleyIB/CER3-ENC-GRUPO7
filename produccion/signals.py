from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType  # Importa ContentType aquí
from django.utils import timezone
from .models import Produccion

@receiver(pre_save, sender=Produccion)
def actualizar_campos_modificacion(sender, instance, **kwargs):
    
    if instance._state.adding or not instance.id:
        return 

    log_entry = LogEntry.objects.filter(
        object_id=instance.id,
        content_type_id=ContentType.objects.get_for_model(instance).pk,
        action_flag=CHANGE
    ).order_by('-action_time').first()

    if log_entry:
        instance.modificado_por = log_entry.user
        instance.fecha_modificacion = timezone.now()
    else:

        pass

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderPlaced
from .utils import send_whatsapp_message


@receiver(post_save, sender=OrderPlaced)
def order_status_change(sender, instance, created, **kwargs):
    if not created and instance.status == 'accepted':
        send_whatsapp_message(instance)

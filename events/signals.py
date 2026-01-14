from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models.signals import m2m_changed


from core.cache.invalidations import invalidate_event_cache
from django.db import transaction

from .models import Event

@receiver([post_save, post_delete], sender=Event)
def clear_event_cache(sender, **kwargs):
    transaction.on_commit(lambda: invalidate_event_cache())



@receiver(m2m_changed, sender=Event.participants.through)
def clear_event_cache_on_participants_change(sender, action, **kwargs):
    print(action)
    if action in ("post_add", "post_remove", "post_clear"):
        transaction.on_commit(lambda: invalidate_event_cache())

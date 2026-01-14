from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from core.cache.invalidations import invalidate_user_cache


from .models import User

@receiver([post_save, post_delete], sender=User)
def clear_user_cache(sender, **kwargs):
    invalidate_user_cache()

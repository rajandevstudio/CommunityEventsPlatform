from functools import wraps
from django.conf import settings
from django.core.cache import cache
import logging

from core.cache.utils import versioned_cache_key

logger = logging.getLogger(__name__)


def cache_get(namespace: str = None, timeout=settings.CACHE_TTL):
    """
    Versioned cache decorator for GET endpoints.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(self, request, *args, **kwargs):
            if request.method != "GET":
                return view_func(self, request, *args, **kwargs)

            # READ
            cache_key = versioned_cache_key(self, request, namespace)
            cached = cache.get(cache_key)

            if cached is not None:
                logger.info(f"Cache hit → {cache_key}")
                return cached

            logger.info(f"Cache miss → {cache_key}")

            # EXECUTE
            response = view_func(self, request, *args, **kwargs)

            # WRITE (re-resolve version)
            cache_key = versioned_cache_key(self, request, namespace)
            cache.set(cache_key, response, timeout)

            return response

        return _wrapped

    return decorator

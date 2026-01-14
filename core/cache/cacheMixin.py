from django.conf import settings
from django.core.cache import cache
from rest_framework.response import Response
import logging

from core.cache.utils import versioned_cache_key


logger = logging.getLogger(__name__)


class ListCacheMixin:
    """
    Reusable caching mixin for GET list APIs.
    Versioned + concurrency safe.
    """

    cache_timeout = settings.CACHE_TTL
    cache_namespace = None  # MUST be set in child view

    def list(self, request, *args, **kwargs):
        if request.method != "GET":
            return super().list(request, *args, **kwargs)

        # Read phase
        cache_key = versioned_cache_key(self, request, self.cache_namespace)
        cached = cache.get(cache_key)

        if cached is not None:
            logger.info(f"Cache hit → {cache_key}")
            return Response(cached)

        logger.info(f"Cache miss → {cache_key}")

        # DB work
        response = super().list(request, *args, **kwargs)

        # WRITE PHASE (re-resolve version)
        cache_key = versioned_cache_key(self, request, self.cache_namespace)
        cache.set(cache_key, response.data, timeout=self.cache_timeout)

        return response



from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)

DEFAULT_VERSION = 1
VERSION_PREFIX = "__version__"


def _version_key(namespace: str) -> str:
    return f"{VERSION_PREFIX}:{namespace}"


def get_cache_version(namespace: str) -> int:
    """
    Get current cache version for a namespace.
    """
    return cache.get(_version_key(namespace), DEFAULT_VERSION)


def bump_cache_version(namespace: str) -> int:
    """
    Atomically bump cache version.
    Monotonic and collision-free.
    """
    key = _version_key(namespace)

    # Initialize exactly once
    cache.add(key, DEFAULT_VERSION)

    # Atomic Redis INCR
    new_version = cache.incr(key)

    logger.info(f"Cache version bumped → {namespace}:v{new_version}")
    return new_version

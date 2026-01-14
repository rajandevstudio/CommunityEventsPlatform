import logging
from .versions import bump_cache_version

logger = logging.getLogger(__name__)

EVENT_CACHE = "events"
USER_CACHE = "users"


def invalidate_event_cache():
    logger.info("Invalidating event cache")
    bump_cache_version(EVENT_CACHE)


def invalidate_user_cache():
    logger.info("Invalidating user cache")
    bump_cache_version(USER_CACHE)

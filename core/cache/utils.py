from core.cache.versions import get_cache_version


def resolve_namespace(view_instance, explicit_namespace=None) -> str:
    """
    Resolve cache namespace:
    1. Explicit namespace
    2. View.cache_namespace
    3. View class name
    """
    if explicit_namespace:
        return explicit_namespace

    view_namespace = getattr(view_instance, "cache_namespace", None)
    if view_namespace:
        return view_namespace

    return view_instance.__class__.__name__.lower()


def versioned_cache_key(view_instance, request, namespace=None) -> str:
    """
    Always resolve version at call time (never cache it).
    """
    ns = resolve_namespace(view_instance, namespace)
    version = get_cache_version(ns)
    return f"{ns}:v{version}:{request.get_full_path()}"

from django.apps import AppConfig, apps
import importlib
import logging

logger = logging.getLogger(__name__)

class CoreConfig(AppConfig):
    name = "core"

    def ready(self):
        for app in apps.get_app_configs():
            try:
                importlib.import_module(f"{app.name}.signals")
                logger.info(f"{app.name} signals loaded")
            except ModuleNotFoundError:
                pass

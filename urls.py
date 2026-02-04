from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf.urls.static import static
from django.views.generic import RedirectView
import settings
ok = JsonResponse({"ok": True})
urlpatterns = [
    path('', RedirectView.as_view(url='/playground/login/', permanent=False)),
    path('ht/', lambda x: ok),
    path('admin/', admin.site.urls),
    path('api/', include('apis.urls')),
    path("playground/", include("frontend.urls")),
]



if settings.DEBUG:
    from drf_spectacular.views import (
            SpectacularAPIView,
            SpectacularSwaggerView
        )
    urlpatterns += [
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    ]

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT if hasattr(settings, "STATIC_ROOT") else None
    )
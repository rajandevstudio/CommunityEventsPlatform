from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

import settings
ok = JsonResponse({"ok": True})
urlpatterns = [
    path('ht/', lambda x: ok),
    path('', lambda x: ok),
    path('admin/', admin.site.urls),
    path('api/', include('apis.urls')),

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

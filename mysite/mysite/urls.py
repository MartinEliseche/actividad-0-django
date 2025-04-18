import debug_toolbar

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls))
    ]

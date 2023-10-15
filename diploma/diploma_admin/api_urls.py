from django.urls import path, include

from .api import me


urlpatterns = [
    path('me/', me),
    path('storage/', include('storage.urls')),
]

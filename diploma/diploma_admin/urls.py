from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from storage import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),
    path('api/', include('diploma_admin.api_urls')),
    path('login/', views.login),
    path('update_data/', views.update_data)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


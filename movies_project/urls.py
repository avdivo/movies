from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin  # Импортируем админку


urlpatterns = [
    path('admin/', admin.site.urls),  # Добавьте маршрут для админки
    path('', include('movies.urls')),  # Веб-маршруты
    path('api/', include('movies.urls_api')),  # API маршруты
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path,include
from django.conf import settings
from appimage import views
from django.conf.urls.static import static
app_name = 'appimage'
urlpatterns = [
    path('', views.post, name='index'),
]

if settings.DEBUG:  # Hanya untuk development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


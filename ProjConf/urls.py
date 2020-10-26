from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movie.views import  MovieHomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MovieHomeView.as_view(), name = "home"),
    path("movie/", include("movie.urls", namespace="movie"))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from games import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('game/', include('games.urls')),
    path('social/', include('publisher_creator.urls')),
    path(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
    path('accounts/', include('allauth.urls')), 
    path("__debug__/", include("debug_toolbar.urls")),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
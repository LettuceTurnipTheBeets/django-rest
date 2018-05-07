from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
]

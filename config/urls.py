from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls), 
    path('', include('hosts.urls')),
    path('hosts/', include('hosts.urls')),
]

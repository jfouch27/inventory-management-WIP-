from django.contrib import admin

from .models import Host, OpenPort


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    pass


@admin.register(OpenPort)
class OpenPortAdmin(admin.ModelAdmin):
    pass

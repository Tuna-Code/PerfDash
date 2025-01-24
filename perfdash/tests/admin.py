from django.contrib import admin

from .models import Host, Test, Location

# Register your models here.
#admin.site.register(Host)
#admin.site.register(Test)


class HostAdmin(admin.ModelAdmin):
    list_display = ('host_name', 'description')

admin.site.register(Host, HostAdmin)

class TestAdmin(admin.ModelAdmin):
    list_display = ('test_name', 'source_host', 'type', 'dest_host', 'duration' )
    list_filter = ('type', 'source_host', 'dest_host')

admin.site.register(Test, TestAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Location, LocationAdmin)

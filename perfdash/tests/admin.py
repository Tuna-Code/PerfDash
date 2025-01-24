from django.contrib import admin

from .models import Host, Test, Location

# Register your models here.
admin.site.register(Host)
admin.site.register(Test)
admin.site.register(Location)


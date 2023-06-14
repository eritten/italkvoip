from django.contrib import admin
from .models import Server

# Register your models here.

admin.site.register(Server)
admin.site.site_header = 'Italkvoip Administration'
admin.site.site_title = 'Italkvoip Administration'
        
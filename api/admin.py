from django.contrib import admin
from .models import Server

# Register your models here.
class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'ip', 'port', 'status', 'created_at', 'updated_at')
    list_filter = ('name', 'ip', 'port', 'status', 'created_at', 'updated_at')
    search_fields = ('name', 'url', 'ip', 'port', 'status', 'created_at', 'updated_at')
    ordering = ('name', 'ip', 'port', 'status', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Server Information', {
            'fields': ('name', 'url', 'ip', 'port', 'status', 'created_at', 'updated_at')
        }),
    )
admin.site.register(Server, ServerAdmin)
admin.site.site_header = 'Italkvoip Administration'
admin.site.site_title = 'Italkvoip Administration'
admin.site.index_title = 'Italkvoip Administration'
admin.site.site_url = '/italkvoip-admin'
        
from django.contrib import admin

from version.models import Version


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'version_number', 'version_name', 'version_status',)
    list_filter = ('version_status',)
    search_fields = ('version_name', 'version_number',)

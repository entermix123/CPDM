from django.contrib import admin

from CPDM.activities.models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
    list_filter = ('title', 'date')
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
    ordering = ('title',)

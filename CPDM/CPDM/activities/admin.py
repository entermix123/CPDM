from django.contrib import admin

from CPDM.activities.models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title',)
    search_fields = ('title', 'description')

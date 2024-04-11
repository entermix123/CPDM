from django.contrib import admin


from CPDM.processes.models import Process


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description', 'activities')
    search_fields = ('name', 'description', 'activities')


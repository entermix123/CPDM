from django.contrib import admin


from CPDM.software.models import Software


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'license', 'vendor', 'company')
    list_filter = ('name', 'vendor', 'company')
    search_fields = ('name', 'vendor', 'company')


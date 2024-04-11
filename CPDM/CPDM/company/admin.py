from django.contrib import admin

from CPDM.company.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'website', 'industry', 'owner')
    list_filter = ('type', 'name', 'website', 'industry', 'owner')
    search_fields = ('name', 'website', 'owner')

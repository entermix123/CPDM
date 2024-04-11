from django.contrib import admin


from CPDM.departments.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'owner')
    list_filter = ('name', 'activities', 'company', 'owner')
    search_fields = ('name', 'activities', 'company', 'owner')


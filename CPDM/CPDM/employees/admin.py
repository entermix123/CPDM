from django.contrib import admin


from CPDM.employees.models import Employee


@admin.register(Employee)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'title')
    list_filter = ('first_name', 'last_name', 'title', 'company')
    search_fields = ('first_name', 'last_name', 'title', 'company')


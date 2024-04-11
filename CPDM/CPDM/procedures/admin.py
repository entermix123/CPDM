from django.contrib import admin


from CPDM.procedures.models import Procedure


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'process')
    list_filter = ('name', 'description', 'process')
    search_fields = ('name', 'description', 'process')


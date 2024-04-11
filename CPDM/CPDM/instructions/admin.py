from django.contrib import admin


from CPDM.instructions.models import Instruction


@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description', 'procedures', 'owner')
    search_fields = ('name', 'procedures')


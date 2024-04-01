from django import forms

from CPDM.departments.models import Department
from CPDM.processes.models import Process


class CreateProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ('name', 'description', 'activities',)


class UpdateProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ('name', 'description', 'activities',)


class DeleteProcessForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Process
        fields = ('name', 'description', 'activities',)

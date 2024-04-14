from django import forms

from CPDM.procedures.models import Procedure, ProcedureTask
from CPDM.processes.models import Process


class CreateProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = ('name', 'description', 'process',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['process'].queryset = Process.objects.filter(owner=user)


class UpdateProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = ('name', 'description', 'process',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['process'].queryset = Process.objects.filter(owner=user)


class DeleteProcedureForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['process'].queryset = Process.objects.filter(owner=user)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Procedure
        fields = ('name', 'description', 'process',)


class CreateProcedureTaskForm(forms.ModelForm):
    class Meta:
        model = ProcedureTask
        fields = ('description', 'duration_days',)


class UpdateProcessTaskForm(forms.ModelForm):
    class Meta:
        model = ProcedureTask
        fields = ('description', 'duration_days',)


class DeleteProcessTaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = ProcedureTask
        fields = ('description', 'duration_days',)

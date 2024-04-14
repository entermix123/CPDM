from django import forms

from CPDM.activities.models import Activity
from CPDM.processes.models import Process


class CreateProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ('name', 'description', 'activities',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['activities'].queryset = Activity.objects.filter(owner=user)


class UpdateProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ('name', 'description', 'activities',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['activities'].queryset = Activity.objects.filter(owner=user)


class DeleteProcessForm(forms.ModelForm):

    class Meta:
        model = Process
        fields = ('name', 'description', 'activities',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['activities'].queryset = Activity.objects.filter(owner=user)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

from django import forms

from CPDM.activities.models import Activity
from CPDM.company.models import Company
from CPDM.departments.models import Department
from CPDM.processes.models import Process


class CreateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name', 'company', 'activities', 'processes', )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['activities'].queryset = Activity.objects.filter(owner=user)
            self.fields['processes'].queryset = Process.objects.filter(owner=user)
            self.fields['company'].queryset = Company.objects.filter(owner=user)


class UpdateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name', 'company', 'activities', 'processes', )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['activities'].queryset = Activity.objects.filter(owner=user)
            self.fields['processes'].queryset = Process.objects.filter(owner=user)
            self.fields['company'].queryset = Company.objects.filter(owner=user)


class DeleteDepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('name', 'company', 'activities', 'processes', )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['activities'].queryset = Activity.objects.filter(owner=user)
            self.fields['processes'].queryset = Process.objects.filter(owner=user)
            self.fields['company'].queryset = Company.objects.filter(owner=user)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

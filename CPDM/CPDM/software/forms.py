from django import forms

from CPDM.company.models import Company
from CPDM.departments.models import Department
from CPDM.software.models import Software


class CreateSoftwareForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['vendor'].widget.attrs['placeholder'] = 'https://..'
        if user:
            self.fields['departments'].queryset = Department.objects.filter(owner=user)
            self.fields['company'].queryset = Company.objects.filter(owner=user)

    class Meta:
        model = Software
        fields = ('name', 'version', 'license', 'vendor', 'departments', 'company')


class UpdateSoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ('name', 'version', 'license', 'vendor', 'departments', 'company')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['departments'].queryset = Department.objects.filter(owner=user)
            self.fields['company'].queryset = Company.objects.filter(owner=user)


class DeleteSoftwareForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['departments'].queryset = Department.objects.filter(owner=user)
            self.fields['company'].queryset = Company.objects.filter(owner=user)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Software
        fields = ('name', 'version', 'license', 'vendor', 'departments', 'company')

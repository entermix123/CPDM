from django import forms

from CPDM.company.models import Company
from CPDM.departments.models import Department
from CPDM.employees.models import Employee


class CreateEmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['department'].queryset = Department.objects.filter(owner=user)
            self.fields['company'].queryset = Company.objects.filter(owner=user)

        # Set email field
        self.fields['title'].widget.attrs['placeholder'] = 'Enter seniority and position'
        self.fields['title'].help_text = 'Enter seniority and position'

    class Meta:
        model = Employee
        # help_text_title="Enter seniority and position"
        fields = ('first_name', 'last_name', 'title', 'salary', 'department', 'company')


class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # help_text_title="Enter seniority and position"
        fields = ('first_name', 'last_name', 'title', 'salary', 'department', 'company')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['department'].queryset = Department.objects.filter(owner=user)
            self.fields['company'].queryset = Company.objects.filter(owner=user)


class DeleteEmployeeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['department'].queryset = Department.objects.filter(owner=user)
            self.fields['company'].queryset = Company.objects.filter(owner=user)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'title', 'salary', 'department', 'company')

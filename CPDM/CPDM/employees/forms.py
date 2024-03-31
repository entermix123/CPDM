from django import forms

from CPDM.employees.models import Employee


class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

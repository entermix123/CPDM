from django import forms

from CPDM.departments.models import Department


class CreateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name', 'company', 'activities', 'processes', )


class UpdateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name', 'company', 'activities', 'processes', )


class DeleteDepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('name', 'company', 'activities', 'processes', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

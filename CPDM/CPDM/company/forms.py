from django import forms

from CPDM.company.models import Company


class CompanyCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['website'].widget.attrs['placeholder'] = 'https://..'

    class Meta:
        model = Company
        fields = ('type', 'name', 'industry', 'website')


class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('type', 'name', 'industry', 'website')


class CompanyDeleteForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('type', 'name', 'industry', 'website')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

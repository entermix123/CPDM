from django import forms

from CPDM.company.models import Company


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('type', 'name', 'industry', 'website')


class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('type', 'name', 'industry', 'website')

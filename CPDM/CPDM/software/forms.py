from django import forms

from CPDM.software.models import Software


class CreateSoftwareForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateSoftwareForm, self).__init__(*args, **kwargs)
        self.fields['vendor'].widget.attrs['placeholder'] = 'https://..'

    class Meta:
        model = Software
        fields = ('name', 'version', 'license', 'vendor', 'departments', 'company')


class UpdateSoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ('name', 'version', 'license', 'vendor', 'departments', 'company')


class DeleteSoftwareForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Software
        fields = ('name', 'version', 'license', 'vendor', 'departments', 'company')

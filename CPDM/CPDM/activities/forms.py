from django import forms

from CPDM.activities.models import Activity


class ActivityCreateForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('title', 'description')


class ActivityUpdateForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('title', 'description')


class DeleteActivityForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Activity
        fields = ('title', 'description')

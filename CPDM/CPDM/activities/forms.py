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

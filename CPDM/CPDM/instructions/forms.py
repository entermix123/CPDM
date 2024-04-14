from django import forms

from CPDM.instructions.models import Instruction
from CPDM.procedures.models import Procedure


class CreateInstructionForm(forms.ModelForm):

    class Meta:
        model = Instruction
        fields = ('name', 'description', 'procedures',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['procedures'].queryset = Procedure.objects.filter(owner=user)


class UpdateInstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ('name', 'description', 'procedures',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['procedures'].queryset = Procedure.objects.filter(owner=user)


class DeleteInstructionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['procedures'].queryset = Procedure.objects.filter(owner=user)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Instruction
        fields = ('name', 'description', 'procedures',)

from django import forms

from CPDM.instructions.models import Instruction


class CreateInstructionForm(forms.ModelForm):

    class Meta:
        model = Instruction
        fields = ('name', 'description', 'procedures',)


class UpdateInstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ('name', 'description', 'procedures',)


class DeleteInstructionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Instruction
        fields = ('name', 'description', 'procedures',)

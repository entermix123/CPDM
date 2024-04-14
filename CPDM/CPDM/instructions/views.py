from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from CPDM.accounts.models import Profile
from CPDM.instructions.forms import CreateInstructionForm, UpdateInstructionForm, DeleteInstructionForm
from CPDM.instructions.models import Instruction


class CreateInstructionView(LoginRequiredMixin, CreateView):
    form_class = CreateInstructionForm
    model = Instruction
    template_name = 'instructions/create_instruction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.filter(pk=self.request.user.pk)
        context['profile'] = profile
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('instructions_list', kwargs={'pk': self.request.user.pk})


class UpdateInstructionView(LoginRequiredMixin, UpdateView):
    form_class = UpdateInstructionForm
    template_name = 'instructions/update_instruction.html'

    def get_object(self, **kwargs):
        obj = get_object_or_404(Instruction, pk=self.kwargs.get('instruction_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        instruction_id = self.kwargs['instruction_id']
        context['profile'] = profile
        context['instruction_id'] = instruction_id
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'instruction_details',
            kwargs={
                'pk': self.request.user.pk,
                'instruction_id': self.kwargs['instruction_id']}
        )


class ListInstructionsView(LoginRequiredMixin, ListView):
    model = Instruction
    template_name = 'instructions/list_instructions.html'

    def get_queryset(self):
        queryset = Instruction.objects.filter(owner=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context


class DetailsInstructionView(LoginRequiredMixin, DetailView):
    template_name = 'instructions/instruction_details.html'

    def get_object(self, **kwargs):
        obj = get_object_or_404(Instruction, pk=self.kwargs.get('instruction_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user

        return context

    def get_success_url(self):
        return reverse_lazy('instructions_list', kwargs={'pk': self.request.user.pk})


class DeleteInstructionView(LoginRequiredMixin, DeleteView):
    form_class = DeleteInstructionForm
    template_name = 'instructions/delete_instruction.html'
    form_class.base_fields['name'].disabled = True
    form_class.base_fields['description'].disabled = True
    form_class.base_fields['procedures'].disabled = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context

    def get_object(self, **kwargs):
        obj = get_object_or_404(Instruction, pk=self.kwargs.get('instruction_id'))
        return obj

    # populate the form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['instance'] = self.object
        return kwargs

    def get_success_url(self):
        return reverse_lazy('instructions_list', kwargs={'pk': self.request.user.pk})
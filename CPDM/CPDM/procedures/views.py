from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from CPDM.accounts.models import Profile
from CPDM.procedures.forms import CreateProcedureForm, UpdateProcedureForm, DeleteProcedureForm
from CPDM.procedures.models import Procedure


class CreateProcedureView(LoginRequiredMixin, CreateView):
    form_class = CreateProcedureForm
    model = Procedure
    template_name = 'procedures/create_procedure.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Procedure.objects.filter(owner=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.filter(pk=self.request.user.pk)
        context['profile'] = profile
        return context

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('procedures_list', kwargs={'pk': self.request.user.pk})


class UpdateProcedureView(LoginRequiredMixin, UpdateView):
    form_class = UpdateProcedureForm
    template_name = 'procedures/procedure_update.html'

    def get_object(self):
        obj = get_object_or_404(Procedure, pk=self.kwargs.get('procedure_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        procedure_id = self.kwargs['procedure_id']
        context['profile'] = profile
        context['procedure_id'] = procedure_id
        return context

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'procedure_details',
            kwargs={
                'pk': self.request.user.pk,
                'procedure_id': self.kwargs['procedure_id']}
        )


class ListProcedureView(LoginRequiredMixin, ListView):
    model = Procedure
    template_name = 'procedures/list_procedures.html'

    def get_queryset(self):
        queryset = Procedure.objects.filter(owner=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context


class DetailsProcedureView(LoginRequiredMixin, DetailView):
    template_name = 'procedures/procedure_details.html'

    def get_object(self):
        obj = get_object_or_404(Procedure, pk=self.kwargs.get('procedure_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user

        return context

    def get_success_url(self):
        return reverse_lazy('procedures_list', kwargs={'pk': self.request.user.pk})


class DeleteProcedureView(LoginRequiredMixin, DeleteView):
    form_class = DeleteProcedureForm
    template_name = 'procedures/delete_procedure.html'
    form_class.base_fields['name'].disabled = True
    form_class.base_fields['description'].disabled = True
    form_class.base_fields['process'].disabled = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context

    def get_object(self):
        obj = get_object_or_404(Procedure, pk=self.kwargs.get('procedure_id'))
        return obj

    # populate the form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def get_success_url(self):
        return reverse_lazy('procedures_list', kwargs={'pk': self.request.user.pk})

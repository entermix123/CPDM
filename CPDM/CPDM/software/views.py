from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from CPDM.accounts.models import Profile
from CPDM.software.forms import CreateSoftwareForm, UpdateSoftwareForm, DeleteSoftwareForm
from CPDM.software.models import Software


class CreateSoftwareView(LoginRequiredMixin, CreateView):
    form_class = CreateSoftwareForm
    model = Software
    template_name = 'software/create_software.html'

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
        return reverse_lazy('software_list', kwargs={'pk': self.request.user.pk})


class UpdateSoftwareView(LoginRequiredMixin, UpdateView):
    form_class = UpdateSoftwareForm
    template_name = 'software/software_update.html'

    def get_object(self, **kwargs):
        obj = get_object_or_404(Software, pk=self.kwargs.get('software_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        software_id = self.kwargs['software_id']
        context['profile'] = profile
        context['software_id'] = software_id
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
            'software_details',
            kwargs={
                'pk': self.request.user.pk,
                'software_id': self.kwargs['software_id']}
        )


class ListSoftwareView(LoginRequiredMixin, ListView):
    model = Software
    template_name = 'software/list_software.html'

    def get_queryset(self):
        queryset = Software.objects.filter(owner=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context


class DetailsSoftwareView(LoginRequiredMixin, DetailView):
    template_name = 'software/software_details.html'

    def get_object(self, **kwargs):
        obj = get_object_or_404(Software, pk=self.kwargs.get('software_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context

    def get_success_url(self):
        return reverse_lazy('software_list', kwargs={'pk': self.request.user.pk})


class DeleteSoftwareView(LoginRequiredMixin, DeleteView):
    form_class = DeleteSoftwareForm
    template_name = 'software/delete_software.html'
    form_class.base_fields['name'].disabled = True
    form_class.base_fields['version'].disabled = True
    form_class.base_fields['license'].disabled = True
    form_class.base_fields['vendor'].disabled = True
    form_class.base_fields['departments'].disabled = True
    form_class.base_fields['company'].disabled = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context

    def get_object(self, **kwargs):
        obj = get_object_or_404(Software, pk=self.kwargs.get('software_id'))
        return obj

    # populate the form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['instance'] = self.object
        return kwargs

    def get_success_url(self):
        return reverse_lazy('software_list', kwargs={'pk': self.request.user.pk})
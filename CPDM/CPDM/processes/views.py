from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from CPDM.accounts.models import Profile
from CPDM.departments.models import Department
from CPDM.processes.forms import CreateProcessForm, UpdateProcessForm, DeleteProcessForm
from CPDM.processes.models import Process


class CreateProcessView(LoginRequiredMixin, CreateView):
    form_class = CreateProcessForm
    model = Process
    template_name = 'processes/create_process.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Department.objects.filter(owner=user)
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
        return reverse_lazy('process_list', kwargs={'pk': self.request.user.pk})


class UpdateProcessView(LoginRequiredMixin, UpdateView):
    form_class = UpdateProcessForm
    template_name = 'processes/process_update.html'

    def get_object(self):
        obj = get_object_or_404(Process, pk=self.kwargs.get('process_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        process_id = self.kwargs['process_id']
        context['profile'] = profile
        context['process_id'] = process_id
        return context

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'process_details',
            kwargs={
                'pk': self.request.user.pk,
                'process_id': self.kwargs['process_id']}
        )


class ListProcessView(LoginRequiredMixin, ListView):
    model = Process
    template_name = 'processes/list_process.html'

    def get_queryset(self):
        queryset = Process.objects.filter(owner=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context


class DetailsProcessView(LoginRequiredMixin, DetailView):
    template_name = 'processes/process_details.html'

    def get_object(self):
        obj = get_object_or_404(Process, pk=self.kwargs.get('process_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context

    def get_success_url(self):
        return reverse_lazy('process_list', kwargs={'pk': self.request.user.pk})


def process_details(request, pk, process_id):
    profile = Profile.objects.get(pk=request.user.pk)
    process = Process.objects.get(pk=process_id)

    form = UpdateProcessForm(instance=process)
    if request.method == 'POST':
        form = UpdateProcessForm(request.POST, instance=process)
        if form.is_valid():
            form.save()
            return redirect('process_list', pk=pk)

    context = {
        'process': process,
        'profile': profile,
        'form': form,
    }
    return render(request, 'processes/process_details.html', context)


def process_update(request, pk, process_id):
    profile = Profile.objects.get(pk=request.user.pk)
    process = Department.objects.get(pk=process_id)

    form = CreateProcessForm(instance=process)
    if request.method == 'POST':
        form = UpdateProcessForm(request.POST, instance=process)
        if form.is_valid():
            form.save()
            return redirect('process_list', pk=pk)

    context = {
        'process': process,
        'profile': profile,
        'form': form,
    }
    return render(request, 'processes/process_update.html', context)


class DeleteProcessView(LoginRequiredMixin, DeleteView):
    form_class = DeleteProcessForm
    template_name = 'processes/delete_process.html'
    form_class.base_fields['name'].disabled = True
    form_class.base_fields['description'].disabled = True
    form_class.base_fields['activities'].disabled = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context

    def get_object(self):
        obj = get_object_or_404(Process, pk=self.kwargs.get('process_id'))
        return obj

    # populate the form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def get_success_url(self):
        return reverse_lazy('process_list', kwargs={'pk': self.request.user.pk})


def delete_process(request, pk, process_id):
    profile = Profile.objects.get(pk=pk)
    process = Process.objects.get(pk=process_id)

    form = DeleteProcessForm(instance=process)
    if request.method == 'POST':
        process.delete()
        return redirect('process_list', pk=request.user.pk)

    context = {
        'profile': profile,
        'process': process,
        'form': form,
    }

    return render(request, 'processes/delete_process.html', context)

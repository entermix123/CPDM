from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from CPDM.accounts.models import Profile
from CPDM.departments.forms import UpdateDepartmentForm, CreateDepartmentForm, DeleteDepartmentForm
from CPDM.departments.models import Department


class CreateDepartmentView(LoginRequiredMixin, CreateView):
    form_class = CreateDepartmentForm
    model = Department
    template_name = 'departments/create_department.html'

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
        return reverse_lazy('activity_list', kwargs={'pk': self.request.user.pk})


class UpdateDepartmentView(LoginRequiredMixin, UpdateView):
    form_class = UpdateDepartmentForm
    template_name = 'departments/department_update.html'

    def get_object(self):
        obj = get_object_or_404(Department, pk=self.kwargs.get('department_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        department_id = self.kwargs['department_id']
        context['profile'] = profile
        context['department_id'] = department_id
        return context

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('departments_list', kwargs={'pk': self.request.user.pk})


class ListDepartmentsView(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'departments/list_department.html'

    def get_queryset(self):
        queryset = Department.objects.filter(owner=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context


class DetailsDepartmentView(LoginRequiredMixin, DetailView):
    template_name = 'departments/department_details.html'

    def get_object(self):
        obj = get_object_or_404(Department, pk=self.kwargs.get('department_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user

        return context

    def get_success_url(self):
        return reverse_lazy('activity_list', kwargs={'pk': self.request.user.pk})


def department_details(request, pk, department_id):
    profile = Profile.objects.get(pk=request.user.pk)
    department = Department.objects.get(pk=department_id)

    form = UpdateDepartmentForm(instance=department)
    if request.method == 'POST':
        form = UpdateDepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('departments_list', pk=pk)

    context = {
        'activity': department,
        'profile': profile,
        'form': form,
    }
    return render(request, 'departments/department_details.html', context)


def department_update(request, pk, department_id):
    profile = Profile.objects.get(pk=request.user.pk)
    department = Department.objects.get(pk=department_id)

    form = CreateDepartmentForm(instance=department)
    if request.method == 'POST':
        form = UpdateDepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('departments_list', pk=pk)

    context = {
        'department': department,
        'profile': profile,
        'form': form,
    }
    return render(request, 'departments/department_update.html', context)


class DeleteDepartmentView(LoginRequiredMixin, DeleteView):
    form_class = DeleteDepartmentForm
    template_name = 'departments/delete_department.html'
    form_class.base_fields['name'].disabled = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context

    def get_object(self):
        obj = get_object_or_404(Department, pk=self.kwargs.get('department_id'))
        return obj

    # populate the form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def get_success_url(self):
        return reverse_lazy('departments_list', kwargs={'pk': self.request.user.pk})


def delete_activity(request, pk, department_id):
    profile = Profile.objects.get(pk=pk)
    department = Department.objects.get(pk=department_id)

    form = DeleteDepartmentForm(instance=department)
    if request.method == 'POST':
        department.delete()
        return redirect('departments_list', pk=request.user.pk)

    context = {
        'profile': profile,
        'department': department,
        'form': form,
    }

    return render(request, 'departments/delete_department.html', context)

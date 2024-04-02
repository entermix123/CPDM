from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from CPDM.accounts.models import Profile
from CPDM.employees.forms import CreateEmployeeForm, UpdateEmployeeForm, DeleteEmployeeForm
from CPDM.employees.models import Employee


class CreateEmployeeView(LoginRequiredMixin, CreateView):
    form_class = CreateEmployeeForm
    model = Employee
    template_name = 'employees/create_employee.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Employee.objects.filter(company_owner=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.filter(pk=self.request.user.pk)
        context['profile'] = profile
        return context

    def form_valid(self, form):
        form.instance.company_owner_id = self.request.user.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employees_list', kwargs={'pk': self.request.user.pk})


class UpdateEmployeeView(LoginRequiredMixin, UpdateView):
    form_class = UpdateEmployeeForm
    template_name = 'employees/update_employee.html'

    def get_object(self):
        obj = get_object_or_404(Employee, pk=self.kwargs.get('employee_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        employee_id = self.kwargs['employee_id']
        context['profile'] = profile
        context['employee_id'] = employee_id
        return context

    def form_valid(self, form):
        form.instance.company_owner_id = self.request.user.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employees_list', kwargs={'pk': self.request.user.pk})


class ListEmployeesView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employees/list_employees.html'

    def get_queryset(self):
        queryset = Employee.objects.filter(company_owner=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context


class DetailsEmployeeView(LoginRequiredMixin, DetailView):
    template_name = 'employees/employee_details.html'

    def get_object(self):
        obj = get_object_or_404(Employee, pk=self.kwargs.get('employee_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user

        return context

    def get_success_url(self):
        return reverse_lazy('employees_list', kwargs={'pk': self.request.user.pk})


class DeleteEmployeeView(LoginRequiredMixin, DeleteView):
    form_class = DeleteEmployeeForm
    template_name = 'employees/delete_employee.html'
    form_class.base_fields['first_name'].disabled = True
    form_class.base_fields['last_name'].disabled = True
    form_class.base_fields['title'].disabled = True
    form_class.base_fields['salary'].disabled = True
    form_class.base_fields['department'].disabled = True
    form_class.base_fields['company'].disabled = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context

    def get_object(self):
        obj = get_object_or_404(Employee, pk=self.kwargs.get('employee_id'))
        return obj

    # populate the form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def get_success_url(self):
        return reverse_lazy('employees_list', kwargs={'pk': self.request.user.pk})
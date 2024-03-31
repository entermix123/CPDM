from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from CPDM.employees.forms import CreateEmployeeForm, UpdateEmployeeForm
from CPDM.employees.models import Employee


class CreateEmployeeView(CreateView):
    model = Employee
    template_name = 'employees/create_employee.html'
    form_class = CreateEmployeeForm

    def get_queryset(self):
        user = self.request.user
        queryset = Employee.objects.filter(company_owner=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        context['profile'] = profile
        return context

    def form_valid(self, form):
        form.instance.company_owner_id = self.request.user.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employees_list', kwargs={'pk': self.request.user.pk})


class EmployeesListView(ListView):
    model = Employee
    template_name = 'employees/list_employees.html'

    def get_queryset(self):
        queryset = Employee.objects.filter(company_owner=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user
        return context


class EmployeesDetailView(DetailView):
    form_class = UpdateEmployeeForm
    model = Employee
    template_name = 'employees/employees_details.html'


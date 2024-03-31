from django.urls import path

from CPDM.employees.views import CreateEmployeeView, EmployeesListView, EmployeesDetailView

urlpatterns = (
    path('create/', CreateEmployeeView.as_view(), name='employee_create'),
    path('details/', EmployeesDetailView.as_view(), name='employee_details'),
    path('list/', EmployeesListView.as_view(), name='employees_list'),
)

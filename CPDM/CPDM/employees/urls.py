from django.urls import path

from CPDM.employees.views import CreateEmployeeView, ListEmployeesView, UpdateEmployeeView, DetailsEmployeeView, \
    DeleteEmployeeView

urlpatterns = (
    path('create/', CreateEmployeeView.as_view(), name='employee_create'),
    path('list/', ListEmployeesView.as_view(), name='employees_list'),
    path('details/<int:employee_id>/', DetailsEmployeeView.as_view(), name='employee_details'),
    path('update/<int:employee_id>/', UpdateEmployeeView.as_view(), name='update_employee'),
    path('delete/<int:employee_id>/', DeleteEmployeeView.as_view(), name='delete_employee'),
)

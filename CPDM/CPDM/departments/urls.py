from django.urls import path


from CPDM.departments.views import CreateDepartmentView, ListDepartmentsView, UpdateDepartmentView, \
    DetailsDepartmentView, DeleteDepartmentView, delete_activity, department_details, department_update

urlpatterns = (
    path('create/', CreateDepartmentView.as_view(), name='department_create'),
    path('list/', ListDepartmentsView.as_view(), name='departments_list'),
    path('details/<int:department_id>/', DetailsDepartmentView.as_view(), name='department_details'),
    # path('details/<int:department_id>/', department_details, name='activity_details'),
    path('update/<int:department_id>/', UpdateDepartmentView.as_view(), name='department_update'),
    # path('update/<int:department_id>/', department_update, name='activity_update'),
    path('delete/<int:department_id>/', DeleteDepartmentView.as_view(), name='department_delete'),
    # path('delete/<int:department_id>/', delete_activity, name='department_delete'),
)

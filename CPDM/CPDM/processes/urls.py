from django.urls import path

from CPDM.processes.views import CreateProcessView, ListProcessView, DetailsProcessView, UpdateProcessView, \
    DeleteProcessView, process_details, process_update, delete_process

urlpatterns = (
    path('create/', CreateProcessView.as_view(), name='process_create'),
    path('list/', ListProcessView.as_view(), name='process_list'),
    path('details/<int:process_id>/', DetailsProcessView.as_view(), name='process_details'),
    # path('details/<int:process_id>/', process_details, name='process_details'),
    path('update/<int:process_id>/', UpdateProcessView.as_view(), name='process_update'),
    # path('update/<int:process_id>/', process_update, name='process_update'),
    path('delete/<int:process_id>/', DeleteProcessView.as_view(), name='process_delete'),
    # path('delete/<int:process_id>/', delete_process, name='process_delete'),
)

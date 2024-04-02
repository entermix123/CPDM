from django.urls import path

from CPDM.procedures.views import CreateProcedureView, ListProcedureView, DetailsProcedureView, UpdateProcedureView, \
    DeleteProcedureView

urlpatterns = (
    path('create/', CreateProcedureView.as_view(), name='procedure_create'),
    path('list/', ListProcedureView.as_view(), name='procedures_list'),
    path('details/<int:procedure_id>/', DetailsProcedureView.as_view(), name='procedure_details'),
    path('update/<int:procedure_id>/', UpdateProcedureView.as_view(), name='update_procedure'),
    path('delete/<int:procedure_id>/', DeleteProcedureView.as_view(), name='delete_procedure'),
)

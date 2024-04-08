from django.urls import path

from CPDM.software.views import CreateSoftwareView, ListSoftwareView, DetailsSoftwareView, UpdateSoftwareView, \
    DeleteSoftwareView

urlpatterns = (
    path('create/', CreateSoftwareView.as_view(), name='software_create'),
    path('list/', ListSoftwareView.as_view(), name='software_list'),
    path('details/<int:software_id>/', DetailsSoftwareView.as_view(), name='software_details'),
    path('update/<int:software_id>/', UpdateSoftwareView.as_view(), name='software_update'),
    path('delete/<int:software_id>/', DeleteSoftwareView.as_view(), name='software_delete'),
)
